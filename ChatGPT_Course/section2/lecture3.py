import os
import pandas as pd

# Path to the folder containing the Excel files
folder_path = 'excel_files'

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an Excel file
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        # Full path to the current Excel file
        file_path = os.path.join(folder_path, filename)
        
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Check if the necessary columns are present
        if 'employee' in df.columns and 'monthly salary' in df.columns:
            # Calculate the annual salary
            df['annual salary'] = df['monthly salary'] * 12
            
            # Save the updated DataFrame back to the Excel file
            df.to_excel(file_path, index=False)
            print(f'Updated {filename}')
        else:
            print(f'{filename} does not contain the necessary columns.')
