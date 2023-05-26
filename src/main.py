import utils
import os

clear = lambda: os.system('cls')

def waitForUser():
    input("\n*** 🔤 Apasati ENTER pentru a continua 🔤 ***")

while True: 
    clear()
    print("*** ✨ MENIU ✨ ***\n")
    print("1. Algoritm Lee")
    print("2. Algoritm N-Regina (Algoritmul Alpinistului)")
    print("3. Problema Comis-Voiajorului")
    print("4. N-Regine cu Calire Simulata")
    print("5. N-Regine cu AG")
    print("6. Grafic variatie timp algoritmi")
    print("7. Info Autor")
    print("8. Iesire")

    optiune = input("\nOPTIUNE = ")
    print()

    if(optiune == "1"):
        utils.functions.option_lee()

    elif(optiune == "2"):
        utils.functions.option_N_Regine_Alpinist()

    elif(optiune == "3"):
        utils.functions.option_Comis_Voiajor()

    elif(optiune == "4"):
        utils.functions.option_N_Regine_Calire_Simulata()

    elif(optiune == "5"):
        utils.functions.option_N_Regine_AG()

    elif(optiune == "6"):
        utils.functions.option_grafic()

    elif(optiune == "7"):
        utils.functions.option_Info_Autor()

    elif(optiune == "8"):
        print("*** Iesire program ***")
        break
    else:
        print("OPTIUNE INVALIDA")
    
    waitForUser()