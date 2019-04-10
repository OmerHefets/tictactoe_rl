import random
import agent_api as ag


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

    # return grid value and not a reference
    def get_grid(self):
        returned_grid = []
        for arr in range(len(self.grid)):
            temp = self.grid[arr][:]
            returned_grid.append(temp)
        return returned_grid

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
    def choose_location(self, symbol, player, agent):
        if player == "human":
            location = (int(input("choose (1-9): ")) - 1)
            row, column = self.change1d_to_2d(location, self.edge)
        elif player == "computer":
            location = (random.randint(1, 9) - 1)
            row, column = self.change1d_to_2d(location, self.edge)
            print("###")
        elif player == "AI":
            location = agent.agent_location(grid)
            row, column = self.change1d_to_2d(location, self.edge)
            print(agent.grid_current_vals)
            print("@@@")
        else:
            print("no such player!")
            location = (random.randint(1, 9) - 1)
            return False, location
        if self.grid[row][column] != 0:
            return False, location
        if symbol == 'x':
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = -1
        return True, location

    def game(self, player1, player2, defined_agent, print_grid, alpha):
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
            print(defined_agent.current_grid)
            valid_location, location = grid.choose_location(symbol, player, agent=defined_agent)
            print(defined_agent.current_grid)
            while not valid_location:
                if player == 'human':
                    print("The spot is occupied")
                if player == 'computer':
                    print("Choosing Again")
                if player == 'AI':
                    defined_agent.full_square_backpropagation(location, grid, alpha)
                valid_location, location = grid.choose_location(symbol, player, agent=defined_agent)
            winner = grid.find_a_winner()
            # change for player2
            turn = not turn
            if print_grid:
                grid.print_grid()
            if winner != 'no_winner':
                defined_agent.win_or_lose_backpropagation(location, grid, alpha)
                return winner
            # Q-Learning implementation if the player is the AI
            #if player == 'AI':

        return "draw"

    #def training(self, iterations, defined_agent):



grid = Grid(3)
niro = ag.Agent()
result = grid.game(player1='human', player2='AI', defined_agent=niro, print_grid=True, alpha=0.01)
print(result)
