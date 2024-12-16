import os
import pandas as pd

# Path to the folder containing the Excel files
folder_path = 'excel_files'
all_data = []

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an Excel file
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        # Full path to the current Excel file
        file_path = os.path.join(folder_path, filename)
        
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Check if the necessary columns are present
        if set(['employee', 'monthly salary', 'annual salary']).issubset(df.columns):
            # Append the data to the list
            all_data.append(df)
        else:
            print(f'{filename} does not contain the necessary columns.')

# Concatenate all data into a single DataFrame
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # Save the combined DataFrame to a new Excel file
    combined_df.to_excel('all_employees.xlsx', index=False)
    print('Merged data has been saved to all_employees.xlsx')
else:
    print('No files were merged.')
