# Import packages
import pandas as pd

# Section 1: Creating the survey-specific API call

# Greet user and ask for survey name
print("To start this script, you will need to enter the survey's ID in the CCYYYYTTT format.")
print("Please enter the survey ID:")
svy = input()

# Construct the two API calls
api_call1 = "https://api.dhsprogram.com/rest/dhs/data/" + svy + ",RH_ANCN_W_N4P,FP_CUSM_W_MOD,FP_NADM_W_PDM,FP_NADM_W_UNT,ED_LITR_W_LIT,AN_ANEM_W_ANY?f=csv"
api_call2 = "https://api.dhsprogram.com/rest/dhs/data/" + svy + ",CH_VACC_C_DP3,CH_VACC_C_MSL,RH_DELP_C_DHF,CH_VACC_C_DP1,CH_VACC_C_BAS,CH_VAC1_C_VCD,CH_VACC_C_M22,CH_VACC_C_PN3?f=csv"
api_call3 = "https://api.dhsprogram.com/rest/dhs/data/" + svy + ",ED_LITR_M_LIT,AH_TOBC_M_NON,WS_TLET_P_NFC,WS_SRCE_P_IMP,ML_ITNA_P_ACC,CN_NUTS_C_HA2?f=csv"

print("Here are your API calls:")
print("Women's indicators: " + api_call1)
print("Children's vaccination indicators: " + api_call2)
print("Household indicators: " + api_call3)

# Section 2: Creating and merging data frames

# Creates two temporary dataframes containing the data from the two API calls
print("Adding API extracts to data frames...")
df_temp1 = pd.read_csv(api_call1)
df_temp2 = pd.read_csv(api_call2)
df_temp3 = pd.read_csv(api_call3)

df_list = [df_temp1, df_temp2, df_temp3]

# Merges the dataframes
print("Concatenating the data frames...")
df_merged = pd.concat(df_list)

# Section 3: Exporting the dataframe to a CSV

# Selects the 'preferred' indicators (removes indicators with duplicate IDs)
df_merged = df_merged.loc[df_merged["IsPreferred"] == 1]

# Filters out the unnecessary API variables
api_vars = ["Indicator", "Value", "IndicatorId", "SDRID", "DenominatorWeighted", "DenominatorUnweighted"]
df_merged = df_merged.filter(api_vars)

print("Exporting the data frame to a CSV...")
df_merged.to_csv("API_extract.csv")
