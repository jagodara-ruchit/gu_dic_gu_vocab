import os

# # Replace 'your_folder_path' with the path to the folder you want to list files from
# folder_path = 'files'

# # Get a list of all files in the specified directory
# files = os.listdir(folder_path)
files = ['part1ac']
# Process each file in the folder
for file_name in files:
    # input_file_path = os.path.join(folder_path, file_name)
    input_file_path = file_name
    # Check if it's a file (not a directory)
    if os.path.isfile(input_file_path):
        # Create an empty list to store lines without numbers
        lines_without_numbers = []

        # Open the input file for reading with IBM866 encoding
        with open(input_file_path, 'r') as input_file:
            # Iterate through each line in the input file
            for line in input_file:
                # Check if the line contains any digits
                if not any(char.isdigit() for char in line):
                    # If the line doesn't contain any digits, add it to the list
                    lines_without_numbers.append(line)

        # Specify the output file path
        output_file_path = os.path.join('final_files', 'new_' + file_name)

        # Open a new output file for writing with UTF-8 encoding
        with open(output_file_path, 'w') as output_file:
            # Write the lines without numbers to the output file
            output_file.writelines(lines_without_numbers)
