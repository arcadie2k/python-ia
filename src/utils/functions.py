from utils import mqueens
from utils import comis_voiajor
from utils import lee
from utils import queens_hill_climbing
from utils import queens_AG
from utils import time_exec
from utils import functions
from utils import ploting


def option_lee():
    print("Algoritmul lui Lee")
    execution_time = lee.init()
    print("Timpul de execuție:", execution_time, "secunde")


def option_N_Regine_Alpinist():
    print("N Regine (Alpinist)")
    queens_hill_climbing.init()


def option_Comis_Voiajor():
    print("Comis_Voiajor")
    comis_voiajor.init("__main__", "cv1.txt","src/output/CV.txt")
    comis_voiajor.init("__main__", "cv2.txt","src/output/CV.txt")
    comis_voiajor.init("__main__", "cv3.txt","src/output/CV.txt")

def option_N_Regine_Calire_Simulata():
    print("N_Regine_Calire_Simulata")
    mqueens.init("__main__")
   

def option_N_Regine_AG():
    print("N_Regine_AG")
    queens_AG.init()

def option_grafic():
   print("MOD GRAFIC")
   ploting.init()

def option_Info_Autor():
   print("FIESC - Calculatoare")
   print("Caldare Arcadie")
   print("Grupa: 3131A") 