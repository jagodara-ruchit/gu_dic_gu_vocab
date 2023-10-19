with open('new_gujarati_words.txt','r') as f:
    data = f.read().split('\n\n')
file = open('gujarati_words.txt','w')
for i in data:
    file.write(i)
file.close()