#Criação de um lista simples
agenda = []

#Função que pede o nome do usuário
def pede_nome():
    return input("Nome: ")

#Função que pede o telefone do usuário
def pede_telefone():
    return input("Telefone: ")

#Função que mostra o nome e telefone do usuário
def mostra_dados(nome, telefone):
    print(f"Nome: {nome} Telefone: {telefone}")

#Função que pede o nome do arquivo
def pede_nome_arquivo():
    return input("Nome do arquivo: ")

#Função que pega o nome
def pesquisa(nome):
    mnome = nome.lower() #Armazena o nome em minúsculo na variável mnome
    for p, e in enumerate(agenda): #Busca os dados da agenda
        if e[0].lower() == mnome: #Se a string na primeira posição da variável 'e' minúscula for igual ao nome em minúsculo
            return p #Retorna o valor de p
    return None #Retorna nada

#Função novo
def novo():
    global agenda #Variável global agenda que será modificada nesse escopo  
    nome = pede_nome() #Variável nome que recebe a função pede_nome()
    telefone = pede_telefone() #Variável telefone que recebe a função pede_telefone()
    agenda.append([nome, telefone]) #Adiciona os elementos nome e telefone na lista agenda

#Função apaga
def apaga():
    global agenda #Variável global agenda que será modificada nesse escopo
    nome = pede_nome() #Variável nome que recebe a função pede_nome()
    p = pesquisa(nome) #Consulta na função pesquisa(nome) o nome digitado
    if p is not None: #Se o nome for encontrado na função de pesquisa
        del agenda[p] #Ele deletará da agenda o nome e telefone dessa pessoa
    else: #Caso ao contrário
        print("Nome não encontrado.") #Exibição de uma mensagem: Nome não encontrado.

#Função de alteração
def altera():
    p = pesquisa(pede_nome()) #Pede o nome do usuário e logo após pesquisa se ele existe na agenda
    if p is not None:  #Se o nome for encontrado na função de pesquisa
        nome = agenda[p][0] #Armazena na variável nome, o nome do usuário (coluna [0]) que foi encontrado na linha [p]
        telefone = agenda[p][1]  #Armazena na variável telefone, o telefone do usuário (coluna [1]) que foi encontrado na linha [p]
        print("Encontrado:") #Exibição da mensagem: Encontrado: 
        mostra_dados(nome, telefone) #Exibe o nome o telefone que foram encontrados
        nome = pede_nome() #Armazena na variável nome, a atualização do nome
        telefone = pede_telefone() #Armazena na variável telefone, a atualização do telefone
        agenda[p] = [nome, telefone] #Armazena na linha [p] da agenda os novos valores de nome e telefone
    else: #Caso ao contrário
        print("Nome não encontrado.") #Exibição da mensagem: Nome não encontrado.

#Função lista
def lista():
    print("\nAgenda\n\n------") #Apresentação visual de Agenda 
    for e in agenda: #Criação de um laço de repetição que armazena em e o tamanho da variável agenda
        mostra_dados(e[0], e[1]) #Imprime os dados da agenda (nome e telefone)
    print("------\n") #Imprime uma linha de separação

#Função le
def le():
    global agenda #Variável global agenda que será modificada nesse escopo
    nome_arquivo = pede_nome_arquivo() #armazena na variável nome_arquivo o nome do arquivo inserido
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo: #Abre o arquivo de acordo com o nome solicitado
        agenda = [] #lista
        for l in arquivo.readlines(): #Método que retorna uma lista contendo cada linha do arquivo
            nome, telefone = l.strip().split("#") #Strip remove os espaços inúteis do início e fim
            #Split divide essa string em uma lista
            agenda.append([nome, telefone]) #Adiciona os elementos nome e telefone na lista agenda
        arquivo.close() #Foi adicionado para evitar possíveis conflitos

#Função grava
def grava():
    nome_arquivo = pede_nome_arquivo() #Variável nome_arquivo recebe o nome do arquivo
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo: #Abre o arquivo de acordo com o nome solicitado
        for e in agenda: #Criação de um laço de repetição que armazena em e o tamanho da variável agenda
            arquivo.write(f"{e[0]}#{e[1]}\n") #Salva na lista o nome e telefone, separando por #
        arquivo.close() #Foi adicionado para evitar possíveis conflitos

#Função para validar faixa de inteiros
def valida_faixa_inteiro(pergunta, início, fim):
    while True: #Enquanto isso for verdadeiro
        try: #Tente o escopo abaixo
            valor = int(input(pergunta)) #Valor recebe a decisão do usuário, ou seja, o que foi digitado
            if início <= valor <= fim:   #Se o valor for maior ou igual ao valor de início [0] e menor ou igual ao valor final [6] 
                return valor    #Retorna o valor
        except ValueError: #Se não der certo
            print(f"Valor inválido, favor digitar entre {início} e {fim}") #Printa a mensagem

#Função menu
def menu():
    #Imprime na tela o que está entre as aspas triplas
    print("""
  1 - Novo
  2 - Altera
  3 - Apaga
  4 - Lista
  5 - Grava
  6 - Lê

  0 - Sai
""")
    #Vai retornar a função valida_faixa_inteiro com a opção que o usuário escolher
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)

#Enquanto isso for verdadeiro, vai repetir o que está dentro do escopo
while True:
    opcao = menu()
    if opcao == 0:   #Se a opção for 0, ele vai sair
        break
    elif opcao == 1: #Se a opção for 1, ele vai chamar a função novo()
        novo()
    elif opcao == 2: #Se a opção for 2, ele vai chamar a função altera()
        altera()
    elif opcao == 3: #Se a opção for 3, ele vai chamar a função apaga()
        apaga()
    elif opcao == 4: #Se a opção for 4, ele vai chamar a função lista()
        lista()
    elif opcao == 5: #Se a opção for 5, ele vai chamar a função grava()
        grava()      
    elif opcao == 6: #Se a opção for 6, ele vai chamar a função le()
        le()
