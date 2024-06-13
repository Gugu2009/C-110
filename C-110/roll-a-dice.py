import random

def roll_dice():
    # Variável de resposta inicializada como "y"
    response = "y"

    while response == "y":
        # Gerando um número aleatório entre 1 e 6
        dice_value = random.randint(1, 6)
        
        # Mostrando o valor do dado
        if dice_value == 1:
            print("[-----------]")
            print("[           ]")
            print("[     O     ]")
            print("[           ]")
            print("[-----------]")
        elif dice_value == 2:
            print("[-----------]")
            print("[           ]")
            print("[   O   O   ]")
            print("[           ]")
            print("[-----------]")
        elif dice_value == 3:
            print("[-----------]")
            print("[     O     ]")
            print("[     O     ]")
            print("[     O     ]")
            print("[-----------]")
        elif dice_value == 4:
            print("[-----------]")
            print("[   O   O   ]")
            print("[           ]")
            print("[   O   O   ]")
            print("[-----------]")
        elif dice_value == 5:
            print("[-----------]")
            print("[   O   O   ]")
            print("[     O     ]")
            print("[   O   O   ]")
            print("[-----------]")
        elif dice_value == 6:
            print("[-----------]")
            print("[   O   O   ]")
            print("[   O   O   ]")
            print("[   O   O   ]")
            print("[-----------]")

        # Perguntando ao usuário se ele quer jogar o dado novamente
        response = input("Você quer jogar o dado novamente? (y/n): ").lower()

if __name__ == "__main__":
    roll_dice()