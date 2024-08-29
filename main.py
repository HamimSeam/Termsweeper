import random
from termcolor import colored

WIDTH = 8
HEIGHT = 8
NUM_BOMBS = 16

grid = [ [0 for x in range(WIDTH)] for y in range(HEIGHT) ]
visible = [ [0 for x in range(WIDTH)] for y in range(HEIGHT) ]

bombs = []
for i in range(NUM_BOMBS):
    row = random.randint(0, HEIGHT-1)
    column = random.randint(0, WIDTH-1)
    
    while (row, column) in bombs:
        row = random.randint(0, HEIGHT-1)
        column = random.randint(0, WIDTH-1)
    
    bombs.append((row, column))
        
for b in bombs:
    grid[b[0]][b[1]] = 9

def print_grid(visibility):
    colors = {
        0: "white",
        1: "cyan", 
        2: "red", 
        3: "yellow", 
        4: "magenta", 
        5: "blue", 
        6: "light_yellow", 
        7: "light_magenta", 
        8: "green", 
    }
    
    for row in range(HEIGHT):
        for column in range(WIDTH):
            if visible[row][column] == 0 and visibility == "hidden":
                print(colored("█", "dark_grey"), end=" ")
            elif visible[row][column] == 2:
                print(colored("⚑", "red"), end=" ")
            elif grid[row][column] >=9:
                print(colored("x", "dark_grey"), end=" ")
            else:
                print(colored(grid[row][column], colors[ grid[row][column] ]), end=" ")
        print("\n")

def print_visible():
    for row in visible:
        print(row)

def count_bombs():
    for b in bombs:
        if b[0] != 0:
            if b[1] != 0:
                grid[ b[0] - 1 ][ b[1] - 1] += 1
            if b[1] != WIDTH - 1:
                grid[ b[0] - 1 ][ b[1] + 1] += 1
            grid[ b[0] - 1 ][ b[1] ] += 1
        
        if b[0] != HEIGHT - 1:
            if b[1] != 0:
                grid[ b[0] + 1 ][ b[1] - 1] += 1
            if b[1] != WIDTH - 1:
                grid[ b[0] + 1 ][ b[1] + 1] += 1
            grid[ b[0] + 1 ][ b[1] ] += 1

        if b[1] != 0: grid[ b[0] ][ b[1] - 1] += 1
        if b[1] != WIDTH - 1: grid[ b[0] ][ b[1] + 1] += 1  

def update():
    print_grid("hidden")

    (mode, row, column) = input("Command: ").split()
    (row, column) = (int(row) - 1, int(column) - 1)

    if mode == "f":
        visible[row][column] = 2

    if mode == "d":
        if (row, column) in bombs:
            return row, column, "loss"
        if grid[row][column] == 0:
            flood(row, column)
        visible[ row ][ column ] = 1

    if mode == "c":
        for b in bombs:
            if visible[b[0]][b[1]] != 2:
                print("Keep going...")
                return row, column, "ongoing"
        return row, column, "win"
    
    return row, column, "ongoing"

def flood(row, column):
        if row not in range(HEIGHT) or column not in range(WIDTH):
            return
        
        if visible[row][column] == 1:
            return

        visible[row][column] = 1

        if grid[row][column] != 0:
            return

        flood(row - 1, column - 1)
        flood(row - 1, column)
        flood(row - 1, column + 1)

        flood(row, column - 1)
        flood(row, column + 1)

        flood(row + 1, column - 1)
        flood(row + 1, column)
        flood(row + 1, column + 1)

if __name__ == "__main__":
    count_bombs()
    init = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))

    while grid[init[0]][init[1]] != 0:
        init = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))

    flood(init[0], init[1])

    (row, column, hasWon) = update()

    while hasWon == "ongoing":
        (row, column, hasWon) = update()

    if hasWon == "win": print("\nYou Win!")
    if hasWon == "loss": print("\nYou Lose!")
    print_grid("visible")


