# Read the contents of converted.txt and output.txt
with open('converted.txt', 'r', encoding='utf-8') as converted_file:
    converted_lines = converted_file.readlines()

with open('unique_words.txt', 'r', encoding='utf-8') as output_file:
    output_lines = output_file.readlines()

# Create a mapping between the first words in converted.txt and output.txt
word_mapping = {}
for converted_line, output_line in zip(converted_lines, output_lines):
    converted_word = converted_line.split()[0]
    output_word = output_line.strip()
    word_mapping[converted_word] = output_word

# Create a new file with updated content
with open('new_old.dic', 'w', encoding='utf-8') as updated_file:
    for line in converted_lines:
        parts = line.split()
        if len(parts) >= 1:
            first_word = parts[0]
            rest_of_line = ' '.join(parts[2:])
            if first_word in word_mapping:
                updated_line = word_mapping[first_word] + ' ' + rest_of_line + '\n'
                updated_file.write(updated_line)
            else:
                updated_file.write(line)
        else:
            updated_file.write(line)

print("Conversion complete. Check 'new_old.dic' for the result.")
