from epitran.backoff import Backoff

# Create a Backoff transliterator for Hindi Devanagari script
backoff = Backoff(['hin-Deva'])

# Function to convert a single word to X-SAMPA format
def convert_to_xsampa(word):
    xsampa_list = backoff.xsampa_list(word)
    xsampa_str = ' '.join(xsampa_list)
    return f"{word} {xsampa_str}"

# Input and output file paths
input_file = 'hindi'
output_file = 'converted.txt'

# Open the input and output files
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        word = line.strip()
        xsampa_output = convert_to_xsampa(word)
        outfile.write(f"{word} {xsampa_output}\n")

print("Conversion completed. Results saved to 'converted.txt'")
