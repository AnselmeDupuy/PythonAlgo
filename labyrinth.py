# Labyrinthe représenté par une matrice (0 = chemin, 1 = mur)
# Entrée en haut [0][1] et sortie en bas [9][8]
labyrinth = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]  # Exit at [9][9]
]



start = (0, 1)
paths = []
end = (9, 9)
walls = []
connectedPaths = []

connections = [(0,1),(1,0),(0,-1),(-1,0)]

for i in range(0,10):
    for j in range(0,10):
        if labyrinth[i][j] == 0:
            paths.append((i,j))
            # print((i,j))


for x, y in paths:
    for directionX, directionY in connections:
        tempX, tempY = x+directionX, y+directionY
        if (tempX, tempY) in paths:
            connectedPaths.append(((x,y), (tempX,tempY)))

for path in connectedPaths:
    print(path)

