import random

def interpret_ezop():
    code = "I@++O@-O@#"  
    queue = list(code)  
    variable = 0 

    while queue:
        command = queue.pop(0)

        if command == 'I':  
            if queue and queue[0] == '@':
                queue.pop(0)
                try:
                    variable = int(input("Zadejte hodnotu: "))
                except ValueError:
                    print("Chyba: Neplatný vstup.")
                    return
            else:
                print("Chyba: Neplatná syntaxe.")
                return

        elif command == 'G':  
            if queue and queue[0] == '@':
                queue.pop(0)
                variable = random.randint(-1024, 1024)
            else:
                print("Chyba: Neplatná syntaxe.")
                return

        elif command == 'O':  
            if queue and queue[0] == '@':
                queue.pop(0)
                print(variable)
            else:
                print("Chyba: Neplatná syntaxe.")
                return

        elif command == '+':  
            variable += 1

        elif command == '-':  
            variable -= 1

        elif command == '0':  
            variable = 0

        elif command == '#':  
            print("Skript ukončen.")
            return

        else:
            print(f"Chyba: Neznámý příkaz '{command}'.")
            return

if __name__ == "__main__":
    interpret_ezop()
