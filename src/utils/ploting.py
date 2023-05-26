import os
import matplotlib.pyplot as plt
from utils import mqueens
from utils import comis_voiajor
from utils import lee
from utils import queens_hill_climbing
from utils import queens_AG
from utils import time_exec


def ploting_AGQueens():
    with open("src/time_exec/AGQueens_time_exec.txt", "r") as file:
        lines = file.readlines()

    # Extrage x și y din linii
    x = []
    y = []
    for line in lines:
        values = line.strip().split()
        x.append(float(values[0]))
        y.append(float(values[1]))

    # Afișează datele utilizând pyplot
    plt.xlabel("Dimensiune Matrice")
    plt.ylabel("Timp executie")
    plt.title("Ploting AGQueens")
    plt.plot(x, y)
    plt.show()
    

def ploting_CV():
    with open("src/time_exec/CV_time_exec.txt", "r") as file:
        lines = file.readlines()

    # Extrage x și y din linii
    x = []
    y = []
    for line in lines:
        values = line.strip().split()
        x.append(float(values[0]))
        y.append(float(values[1]))

    # Afișează datele utilizând pyplot
    plt.xlabel("Numar orase")
    plt.ylabel("Timp executie")
    plt.title("Ploting Comis Voiajor")
    plt.plot(x, y)
    plt.show()


def ploting_mqueens():
    with open("src/time_exec/mqueens_time_exec.txt", "r") as file:
        lines = file.readlines()

    # Extrage x și y din linii
    x = []
    y = []
    for line in lines:
        values = line.strip().split()
        x.append(float(values[0]))
        y.append(float(values[1]))

    # Afișează datele utilizând pyplot
    plt.xlabel("Dimensiune matrice generata")
    plt.ylabel("Timp executie")
    plt.title("N-Regine cu Calire simulata")
    plt.plot(x, y)
    plt.show()


def ploting_QueensHillClimbing():
    with open("src/time_exec/QueensHillClimb_time_exec.txt", "r") as file:
        lines = file.readlines()

    # Extrage x și y din linii
    x = []
    y = []
    for line in lines:
        values = line.strip().split()
        x.append(float(values[0]))
        y.append(float(values[1]))

    # Afișează datele utilizând pyplot
    plt.xlabel("Dimensiune tabla")
    plt.ylabel("Timp executie")
    plt.title("Algoritm N-Regina(alpinist)")
    plt.plot(x, y)
    plt.show()


def init():
    clear = lambda: os.system('cls')

    while True:
        clear() 
        print("*** 🍴 Meniu ploating 🍴 ***\n")
        print("1. Algoritm N-Regina(alpinist)")
        print("2. Comis-Voiajor")
        print("3. N-Regine cu Calire simulata")
        print("4. N-Regine cu AG")
        print("5. Inapoi ")
        
        optiune = input("\nOPTIUNE = ")
        print()

        if(optiune == "1"):
            ploting_QueensHillClimbing()

        elif(optiune == "2"):
            ploting_CV()

        elif(optiune == "3"):
            ploting_mqueens()

        elif(optiune == "4"):
            ploting_AGQueens()

        elif(optiune == "5"):
            break

        else:
            print("OPTIUNE INVALIDA")