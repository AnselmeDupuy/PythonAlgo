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

connections = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(labyrinth, paths, end):
    queue = []
    visited = {end: None}
    print(queue)

    while queue:
        current = queue.pop(0)
        if current == end:
            break
        for directionX, directionY in connections:
            tempX, tempY = current[0] + directionX, current[1] + directionY
            if 0 <= tempX < 10 and 0 <= tempY < 10 and labyrinth[tempX][tempY] == 0 and (tempX, tempY) not in visited:
                queue.append((tempX, tempY))
                visited[(tempX, tempY)] = current


for i in range(0,10):
    for j in range(0,10):
        if labyrinth[i][j] == 0:
            paths.append((i,j))

for x, y in paths:
    for directionX, directionY in connections:
        tempX, tempY = x+directionX, y+directionY
        if (tempX, tempY) in paths:
            connectedPaths.append(((x,y),(tempX,tempY)))

for path in connectedPaths:
    if path in connectedPaths and (path[1], path[0]) in connectedPaths:
        connectedPaths.remove((path[1], path[0]))

# print(connectedPaths)
final = dfs(labyrinth, paths, end)
# print(final)