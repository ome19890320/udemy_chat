lines = []
with open ('3.txt', 'r', encoding = 'utf-8-sig') as f :
    for line in f :
        lines.append(line.strip()) # .strip移除換行空白

for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]

    print (name)


