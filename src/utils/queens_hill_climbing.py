import random
import time

# Funcție pentru a genera o tablă de șah cu N regine plasate aleatoriu
def generate_board(N):
    board = []
    for _ in range(N):
        row = [0] * N
        queen_pos = random.randint(0, N-1)
        row[queen_pos] = 1
        board.append(row)
    return board

# Funcție pentru a calcula numărul total de atacuri pe o tablă de șah
def calculate_attacks(board):
    N = len(board)
    attacks = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                # Verificăm orizontal și vertical
                for k in range(N):
                    if board[i][k] == 1 and k != j:
                        attacks += 1
                    if board[k][j] == 1 and k != i:
                        attacks += 1
                # Verificăm diagonală principală
                k = 1
                while i + k < N and j + k < N:
                    if board[i + k][j + k] == 1:
                        attacks += 1
                    k += 1
                k = 1
                while i - k >= 0 and j - k >= 0:
                    if board[i - k][j - k] == 1:
                        attacks += 1
                    k += 1
                # Verificăm diagonală secundară
                k = 1
                while i - k >= 0 and j + k < N:
                    if board[i - k][j + k] == 1:
                        attacks += 1
                    k += 1
                k = 1
                while i + k < N and j - k >= 0:
                    if board[i + k][j - k] == 1:
                        attacks += 1
                    k += 1
    return attacks

# Funcție pentru a muta o regină astfel încât să minimizeze numărul de atacuri
def move_queen(board):
    N = len(board)
    best_attacks = calculate_attacks(board)
    best_board = board
    moves_available = False  # Variabilă de control pentru a indica dacă există o mișcare validă disponibilă

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                for k in range(N):
                    if k != j:
                        board[i][j] = 0
                        board[i][k] = 1
                        attacks = calculate_attacks(board)
                        if attacks < best_attacks:
                            best_attacks = attacks
                            best_board = [row[:] for row in board]  # Creăm o copie a tablei
                            moves_available = True  # Setăm variabila de control la True pentru a indica că există o mișcare validă
                        board[i][j] = 1
                        board[i][k] = 0

    if not moves_available:
        return board

    return best_board

# Funcția principală care rezolvă problema reginelor folosind strategia alpinistului
def solve_queens(N):
    board = generate_board(N)
    attacks = calculate_attacks(board)

    while attacks > 0:
        board = move_queen(board)
        attacks = calculate_attacks(board)

    return board

# Testare
def init():
    with open("src/input/queens_hill_climb.txt", "r") as file:
        lines = file.readlines()
    start_time = time.time()
    
    for line in lines:
        element = int(line.strip())
        solution = solve_queens(element)

        for row in solution:
            print(row)
            
        with open("src/output/QueensHillClimb.txt", "w") as file:
            for row in solution:
                file.write(str(row) + "\n")
        end_time = time.time()
        execution_time = end_time - start_time

        with open("src/time_exec/QueensHillClimb_time_exec.txt", "w") as file:
            file.write(str(element)+" "+str(execution_time) + "\n")
        print("Timpul de execuție:", execution_time, "secunde")
        
            


