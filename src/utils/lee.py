from collections import deque
import time


def findStartStop(matrix):
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -2:
                positions.append((i, j))
    return positions


def read_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        matrix = []
        for line in lines:
            row = [int(num) for num in line.strip().split()]
            matrix.append(row)
        return matrix


def findExit(matrix):
    positions = []
    for i in range(len(matrix)):
        if matrix[0][i] == 0:
                positions.append((0, i))
    for i in range(len(matrix)):
        if matrix[len(matrix) - 1][i] == 0:
             positions.append((len(matrix) - 1, i))
    return positions


def lee_algorithm(maze, entry_points, exit_points):
    m = len(maze)
    n = len(maze[0])

    # Inițializare matrice de distanțe
    dist = [[float('inf') for _ in range(n)] for _ in range(m)]
    for i, j in entry_points:
        dist[i][j] = 0

    # Inițializare coadă
    queue = deque(entry_points)

    # Parcurgere labirint
    while queue:
        x, y = queue.popleft()

        # Verificare dacă am ajuns la punctul de ieșire
        if (x, y) in exit_points:
            return dist[x][y]

        # Parcurgere vecini
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            i = x + dx
            j = y + dy

            # Verificare dacă vecinul este valid și nevizitat
            if 0 <= i < m and 0 <= j < n and maze[i][j] != -1 and dist[i][j] == float('inf'):
                dist[i][j] = dist[x][y] + 1
                queue.append((i, j))

    return -1  # nu s-a găsit drum între intrări și ieșiri


def scrie_matrice_in_fisier(matrice, nume_fisier):
    with open(nume_fisier, 'w') as fisier:
        for linie in matrice:
            linie_text = ' '.join(str(element) for element in linie)  
            # Transformă elementele matricei în șiruri de caractere și le concatenează cu un spațiu între ele
            fisier.write(linie_text + '\n')  
            # Scrie linia în fișier și adaugă un caracter nou de linie


def init():
    start_time = time.time()
    filename = "src/input/lee.txt"
    matrix = read_input(filename)

    entry_points = findStartStop(matrix)
    exit_points = findExit(matrix)

    shortest_distance = lee_algorithm(matrix, entry_points, exit_points)
    
    print(entry_points)
    print(exit_points)

    with open('src/output/Lee.txt', "w",encoding="utf-8") as file:
        if shortest_distance != -1:
            print("Lungime drum: " + str(shortest_distance))
            for row in matrix:
                print("\t".join(str(x) for x in row))
            file.write("Lungime drum: " + str(shortest_distance))
            for row in matrix:
                file.write("\t".join(str(x) for x in row))
        else:
            print("Nu exista scapare din labirint!")
            file.write("Nu exista scapare din labirint!")
    end_time = time.time()
    execution_time = end_time - start_time

    with open("src/time_exec/mqueens_time_exec.txt", 'a') as file:
             file.write(str(execution_time) + '\n')
    return execution_time
        
        
