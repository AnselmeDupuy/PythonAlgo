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

def dfs(labyrinth, start, end):
    queue = [start]
    while queue:
        current = queue[0]
        visited = {end: None}

        for x, y in paths:
            for directionX, directionY in connections:
                tempX, tempY = x+directionX, y+directionY
                if (tempX, tempY) in paths:
                    queue.append((tempX, tempY))
                    visited[(tempX, tempY)] = (x, y)
        print(queue)
        print(visited)
        queue.pop(0)
        if current == end:
            return print("path found")




    for i in range(0,10):
        for j in range(0,10):
            if labyrinth[i][j] == 0:
                paths.append((i,j))
                

finalPath = dfs(labyrinth, start, end)
print(finalPath)