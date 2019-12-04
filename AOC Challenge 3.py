file = open("input.txt","r")
line1 = file.readline().split(",")
line1[-1] = line1[-1][:-1]
line2 = file.readline().split(",")
points1 = []
x = 0
y = 0
DX = {'R': 1, 'L':-1, 'U': 0, 'D': 0}
DY = {'R': 0, 'L':0, 'U': 1, 'D': -1}
ansA = {}
ansB = {}
length = 0
for i in line1:
    
    d = i[0]
    n = int(i[1:])
    for j in range(n):
        x += DX[d]
        y += DY[d]
        length += 1
        ansA[(x,y)] = length
        points1.append([x,y])
x = 0
y = 0
points2 = []
length = 0
for i in line2:
    d = i[0]
    n = int(i[1:])
    for j in range(n):
        x += DX[d]
        y += DY[d]
        length += 1
        ansB[(x,y)] = length
        points2.append([x,y])
intersection = list(set(ansA.keys()) & set(ansB.keys()))
print(ansB[intersection[0]])
print(min([ansA[i] + ansB[i] for i in intersection]))

 

