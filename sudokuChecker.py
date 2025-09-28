# Une grille de Sudoku valide (complétée correctement)
validGrid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

# Une grille de Sudoku invalide (avec un 5 en double dans la première ligne)
invalidGrid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 5],  # Le dernier chiffre devrait être 2, mais c'est un 5 (doublon)
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

def countChar(array):
    tempList = []
    for i in array:
        if i not in tempList:
            tempList.append(i)
        else:
            return False
    return True
    
def checkRows(array):
    for line in array:
        if not countChar(line):
            return False
    return True

def checkColumns(array):
    tempArray = []
    for i in range(0, 9):
        tempArray = []
        for j in range(0, 9):
            if array[j][i] not in tempArray:
                tempArray.append(array[j][i])
            else:
                return False
            
    return True

def checkSquare(array):
    tempList = []
    for block_i in range(0, 9, 3):
        for block_j in range(0, 9, 3):
            tempList = []
            for i in range(block_i, block_i + 3):
                for j in range(block_j, block_j + 3):
                    if array[i][j] not in tempList:
                        tempList.append(array[i][j])
                    else:
                        return False                    
    return True
        
def isValidSudokuGrid(grid):
    return checkRows(grid) and checkSquare(grid) and checkColumns(grid)

def printGrid(grid):
    for i in range(len(grid)):
        if i % 3 == 0:
            print("-" * 25)
        for j in range(len(grid[0])):
            if j % 3 == 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print("|")
    print("-" * 25)

print("\nChecking grid:")
printGrid(invalidGrid)

if isValidSudokuGrid(invalidGrid):
    print("\nThis Sudoku grid is valid")
else:
    print("\nThis Sudoku grid is invalid")