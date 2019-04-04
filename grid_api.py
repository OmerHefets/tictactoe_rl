import random


class Grid:
    def __init__(self, edge):
        self.edge = edge
        # Make (edge * edge) dimensional grid. initialize to 0 (empty) values
        self.grid = [[0 for x in range(edge)] for y in range(edge)]

    # Print the current grid values in a 2D grid shape
    def print_grid(self):
        for row in range(len(self.grid)):
            print("|", end='\t\t')
            for column in range(len(self.grid[0])):
                print("%d" % (self.grid[row][column]), end='\t\t|\t\t')
            print("\n", end='')

    # Reset all grid values to 0
    def reset_grid(self):
        size = len(self.grid)
        self.grid = [[0 for x in range(size)] for y in range(size)]
        return grid

    def is_full(self):
        for i in range(self.edge):
            for j in range(self.edge):
                if self.grid[i][j] == 0:
                    return False
        return True

    # set the grid to specific values, for testing
    def set_grid(self, values):
        self.grid[0][0] = values[0]
        self.grid[0][1] = values[1]
        self.grid[0][2] = values[2]
        self.grid[1][0] = values[3]
        self.grid[1][1] = values[4]
        self.grid[1][2] = values[5]
        self.grid[2][0] = values[6]
        self.grid[2][1] = values[7]
        self.grid[2][2] = values[8]

    # Making changes and retrieve values from the grid
    def put_x(self, row, column):
        self.grid[row][column] = 1

    def put_o(self, row, column):
        self.grid[row][column] = -1

    def get_val(self, row, column):
        return self.grid[row][column]

    def get_grid(self):
        return self.grid

    def find_a_winner(self):
        # check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            if self.grid[1][1] == 1:
                return "x_player"
            elif self.grid[1][1] == -1:
                return "o_player"
        if self.grid[2][0] == self.grid[1][1] == self.grid[0][2]:
            if self.grid[1][1] == 1:
                return "x_player"
            elif self.grid[1][1] == -1:
                return "o_player"

        # check rows & columns
        for i in range(self.edge):
            # columns
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2]:
                if self.grid[i][0] == 1:
                    return "x_player"
                elif self.grid[i][0] == -1:
                    return "o_player"
            # rows
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                if self.grid[0][i] == 1:
                    return "x_player"
                elif self.grid[0][i] == -1:
                    return "o_player"
        return "no_winner"

    # val 0-8
    @staticmethod
    def change1d_to_2d(val, edge):
        row = int(val / edge)
        column = val % edge
        return row, column

    # change value in the grid, return false if the location is already filled, true if succeeded
    def choose_location(self, symbol, player):
        if player == "human":
            location = int(input("choose (1-9): ")) - 1
            row, column = self.change1d_to_2d(location, self.edge)
        else:
            location = random.randint(0, 9)
            row, column = self.change1d_to_2d(location, self.edge)
        if self.grid[row][column] != 0:
            return False
        if symbol == 'x':
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = -1
        return True

    def game(self, player1, player2, print_grid):
        grid.reset_grid()
        if print_grid:
            grid.print_grid()
        # turn = [True] player1, [False] player2
        turn = True
        # until the board is full:
        while not grid.is_full():
            if turn:
                player = player1
                symbol = 'x'
            else:
                player = player2
                symbol = 'o'
            while not grid.choose_location(symbol, player):
                if player == 'human':
                    print("The spot is occupied")
            winner = grid.find_a_winner()
            # change for player2
            turn = not turn
            if print_grid:
                grid.print_grid()
            if winner != 'no_winner':
                return winner
        return "draw"


grid = Grid(3)
#result = grid.game(player1='human', player2='human', print_grid=True)
#print(result)

