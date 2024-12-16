import pandas as pd

# Read the original CSV file
df = pd.read_csv('stockholm.csv')

# Make a copy of the DataFrame
df_updated = df.copy()

# Divide all values in the 'TG' column by 10 in the copied DataFrame
df_updated['TG'] = df_updated['TG'] / 10

# Write the modified DataFrame to a new CSV file
df_updated.to_csv('stockholm_updated.csv', index=False)

print("The 'TG' column has been successfully divided by 10 in 'stockholm_updated.csv'.")
