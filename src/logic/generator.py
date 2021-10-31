from random import randint, shuffle

from src.logic.utils import ConfigManager, SerializableDict
from src.logic.board import Board


class Generator:
    def __init__(self) -> None:
        self.config = SerializableDict(**ConfigManager.load_config())
        self.board = Board()

        self.number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def generate(self):
        self.board.create_board()

        self.fill_grid(self.board.grid)
        self.board.display()

    def check_grid(self, grid):
        """
        Check if any of the elements from the grid is 0.
        """

        for row in range(self.config.board_size):
            for col in range(self.config.board_size):
                if grid[row][col] == 0:
                    return False

        return True

    def fill_grid(self, grid):
        # Find next empty cell
        for i in range(self.config.board_size ** 2):
            row = i // self.config.board_size
            col = i % self.config.board_size

            if grid[row][col] == 0:
                shuffle(self.number_list)
                for value in self.number_list:
                    # Check that this value has not already be used on this row
                    if not (value in grid[row]):
                        # Check that this value has not already be used on this column
                        if value not in (
                                grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col],
                                grid[5][col], grid[6][col], grid[7][col], grid[8][col]):
                            # Identify which of the 9 squares we are working on
                            if row < 3:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(0, 3)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(0, 3)]
                                else:
                                    square = [grid[i][6:9] for i in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(3, 6)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(3, 6)]
                                else:
                                    square = [grid[i][6:9] for i in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(6, 9)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(6, 9)]
                                else:
                                    square = [grid[i][6:9] for i in range(6, 9)]
                            # Check that this value has not already be used on this 3x3 square
                            if value not in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                if self.check_grid(grid):
                                    return True
                                else:
                                    if self.fill_grid(grid):
                                        return True
                break
        grid[row][col] = 0

# #Start Removing Numbers one by one

# #A higher number of attempts will end up removing more numbers from the grid
# #Potentially resulting in more difficiult grids to solve!
# attempts = 5 
# counter=1
# while attempts>0:
#   #Select a random cell that is not already empty
#   row = randint(0,8)
#   col = randint(0,8)
#   while grid[row][col]==0:
#     row = randint(0,8)
#     col = randint(0,8)
#   #Remember its cell value in case we need to put it back  
#   backup = grid[row][col]
#   grid[row][col]=0

#   #Take a full copy of the grid
#   copyGrid = []
#   for r in range(0,9):
#      copyGrid.append([])
#      for c in range(0,9):
#         copyGrid[r].append(grid[r][c])
