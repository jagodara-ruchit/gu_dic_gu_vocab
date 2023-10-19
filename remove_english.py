import regex as re

# Input and output file names
input_file = "final_files/new_part1ac"
output_file = "gujarati_words.txt"

# Regular expression pattern to match Gujarati words
gujarati_pattern = r'\p{script=Gujarati}+'

# Open the input and output files
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    # Iterate through each line in the input file
    for line in infile:
        # Use regex to find Gujarati words in the line
        gujarati_words = re.findall(gujarati_pattern, line)
        
        # Write the Gujarati words to the output file, one word per line
        for word in gujarati_words:
            outfile.write(word + "\n")

print("Gujarati words extracted and saved to", output_file)
