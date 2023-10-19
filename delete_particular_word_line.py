with open('new.dic','r') as file:
    data = file.read().split('\n')

f = open('new.dic','w')
for i in data:
    d = i.split()
    c = True
    for j in d:
        if j == '@~':
            c = False
            break
    if c:
        f.write(i+'\n')
f.close()