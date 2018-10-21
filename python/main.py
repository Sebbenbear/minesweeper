#python
from random import randint

# M: marked bomb
# 1-9: visible letter
# B: visible bomb
# - : blank square
# ' ': covered tile
class MineSweeper:

    def __init__(self, level):
        # height, width, mines
        self.levels = {
            "teensy": (3, 3, 1),
            "beginner": (9, 9, 10),
            "intermediate": (16, 16, 40),
            "expert": (16, 30, 99)
        }
        self.start(level)

    def insertMines(self, mines, height, width, grid):
        while mines > 0:
            x = randint(0, width-1)
            y = randint(0, height-1)
            #print(f"wd:{width} ht:{height} x:{x} y:{y}")
            if grid[x][y] != 'M': 
                grid[x][y] = 'M' 
                mines-=1
        return grid

    def printBoard(self, grid):
        for row in grid:
            print(row)

    def initialiseBoard(self, level):
        width, height, mines = self.levels[level]
        grid = [['-' for i in range(height)] for j in range(width)]
        grid = self.insertMines(mines, height, width, grid)
        return grid

    # Checks a square for a mine, returns 1 if there is a mine found, 0 if not.
    def checkForMine(self, grid, row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            if grid[row][col] == 'M':
                return 1
        return 0

    # this is the step where we gradually reveal mines
    def checkNeighbours(self, grid, row, col, visited):
        if (row, col) in visited:
            return
        visited.add((row, col))
        
        # print(f"r:{row} c:{col}")

        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            if grid[row][col] == 'M':
                return

            if grid[row][col] != '-':
                return

            count  = self.checkForMine(grid, row-1, col-1)
            count += self.checkForMine(grid, row-1, col+0)
            count += self.checkForMine(grid, row-1, col+1)
            count += self.checkForMine(grid, row+0, col-1)
            count += self.checkForMine(grid, row+0, col+0)
            count += self.checkForMine(grid, row+0, col+1)
            count += self.checkForMine(grid, row+1, col-1)
            count += self.checkForMine(grid, row+1, col+0)
            count += self.checkForMine(grid, row+1, col+1)

            grid[row][col] = str(count)
            if count > 0:
                return

            self.checkNeighbours(grid, row-1, col-1, visited)
            self.checkNeighbours(grid, row-1, col+0, visited)
            self.checkNeighbours(grid, row-1, col+1, visited)
            self.checkNeighbours(grid, row+0, col-1, visited)
            self.checkNeighbours(grid, row+0, col+0, visited)
            self.checkNeighbours(grid, row+0, col+1, visited)
            self.checkNeighbours(grid, row+1, col-1, visited)
            self.checkNeighbours(grid, row+1, col+0, visited)
            self.checkNeighbours(grid, row+1, col+1, visited)

    def revealAllMines(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'M':
                    grid[row][col] = 'E'

    def revealArea(self, grid, row, col):
        if grid[row][col] == 'M': # if it's an unrevealed mine
            grid[row][col] = 'E' # reveal it, and all the other mines
            self.revealAllMines(grid)
            return True
        else:
            if grid[row][col] == '-': # set it to be a revealed blank
                self.checkNeighbours(grid, row, col, set())
            # otherwise it's already a number
        return False

    def gridIsFull(self, grid):
        for row in grid:
            for elem in row:
                if elem == '-':
                    return False
        return True
        
    def start(self, level):
        grid = self.initialiseBoard(level)
        while True:
            row = int(input("Choose a row: "))
            col = int(input("Choose a column: "))
            # print(f"Revealing area at grid[{row}][{col}]:")
            hasLost = self.revealArea(grid, row, col)
            self.printBoard(grid)
            if hasLost:
                print('You lost!')
                return
            if self.gridIsFull(grid):
                print("You won!")
                return

    def loop(self):
        pass

    def endGame(self):
        pass

def main():
    choice = "teensy"
    ms = MineSweeper(choice)

if __name__ == "__main__":
    main()
