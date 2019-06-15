from random import randint

n = int(input())

grid = []
for y in range(n):
    grid.append([])
    for x in range(n):
        if y % 2 == 0:
            grid[y] = [1]*n
        elif (y-1) % 4 == 0:
            grid[y] = [0]*n
            grid[y][0] = 1
        else:
            grid[y] = [0]*n
            grid[y][n-1] = 1

ends = [[0,n-1],[n-1,]]

def getZeros(x,y):
    adj=[]
    if y+1 < n:
        if grid[x][y+1] == 0:
            adj.append((x,y+1))
    if y-1 >= 0:
        if grid[x][y-1] == 0:
            adj.append((x,y-1))
    if x+1 < n:
        if grid[x+1][y] == 0:
            adj.append((x+1,y))
    if x-1 >= 0:
        if grid[x-1][y] == 0:
            adj.append((x-1,y))
    return adj

def getAll(x,y):
    adj=[]
    if y+1 < n:
        adj.append((x,y+1))
    if y-1 >= 0:
        adj.append((x,y-1))
    if x+1 < n:
        adj.append((x+1,y))
    if x-1 >= 0:
        adj.append((x-1,y))
    return adj

def getAdj(x,y):
    adj=[]
    if y+1 < n:
        if grid[x][y+1] == 1:
            adj.append((x,y+1))
    if y-1 >= 0:
        if grid[x][y-1] == 1:
            adj.append((x,y-1))
    if x+1 < n:
        if grid[x+1][y] == 1:
            adj.append((x+1,y))
    if x-1 >= 0:
        if grid[x-1][y] == 1:
            adj.append((x-1,y))
    return adj

adj = []
ends = []
for y in range(n):
    adj.append([])
    for x in range(n):
        adj[y].append(len(getAdj(y,x)))
        if(len(getAdj(y,x))) == 1:
            ends.append((y,x))

print("##initial grid\n")
for y in range(n):
    print("".join([str(x) for x in grid[y]]).replace("1","+").replace("0"," "))
print("\n\n")

tail = ends[randint(0,1)]
poss = getZeros(tail[0],tail[1])

print("tail: " + str(tail) + " link: " + str(poss))

testing = 0

while True:
    testing = poss[randint(0,len(poss)-1)]
    if adj[testing[0]][testing[1]] != 3:
        break

for pot in getAll(testing[0],testing[1]):
    adj[pot[0]][pot[1]] += 1

for pot in getAdj(testing[0],testing[1]):
    if adj[pot[0]][pot[1]] != 3:
        continue
    else:
        for padj in getAdj(pot[0],pot[1]):
            if padj != testing:
                #potential break
                seen = set([padj])
                current = 0
                for temp in getAdj(padj[0],padj[1]):
                    if temp != pot:
                        current = temp
                
                while True:
                    for temp in getAdj(current[0],current[1]):
                        if temp not in seen:
                            seen.add(temp)
                            current = temp
                        if temp == pot:
                            break
                        else:
                            #loop
                            continue


