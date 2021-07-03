último = 10
último2 = 10
fila = list(range(1, último + 1))
fila2 = list(range(1, último2 + 1))
while True:
    print('-' *50)
    print(f"\n \033[1;35m Existem {len(fila)} clientes na fila 1 \033[m")
    print(f"Fila 1 atual: {fila}")
    print(f"\n \033[1;35m Existem {len(fila2)} clientes na fila 2 \033[m")
    print(f"Fila 2 atual: {fila2}")
    #Menu
    print("\nDigite \033[1;34m A \033[m para realizar o atendimento da \033[1;34m fila 1 \033[m ou \033[1;34m B \033[m para realizar o atendimento da \033[1;34m fila 2.\033[m")
    print("Digite \033[1;34m F \033[m para adicionar um cliente ao fim da \033[1;34m fila 1 \033[m ou \033[1;34m G \033[m para adicioná-lo ao fim da \033[1;34m fila 2. \033[m")
    print("Digite S caso queira sair.")

    operação = input("Operação (A, B ; F, G ou S): ")
    if operação == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} da fila 1 atendido")
        else:
            print("Fila vazia! Não há Ninguém para atender!")
    elif operação == "B":
        if len(fila2) > 0:
            atendido = fila2.pop(0)
            print(f"Cliente {atendido} da fila 2 atendido")
        else:
            print("Fila vazia! Não há ninguém para atender!")   

    elif operação == "F":
        último += 1  
        fila.append(último)
    elif operação == "G":
        último2 += 1
        fila2.append(último2)
    elif operação == "S":
        break
    else:
        print("Operação inválida! Digite apenas A, B ; F, G ou S!")
