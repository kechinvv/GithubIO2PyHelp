lines = []
with open(r"C:\Users\valer\PycharmProjects\edsuck2\sucko2.txt", "r") as file:
    for line in file:
        lines.append(line)
i = 56
with open(r"C:\Users\valer\PycharmProjects\edsuck2\suck2.txt", "w") as file:
    for line in lines:
        if len(line) > 2 and line.strip()[0] == "G" and line.strip()[2] == "K":
            i = -1
            file.write(line)
        else:
            if line.strip() != "" and line.strip()[0] != "[":
                i += 1
                file.write("[" + str(i) + "] " + line)
            else:
                file.write(line)
lines = []
with open(r"C:\Users\valer\PycharmProjects\edsuck2\suck2.txt", "r") as file:
    for line in file:
        lines.append(line.split(" "))
print(lines)
dic = {}
for line in lines:
    if 4 < len(line):
        dic[line[4].replace('\n', '')] = line[0]
print(dic)
for line in lines:
    if 2 < len(line) and line[2] in dic.keys():
        ins = dic[line[2]]
        if ins[0] == '[':
            ins = ins[1: -1]
        line.insert(2, ins)
with open(r"C:\Users\valer\PycharmProjects\edsuck2\suck2.txt", "w") as file:
    for line in lines:
        file.write(' '.join(line))
