import random

# Rotates a 2D list clockwise
def rotate(grid):
    return list(map(list, zip(*grid[::-1])))

# Implements game logic 
# Generalized for all four directions using rotation logic
def pickNewValue():
    if random.randint(1,8)==1:
        return 4
    else:
        return 2    

def move(grid, dir):
    for i in range(dir): grid = rotate(grid)
    for i in range(len(grid)):
        temp = []
        for j in grid[i]:
            if j != '.':
                temp.append(j)
        temp += ['.'] * grid[i].count('.') 
        for j in range(len(temp) - 1):
            if temp[j] == temp[j + 1] and temp[j] != '.' and temp[j + 1] != '.':
                temp[j] = str(2 * int(temp[j]))
                move.score += int(temp[j])
                temp[j + 1] = '.'
        grid[i] = []
        for j in temp:
            if j != '.':
                grid[i].append(j)
        grid[i] += ['.'] * temp.count('.')
    for i in range(4 - dir): grid = rotate(grid)
    return grid

# Finds empty slot in the game grid
def findEmptySlot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i, j, 0)
    return (-1, -1, 1)

# Adds a random number to the grid
def addNumber(grid):
    num = random.randint(1, 2) * 2
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    lost = 0
    if grid[x][y] != '.':
        x, y, lost = findEmptySlot(grid)
    if not lost: grid[x][y] = str(num)
    return (grid, lost)

# Prints the current game state
def printGrid(grid):
    print ("\n")
    for i in range(len(grid)):
        res = "\t\t"
        for j in range(len(grid[i])):
            for _ in range(5 - len(grid[i][j])): res += " "
            res += (grid[i][j]) + " "
        print (res)
        print ("\n")
    return 0

# Starts the game
def startGame():
    print (" \n Welcome to the 2048 Console world. Let's play!")
    print ("Combine given numbers to get a maximum score. \n  You can move numbers to left, right, top or bottom direction.\n")
    
    # Create the game grid x
    # The game should work for square grid of any size though
    grid = [['.', '.', '2', '.'],
            ['.', '.', '.', '.'],
            ['.', '4', '.', '.'],
            ['.', '.', '.', '.']]
    # grid=[]
    # for i in range(4):
    #     row=[]
    #     for i in range(4):
    #         row.append(".")
    #     grid.append(row)    

    # numNeeded=2
    # while numNeeded>0:
    #     rowNum=random.randint(0,3)
    #     colNum=random.randint(0,3)
    #     if grid[rowNum][colNum]==".":
    #        grid[rowNum][colNum]={pickNewValue()}
    #        numNeeded-=1
    direction = {'1': 0, '4': 1, '2': 2, '3': 3, 'X': 4}

    printGrid(grid)
    loseStatus = 0
    move.score = 0 # Score of the user
    while True:
        tmp = input("\n To continue, Press 1 for left, 2 for right, 3 for top, 4 for bottom or\nPress X to end the game.\n")
        if tmp in ["2", "1", "3", "4", "X", ]:
            dir = direction[tmp]
            if dir == 4:
                print ("\nFinal score: " + str(move.score))
                break
            else:
                grid = move(grid, dir)
                grid, loseStatus = addNumber(grid)
                printGrid(grid)
                if loseStatus:
                    print ("\n Game Over")
                    print ("Final score: " + str(move.score))
                    break
                print ("\n Current score: " + str(move.score))
        else:
            print ("\n Invalid direction, please provide valid movement direction (1, 2, 3, 4).")
    return 0

# Program starts here
startGame()