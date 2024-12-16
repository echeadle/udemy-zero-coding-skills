import os

def merge_text_files(input_folder, output_file):
    # List all files in the input folder
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    with open(output_file, 'w') as outfile:
        for filename in files:
            filepath = os.path.join(input_folder, filename)
            with open(filepath, 'r') as infile:
                outfile.write(infile.read())
                outfile.write("\n")  # Add a newline after each file's content

if __name__ == "__main__":
    input_folder = "files"
    output_file = "merged_file.txt"
    merge_text_files(input_folder, output_file)
    print(f"All files in '{input_folder}' have been merged into '{output_file}'")
