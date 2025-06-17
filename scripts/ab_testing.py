import pandas as pd
import numpy as np
from scipy import stats

# Load the data with low_memory=False to avoid DtypeWarning
df = pd.read_csv('data/MachineLearningRating_v3.txt', sep='|', low_memory=False)
df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')

# Calculate LossRatio to match EDA approach
df['LossRatio'] = df['TotalClaims'] / df['TotalPremium'].replace(0, np.nan)  # Avoid division by zero

# Focus on key variables, include all rows with available data
df = df[['Province', 'VehicleType', 'TotalClaims', 'TotalPremium', 'LossRatio']]
df = df.dropna()  # Remove rows with missing values
print("Data prepared for A/B testing:", df.head())

# Hypothesis 1: Claim frequency difference by Province (Gauteng vs. others)
gauteng_data = df[df['Province'] == 'Gauteng']['TotalClaims']
other_provinces_data = df[df['Province'] != 'Gauteng']['TotalClaims']

# T-test for claim frequency with data point check
if len(gauteng_data) > 1 and len(other_provinces_data) > 1:
    t_stat, p_value = stats.ttest_ind(gauteng_data, other_provinces_data, equal_var=False)
    print(f"T-statistic (Claim Frequency): {t_stat}, P-value: {p_value}")

    # Interpretation
    alpha = 0.05
    if p_value < alpha:
        print("Reject H0: Significant difference in claim frequency between Gauteng and other provinces.")
    else:
        print("Fail to reject H0: No significant difference detected.")
else:
    print("Warning: Insufficient data points for Province t-test.")

# Hypothesis 2: Claim frequency by VehicleType (Passenger Vehicle vs. others)
passenger_data = df[df['VehicleType'] == 'Passenger Vehicle']['TotalClaims']
other_vehicle_data = df[df['VehicleType'] != 'Passenger Vehicle']['TotalClaims']

# T-test for VehicleType with data point check
if len(passenger_data) > 1 and len(other_vehicle_data) > 1:
    t_stat_vehicle, p_value_vehicle = stats.ttest_ind(passenger_data, other_vehicle_data, equal_var=False)
    print(f"VehicleType T-statistic (Claim Frequency): {t_stat_vehicle}, P-value: {p_value_vehicle}")

    if p_value_vehicle < alpha:
        print("Reject H0: Significant difference in claim frequency between Passenger Vehicles and others.")
    else:
        print("Fail to reject H0: No significant difference detected.")
else:
    print("Warning: Insufficient data points for VehicleType t-test.")

# Hypothesis 3: LossRatio difference by Province (Gauteng vs. others)
gauteng_loss = df[df['Province'] == 'Gauteng']['LossRatio'].dropna()
other_loss = df[df['Province'] != 'Gauteng']['LossRatio'].dropna()

# T-test for LossRatio with data point check
if len(gauteng_loss) > 1 and len(other_loss) > 1:
    t_stat_loss, p_value_loss = stats.ttest_ind(gauteng_loss, other_loss, equal_var=False)
    print(f"LossRatio T-statistic: {t_stat_loss}, P-value: {p_value_loss}")

    if p_value_loss < alpha:
        print("Reject H0: Significant difference in LossRatio between Gauteng and other provinces.")
    else:
        print("Fail to reject H0: No significant difference detected.")
else:
    print("Warning: Insufficient data points for LossRatio t-test.")