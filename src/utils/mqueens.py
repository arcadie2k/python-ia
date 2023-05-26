import time
import random
import math




class Board(object):
    def __init__(self, queens):
        '''Instances differ by their queen placements.'''
        self.queens = queens.copy()  # No aliasing!
        
    def display(self):
        '''Print the board.'''
        for r in range(len(self.queens)):
            for c in range(len(self.queens)):
                if self.queens[c] == r:
                    print('Q', end=' ')
                else:
                    print('-', end=' ')
            print()
        print()
    def write_board_to_file(self, file_name):
        '''Write the board to a file.'''
        with open(file_name, 'w') as file:
            for r in range(len(self.queens)):
                for c in range(len(self.queens)):
                    if self.queens[c] == r:
                        file.write('Q ')
                    else:
                        file.write('- ')
                file.write('\n')
            file.write('\n')



    def moves(self):
        '''Return a list of possible moves given the current placements.'''
        # Generate all possible moves of queens (columns) to different rows
        # (excluding the current position of the queen in each column)
        moves = []
        for col in range(len(self.queens)):
            for row in range(len(self.queens)):
                if row != self.queens[col]:
                    moves.append((col, row))
        return moves

    def neighbor(self, move):
        '''Return a Board instance like this one but with one move made.'''
        new_board = Board(self.queens)
        col, row = move
        new_board.queens[col] = row
        return new_board

    def cost(self):
        '''Compute the cost of this solution.'''
        # Compute the number of conflicting queens (queens that are attacking each other)
        cost = 0
        for i in range(len(self.queens)):
            for j in range(i+1, len(self.queens)):
                if self.queens[i] == self.queens[j] or abs(self.queens[i] - self.queens[j]) == abs(i - j):
                    cost += 1
        return cost

class Agent (object):
    def anneal(self, board, max_moves=1000):
        '''Return a list of moves to adjust queen placements.'''
        # Set the initial temperature and cooling rate
        temperature = 1.0
        cooling_rate = 0.01

            # Set the current and best solutions to the initial state
        current = board
        best = board

        # Iterate until the maximum number of moves is reached
        for move in range(max_moves):
            # Generate a random neighbor of the current state
            neighbor = current.neighbor(random.choice(current.moves()))

            # Compute the energy (cost) difference between the current state and the neighbor
            energy_diff = neighbor.cost() - current.cost()

            # If the neighbor is a better solution, move to it
            if energy_diff < 0:
                current = neighbor

                # If the neighbor is the best solution so far, update the best solution
                if current.cost() < best.cost():
                    best = current

            # If the neighbor is a worse solution, move to it with a certain probability
            else:
                probability = math.exp(-energy_diff/temperature)
                if random.random() < probability:
                    current = neighbor

            # Cool down the temperature
            temperature *= 1 - cooling_rate

        # Return the list of moves that led to the best solution found
        moves = []
        for i in range(len(best.queens)):
            moves.append((i, best.queens[i]))
        return moves


    def main(self,n):
        '''Create a problem, solve it with simulated annealing, and console-animate.'''

        queens = dict()
        for col in range(n):
            row = random.choice(range(n))
            queens[col] = row

        board = Board(queens)
        board.display()
        board.write_board_to_file('src/output/mqueens.txt')

        agent = Agent()
        path = agent.anneal(board)

        while path:
            move = path.pop(0)
            board = board.neighbor(move)
            time.sleep(0.1)
            board.display()
            board.write_board_to_file('src/output/mqueens.txt')
def init(__name__):
    if __name__ == '__main__':
        with open("src/input/mqueens.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            element = int(line.strip())
            start_time = time.time()
            agent = Agent()
            agent.main(element)
            end_time = time.time()
            execution_time = end_time - start_time
            with open("src/time_exec/mqueens_time_exec.txt", 'a') as file:
                file.write(str(element)+" "+str(execution_time)+'\n')
            print(str(execution_time)+'\n')

