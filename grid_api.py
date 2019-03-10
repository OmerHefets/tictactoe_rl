class Grid:
    def __init__(self, edge):
        self.edge = edge
        # Make (edge * edge) dimensional grid. initialize to -1 (empty) values
        self.grid = [[-1 for x in range(edge)] for y in range(edge)]
        self.sum = -1 * (edge ** 2)

    # Print the current grid values in a 2D grid shape
    def print_grid(self):
        for row in range(len(self.grid)):
            print("|", end='\t\t')
            for column in range(len(self.grid[0])):
                print("%d" % (self.grid[row][column]), end='\t\t|\t\t')
            print("\n", end='')

    # Reset all grid values to -1
    def reset_grid(self):
        size = len(self.grid)
        self.grid = [[-1 for x in range(size)] for y in range(size)]
        return grid

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
        self.grid[row-1][column-1] = 1

    def put_o(self, row, column):
        self.grid[row-1][column-1] = 0

    def get_val(self, row, column):
        return self.grid[row-1][column-1]

    def find_a_winner(self):
        # check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            if self.grid[1][1] == 1:
                return "x_player"
            elif self.grid[1][1] == 0:
                return "o_player"
        if self.grid[2][0] == self.grid[1][1] == self.grid[0][2]:
            if self.grid[1][1] == 1:
                return "x_player"
            elif self.grid[1][1] == 0:
                return "o_player"

        # check rows & columns
        for i in range(self.edge):
            # columns
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2]:
                if self.grid[i][0] == 1:
                    return "x_player"
                elif self.grid[i][0] == 0:
                    return "o_player"
            # rows
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                if self.grid[0][i] == 1:
                    return "x_player"
                elif self.grid[0][i] == 0:
                    return "o_player"
        return "no_winner"


grid = Grid(3)
grid.put_x(2, 2)
grid.put_x(3, 3)
grid.put_x(1, 1)
grid.print_grid()
print(grid.find_a_winner())
value = [0, 1, 0, 1, 0, 1, 0, 1, 0]
grid.set_grid(value)
grid.print_grid()