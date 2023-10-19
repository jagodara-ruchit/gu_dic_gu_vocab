# gu_dic_gu_vocab
This repository contains the necessary code to create gu.dic and gu.vocab files for handling Gujarati language data.

## Getting Started
To generate the gu.dic file, follow these steps:

1. Create a text file named `unique_words.txt` containing a list of Gujarati words, with each word on a new line.

2. Convert the Gujarati words in `unique_words.txt` to Hindi without altering the characters. You can do this easily by using the online tool [Anirdesh Gujarati to Hindi Converter](https://www.anirdesh.com/gujarati/gujarati-to-hindi.php). Simply input the Gujarati words, obtain the corresponding Hindi words, and save them to a text file named "hindi" (without a .txt extension).

3. Run the `convert_hindi_to_XAMPA.py` script. This will generate a file named `converted.txt`.

4. Execute the `mapping.py` script. This will produce a text file that contains Gujarati words mapped to their respective phonemes. Be aware that this file may include some characters not found in `non_silence_phones.txt`. To resolve this, use the `check.py` script to identify words with these uncommon characters.

5. Add these unique characters along with their corresponding replacements in a text file named `non_available.txt`. For example, if you want to replace "@:" with "@," add a line in the format "@: @" in `non_available.txt`. (Note there is a space between @: and @ in the format) 

6. Finally, run the `change_phones.py` script. This script will replace the specified phonemes with their corresponding words, as specified in `non_available.txt`. The result is a text file named `new.dic`, which serves as your final file containing mapped words with their phonemes.

## Verification
After completing the above steps, run the `check.py` script to verify the integrity of your gu.dic file. If the script doesn't output any issues, your process is complete, and your gu.dic and gu.vocab files are ready for use.
