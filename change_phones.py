# Open and read the first text file
with open('non_available.txt', 'r', encoding='utf-8') as file1:
    words_file1 = {}
    data = file1.read().split('\n')
    for i in data:
        i = i.split()
        word1 = i[0]
        if len(i)>2:
            word2 = i[1] + ' ' +i[2]
        else:
            word2 = i[1]
        words_file1[word1] = word2

# Open an output file to write the modified lines
output_file = open('new.dic', 'w', encoding='utf-8')

# Open and read the second text file
with open('new_old.dic', 'r', encoding='utf-8') as file2:
    modified_lines = []
    data = file2.read().split('\n')
    for line in data:
        line = line.split()
        for i in range(len(line)):
            c = line[i]
            for word1,word2 in words_file1.items():
                if line[i] == word1:
                    c = word2
                    break
            if i!=len(line)-1:
                output_file.write(c+' ')
            else:
                output_file.write(c+'\n')
        


# Close the files
file1.close()
file2.close()
output_file.close()
