import os

# Original list of names
names = [
    "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Amelia", "Charlotte",
    "Harper", "Evelyn", "Abigail", "Emily", "Ella", "Elizabeth", "Sofia", "Avery",
    "Scarlett", "Madison", "Lily", "Grace", "Chloe", "Victoria", "Riley", "Aria",
    "Zoey", "Luna", "Layla", "Mila", "Nora", "Hannah", "Ellie", "Bella", "Addison",
    "Aubrey", "Natalie", "Stella", "Maya", "Paisley", "Audrey", "Brooklyn", "Savannah",
    "Skylar", "Claire", "Hazel", "Lucy", "Sadie", "Alexa", "Penelope", "Ariana",
    "Alice", "Anna", "Ruby", "Caroline", "Samantha", "Autumn", "Leah", "Isla",
    "Quinn", "Ivy", "Violet", "Genesis", "Josephine", "Delilah", "Naomi",
    "Mackenzie", "Serenity", "Madeline", "Eva", "Brielle", "Gabriella",
    "Cora", "Allison", "Sophie", "Piper", "Jade", "Jasmine", "Rylee", "Kylie", 
    "Clara", "Faith", "Andrea", "Willow", "Vivian", "Amaya", "Alyssa", "Molly",
    "Lila", "Elena", "Reagan", "Alexandra", "Eliana", "Jocelyn", "Arianna", 
    "Maria", "Adeline", "Arya", "Kennedy"  # Ensure all names are present
]

# Deduplicate names
unique_names = list(dict.fromkeys(names))

# Check how many names are missing
if len(unique_names) < 100:
    print(f"Warning: Only {len(unique_names)} unique names found. Adding more to reach 100.")
    # Generate more unique names to fill the gap
    while len(unique_names) < 100:
        unique_names.append(f"Name_{len(unique_names) + 1}")

# Folder name where files will be stored
folder_name = "names"

# Ensure the folder exists
os.makedirs(folder_name, exist_ok=True)

# Create a text file for each name
for i, name in enumerate(unique_names, start=1):
    file_path = os.path.join(folder_name, f"name_{i}.txt")
    with open(file_path, 'w') as file:
        file.write(name)

print(f"Successfully created {len(unique_names)} text files in the '{folder_name}' folder.")
