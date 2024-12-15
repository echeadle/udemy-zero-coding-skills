import os

# Define the parent folder where all subfolders will be created
parent_folder = "all"

# Create the parent folder if it doesn't already exist
os.makedirs(parent_folder, exist_ok=True)

# Loop to create folders named 1a, 2a, ..., 100a
for i in range(1, 101):
    folder_name = f"{i}a"  # Construct the folder name
    folder_path = os.path.join(parent_folder, folder_name)  # Full path to the folder
    os.makedirs(folder_path, exist_ok=True)  # Create the folder

print(f"Created 100 folders named '1a' to '100a' inside the '{parent_folder}' folder.")
