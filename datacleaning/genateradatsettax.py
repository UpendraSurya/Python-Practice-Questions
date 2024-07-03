import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Number of rows
n = 10000

# Create dataset
data = {
    'taxpayer_id': np.arange(1, n + 1),
    'age': np.random.randint(18, 80, n),
    'monthly_income': np.random.normal(5000, 1500, n),  # Changed to 1D array
    'Dependents': np.random.randint(0, 5, n),
    'states': np.random.choice([
        'AP', 'AR', 'AS', 'BR', 'CG', 'GA', 'GJ', 'HR', 'HP', 'JH', 'KA', 'KL', 'MP',
        'MH', 'MN', 'ML', 'MZ', 'NL', 'OR', 'PB', 'RJ', 'SK', 'TN', 'TS', 'TR', 'UP',
        'UK', 'WB'
    ], n),
    'FiledLate': np.random.choice([0, 1], n),
    'PropertyValue': np.random.normal(300000, 100000, n),
    'LoanAmount': np.random.normal(200000, 80000, n),
    'CreditScore': np.random.randint(300, 850, n),
    'MaritalStatus': np.random.choice(['Single', 'Married', 'Divorced', 'Widowed'], n),
    'EmploymentStatus': np.random.choice(['Employed', 'Unemployed', 'Self-Employed', 'Retired'], n),
    'EducationLevel': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n),
    'HealthExpenses': np.random.normal(5000, 2000, n)
}

data['annual_income'] = data['monthly_income'] * 12

# Function to calculate tax
def calculate_tax(income):
    tax_brackets = [
        (10000, 0.00),  # up to $10,000 at 0%
        (30000, 0.10),  # $10,001 to $30,000 at 10%
        (60000, 0.20),  # $30,001 to $60,000 at 20%
        (float('inf'), 0.30)  # over $60,000 at 30%
    ]

    tax = 0.0
    previous_limit = 0

    for limit, rate in tax_brackets:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break

    return tax

# Convert to DataFrame
df = pd.DataFrame(data)

# Apply the function to the 'annual_income' column and create a new 'tax' column
df['tax'] = df['annual_income'].apply(calculate_tax)

# Introduce missing values in specified columns
for col in ['age', 'PropertyValue', 'CreditScore', 'monthly_income','annual_income','tax']:
    nan_indices = np.random.choice(df.index, size=int(len(df) * 0.1), replace=False)
    df.loc[nan_indices, col] = np.nan

for col in [ 'Dependents','LoanAmount', 'HealthExpenses']:
    nan_indices = np.random.choice(df.index, size=int(len(df) *0.3), replace=False)
    df.loc[nan_indices, col] = np.nan

# Display the first few rows of the DataFrame
print(df.head())

#%%
df.to_csv('dirty.csv',index=False)
#%%
