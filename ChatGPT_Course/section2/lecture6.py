import os
import zipfile

# Directory containing the text files
source_dir = 'text_files'
# Output directory for the ZIP files
output_dir = 'zip_files'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to create ZIP files in batches
def create_zip_files(start_index, end_index, batch_size):
    current_batch_start = start_index
    while current_batch_start <= end_index:
        # Determine the end of the current batch
        current_batch_end = min(current_batch_start + batch_size - 1, end_index)
        zip_filename = f'TG_STAID{current_batch_start:06d}_to_TG_STAID{current_batch_end:06d}.zip'
        zip_filepath = os.path.join(output_dir, zip_filename)
        
        # Create a ZIP file and add the text files to it
        with zipfile.ZipFile(zip_filepath, 'w') as zipf:
            for i in range(current_batch_start, current_batch_end + 1):
                filename = f'TG_STAID{i:06d}.txt'
                file_path = os.path.join(source_dir, filename)
                if os.path.exists(file_path):
                    zipf.write(file_path, filename)
        
        # Move to the next batch
        current_batch_start += batch_size

# Parameters for the file batching
start_index = 1
end_index = 400
batch_size = 10

# Create the ZIP files
create_zip_files(start_index, end_index, batch_size)

print("ZIP files created successfully!")
