import time

def calculate_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Exemplu de utilizare
def my_function():
    time.sleep(2)  # Simularea unei operații care durează 2 secunde
    return "Finished"

#result, execution_time = calculate_execution_time(my_function)
#print("Rezultat:", result)
#print("Timpul de execuție:", execution_time, "secunde")
