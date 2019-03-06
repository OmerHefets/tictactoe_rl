class Grid:
    def __init__(self, edge):
        self.edge = edge
        # Make (edge * edge) dimension grid. initialize to -1 (empty) values
        self.grid = [[-1 for x in range(edge)] for y in range(edge)]

    # Print the current grid values in a 2D grid shape
    def print_grid(self):
        for row in range(len(self.grid)):
            print("|", end='    ')
            for column in range(len(self.grid[0])):
                print("%d" % (self.grid[row][column]), end='\t\t|\t\t')
            print("\n", end='')

    # Reset all grid values to -1
    def reset_grid(self):
        size = len(self.grid)
        grid = [[-1 for x in range(size)] for y in range(size)]
        return grid

    # Making changes and retrieving values from the grid
    def put_x(self, row, column):
        self.grid[row-1][column-1] = 1

    def put_o(self, row, column):
        self.grid[row-1][column-1] = 0

    def get_val(self, row, column):
        return self.grid[row-1][column-1]


grid = Grid(3)
grid.put_x(2, 2)
grid.put_o(1, 1)
grid.print_grid()