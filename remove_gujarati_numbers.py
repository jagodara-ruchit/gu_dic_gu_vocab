import re

# Function to check if a word contains Gujarati numbers
def contains_gujarati_numbers(word):
    gujarati_numbers = set('૦૧૨૩૪૫૬૭૮૯')
    return any(char in gujarati_numbers for char in word)

# Input file path and output file path
input_file_path = 'unique_words.txt'
output_file_path = 'new_gujarati_words.txt'

# Read the input file and remove words with Gujarati numbers
with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        words = line.split()
        filtered_words = [word for word in words if not contains_gujarati_numbers(word)]
        output_line = ' '.join(filtered_words)
        output_file.write(output_line + '\n')

print("Words with Gujarati numbers removed. Output saved to 'output.txt'.")
