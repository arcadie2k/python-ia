import time

def read_input(file_name):
    with open(file_name, 'r') as f:
        N = int(f.readline())
        cities = []
        for i in range(N):
            city_name = f.readline().strip()
            cities.append(city_name)
        distances = []
        for i in range(N):
            distances.append(list(map(int, f.readline().split())))
        start_city = int(f.readline())
        return N, cities, distances, start_city

def nearest_neighbour(N, distances, start_city):
    start_time = time.time()
    VIZITAT = [0] * N
    DT = 0
    current_city = start_city - 1
    visited_cities = [current_city]
    VIZITAT[current_city] = 1
    while len(visited_cities) < N:
        nearest_city = None
        for i in range(N):
            if i != current_city and not VIZITAT[i]:
                if nearest_city is None or distances[current_city][i] < distances[current_city][nearest_city]:
                    nearest_city = i
        if nearest_city is None:
            break
        DT += distances[current_city][nearest_city]
        current_city = nearest_city
        visited_cities.append(current_city)
        VIZITAT[current_city] = 1
    DT += distances[current_city][start_city-1]
    end_time = time.time()
    exec_time = end_time - start_time
    return visited_cities, DT, exec_time

def init(__name__, input_file_name ,output_file_name ):
    if __name__ == '__main__':
        N, cities, distances, start_city = read_input('src/input/'+input_file_name)
        print('Number of cities:', N)
        print('City names:', cities)
        print('Distances:')
        for row in distances:
            print(row)
        print('Starting city:', start_city)
        visited_cities, DT, exec_time = nearest_neighbour(N, distances, start_city)
        print('Visited cities:', [cities[i] for i in visited_cities])
        print('Total distance:', DT)
        print('Execution time:', exec_time)
        with open("src/time_exec/CV_time_exec.txt", 'a') as file:
             file.write(str(N) + ' '+ str(exec_time)+'\n')
        with open(output_file_name, 'a') as file:
            file.write('Number of cities: ' + str(N) + '\n')
            file.write('City names: ' + str(cities) + '\n')
            file.write('Distances:\n')
            for row in distances:
                file.write(str(row) + '\n')
            file.write('Starting city: ' + str(start_city) + '\n')
            visited_cities, DT, exec_time = nearest_neighbour(N, distances, start_city)
            file.write('Visited cities: ' + str([cities[i] for i in visited_cities]) + '\n')
            file.write('Total distance: ' + str(DT) + '\n')
            file.write('Execution time: ' + str(exec_time) + '\n')