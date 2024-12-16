import pandas as pd

# Load the data from the current directory
file_path = "stockholm_updated.csv"

try:
    data = pd.read_csv(file_path)
    
    # Check if 'TG' column exists
    if 'TG' in data.columns:
        # Calculate the mean temperature
        mean_temperature = data['TG'].mean()
        print(f"The mean temperature is {mean_temperature:.2f} °C")
    else:
        print("The 'TG' column does not exist in the provided CSV file.")
except FileNotFoundError:
    print("The file 'stockholm_updated.csv' was not found in the current directory.")
