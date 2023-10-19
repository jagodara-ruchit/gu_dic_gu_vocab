d = []
with open('new.dic','r') as file:
    data = file.read().split('\n')
file.close()
with open('nonsilence_phones.txt','r') as f:
    d.append(f.read().split('\n'))
d =d[0]
for i in (data):
    for j in (i.split())[1:]:
        
        c = False
        for k in d:

            if j == k:
                c = True
                break
        
        if not c:
                print(j)
f.close()