<<<<<<< HEAD
# TRABALHO IESB- PROJETO SISTEMA TIA ROSA
# ALUNO: WANDERLAN ALVES
# PROFESSOR: FRANCISCO FILHO 





# Fazendo o cadarpio inicial dos produtos do sistema Tia Rosa, com descrição e preço
cardapio = [
    {"id": 1, "nome": "Café Expresso", "preco": 5.00, "descricao": "Café forte"},
    {"id": 2, "nome": "Pão de Queijo", "preco": 3.50, "descricao": "Pão de queijo mineiro"},
    {"id": 3, "nome": "Bolo de Cenoura", "preco": 7.00, "descricao": "Com cobertura de chocolate"},
    {"id": 4, "nome": "Suco de Laranja", "preco": 6.00, "descricao": "Suco natural"},
    {"id": 5, "nome": "Sanduíche Natural", "preco": 8.00, "descricao": "Com vegetais frescos"},
    {"id": 6, "nome": "Leite com Chocolate", "preco": 6.00, "descricao": "Leite quente com chocolate"},
]

# Gerando listas de clientes e pedidos de forma simples 
clientes = []
pedidos = []

# Tipo de cabecalho do sistema, uma função que exibe o menu principal
def menu_principal():
    print("Bem-vindo ao Coffee Shop Tia Rosa\n")
    print("1- Cardápio")
    print("2- Registrar Pedido")
    print("3- Registrar Cliente")
    print("4- Listar Clientes")
    print("5- Realizar Pagamento")
    print("0- Sair\n")

# Uma função criada, para exibir o cardápio com os produtos formatados 
def exibir_cardapio():
    print("\n--- Cardápio ---")
    for item in cardapio:
        print(f"{item['id']} - {item['nome']} - R$ {item['preco']:.2f} - {item['descricao']}") # Produto formatado
    print()

# Outra função criada, para registrar um cliente, pediindo informações como nome e CPF
def registrar_cliente():
    nome = input("Nome do cliente: ")
    cpf = input("CPF: ")
    cliente = {"nome": nome, "cpf": cpf}
    clientes.append(cliente)
    print(f"Cliente {nome} registrado com sucesso!")

# Mais outra função, criada para clientes cadastrados
def listar_clientes():
    print("\n--- Clientes Cadastrados ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for idx, c in enumerate(clientes, 1):
            print(f"{idx}. {c['nome']} - {c['cpf']}") # Informações do cliente formatadas
    print()


# Função criada para registrar um pedido, ligando cliente e itens do cardápio
def registrar_pedido():
    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente antes de registrar pedidos.")
        return # Retorna se não houver clientes
    listar_clientes()
    cliente_id = input("Digite o número do cliente: ")
    try:
        cliente_id = int(cliente_id) - 1
        cliente = clientes[cliente_id]
    except (ValueError, IndexError): # Evitar erros de entrada inválida
        print("Cliente inválido.")
        return # Retorna se o cliente for inválido
    exibir_cardapio()
    itens = input("Digite os IDs dos itens separados por vírgula: ").split(',')
    try:
        itens = [int(item.strip()) for item in itens] # Converte os IDs dos itens para inteiros
        itens_validos = [item for item in itens if any(prod['id'] == item for prod in cardapio)]
        if not itens_validos:
            print("Nenhum item válido selecionado.")
            return
    except ValueError:
        print("IDs inválidos.")
        return
    pedido = {'cliente': cliente, 'itens': itens_validos}
    pedidos.append(pedido) # Adiciona o pedido à lista de pedidos
    print(f"Pedido registrado com sucesso para {cliente['nome']}!")


# Função que calcula o total dos pedidos de um cliente específico e mostra o total a pagar, além de permitir o pagamento
def total_pedidos_cliente():
    if not pedidos:
        print("Nenhum pedido registrado.")
        return
    listar_clientes()
    cliente_id = input("Digite o número do cliente para ver o total dos pedidos: ")
    try: 
        cliente_id = int(cliente_id) - 1 # Convertendo o ID do cliente para inteiro
        cliente = clientes[cliente_id] # Obtém o cliente da lista
    except (ValueError, IndexError):
        print("Cliente inválido.")
        return
    total = 0
    for pedido in pedidos:
        if pedido['cliente'] == cliente:
            for item_id in pedido['itens']:
                produto = next((item for item in cardapio if item['id'] == item_id), None)
                if produto:
                    total += produto['preco']
    print(f"Total dos pedidos de {cliente['nome']}: R$ {total:.2f}") # Exibe o total a pagar


# Função que realiza o pagamento, mostrando o total a pagar e permitindo escolher a forma de pagamento
def realizar_pagamento():
    if not pedidos: # Verifica se há pedidos registrados
        print("Nenhum pedido registrado.")
        return
    listar_clientes() # Exibe a lista de clientes cadastrados
    cliente_id = input("Digite o número do cliente para realizar o pagamento: ")
    try: # Converte o ID do cliente para inteiro
        cliente_id = int(cliente_id) - 1 # Obtém o cliente da lista
        cliente = clientes[cliente_id] 
    except (ValueError, IndexError):
        print("Cliente inválido.")
        return
    total = 0
    for pedido in pedidos:
        if pedido['cliente'] == cliente: # Verifica se o pedido é do cliente selecionado
            for item_id in pedido['itens']: # Obtém os IDs dos itens do pedido
                produto = next((item for item in cardapio if item['id'] == item_id), None) # Obtém o produto do cardápio
                if produto:
                    total += produto['preco'] # Adiciona o preço do produto ao total
    if total == 0: # Verifica se o total é zero
        print(f"{cliente['nome']} não possui pedidos para pagar.") # Se não houver pedidos, informa o cliente
        return
    print(f"Total a pagar para {cliente['nome']}: R$ {total:.2f}")
    print("Formas de pagamento: 1-Crédito  2-Débito  3-Dinheiro") # Exibe as formas de pagamento disponíveis
    forma = input("Escolha a forma de pagamento: ")
    if forma == '1':
        print("Pagamento no crédito realizado com sucesso!")
    elif forma == '2':
        print("Pagamento no débito realizado com sucesso!")
    elif forma == '3':
        print("Pagamento em dinheiro realizado com sucesso!")
    else:
        print("Forma de pagamento inválida.")
        return
    print("Obrigado pela preferência. Até logo!")
    exit()

# Começo do sistema, exibe o menu principal e aguarda a escolha do usuário
while True:
    menu_principal()
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        exibir_cardapio()
    elif opcao == '2':
        registrar_pedido()
    elif opcao == '3':
        registrar_cliente()
    elif opcao == '4':
        listar_clientes()
    elif opcao == '5':
        realizar_pagamento()  
    elif opcao == '0':
        print("Operação finalizada. Até logo!")
        break
    else:
=======
# TRABALHO IESB 
# ALUNO: WANDERLAN ALVES
# PROFESSOR: FRANCISCO FILHO 
# 




# Fazendo o cadarpio inicial dos produtos do sistema Tia Rosa, com descrição e preço
cardapio = [
    {"id": 1, "nome": "Café Expresso", "preco": 5.00, "descricao": "Café forte"},
    {"id": 2, "nome": "Pão de Queijo", "preco": 3.50, "descricao": "Pão de queijo mineiro"},
    {"id": 3, "nome": "Bolo de Cenoura", "preco": 7.00, "descricao": "Com cobertura de chocolate"},
    {"id": 4, "nome": "Suco de Laranja", "preco": 6.00, "descricao": "Suco natural"},
    {"id": 5, "nome": "Sanduíche Natural", "preco": 8.00, "descricao": "Com vegetais frescos"},
    {"id": 6, "nome": "Leite com Chocolate", "preco": 6.00, "descricao": "Leite quente com chocolate"},
]

# Gerando listas de clientes e pedidos de forma simples 
clientes = []
pedidos = []

# Tipo de cabecalho do sistema, uma função que exibe o menu principal
def menu_principal():
    print("Bem-vindo ao Coffee Shop Tia Rosa\n")
    print("1- Cardápio")
    print("2- Registrar Pedido")
    print("3- Registrar Cliente")
    print("4- Listar Clientes")
    print("5- Realizar Pagamento")
    print("0- Sair\n")

# Uma função criada, para exibir o cardápio com os produtos formatados 
def exibir_cardapio():
    print("\n--- Cardápio ---")
    for item in cardapio:
        print(f"{item['id']} - {item['nome']} - R$ {item['preco']:.2f} - {item['descricao']}") # Produto formatado
    print()

# Outra função criada, para registrar um cliente, pediindo informações como nome e CPF
def registrar_cliente():
    nome = input("Nome do cliente: ")
    cpf = input("CPF: ")
    cliente = {"nome": nome, "cpf": cpf}
    clientes.append(cliente)
    print(f"Cliente {nome} registrado com sucesso!")

# Mais outra função, criada para clientes cadastrados
def listar_clientes():
    print("\n--- Clientes Cadastrados ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for idx, c in enumerate(clientes, 1):
            print(f"{idx}. {c['nome']} - {c['cpf']}") # Informações do cliente formatadas
    print()


# Função criada para registrar um pedido, ligando cliente e itens do cardápio
def registrar_pedido():
    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente antes de registrar pedidos.")
        return # Retorna se não houver clientes
    listar_clientes()
    cliente_id = input("Digite o número do cliente: ")
    try:
        cliente_id = int(cliente_id) - 1
        cliente = clientes[cliente_id]
    except (ValueError, IndexError): # Evitar erros de entrada inválida
        print("Cliente inválido.")
        return # Retorna se o cliente for inválido
    exibir_cardapio()
    itens = input("Digite os IDs dos itens separados por vírgula: ").split(',')
    try:
        itens = [int(item.strip()) for item in itens] # Converte os IDs dos itens para inteiros
        itens_validos = [item for item in itens if any(prod['id'] == item for prod in cardapio)]
        if not itens_validos:
            print("Nenhum item válido selecionado.")
            return
    except ValueError:
        print("IDs inválidos.")
        return
    pedido = {'cliente': cliente, 'itens': itens_validos}
    pedidos.append(pedido) # Adiciona o pedido à lista de pedidos
    print(f"Pedido registrado com sucesso para {cliente['nome']}!")


# Função que calcula o total dos pedidos de um cliente específico e mostra o total a pagar, além de permitir o pagamento
def total_pedidos_cliente():
    if not pedidos:
        print("Nenhum pedido registrado.")
        return
    listar_clientes()
    cliente_id = input("Digite o número do cliente para ver o total dos pedidos: ")
    try: 
        cliente_id = int(cliente_id) - 1 # Convertendo o ID do cliente para inteiro
        cliente = clientes[cliente_id] # Obtém o cliente da lista
    except (ValueError, IndexError):
        print("Cliente inválido.")
        return
    total = 0
    for pedido in pedidos:
        if pedido['cliente'] == cliente:
            for item_id in pedido['itens']:
                produto = next((item for item in cardapio if item['id'] == item_id), None)
                if produto:
                    total += produto['preco']
    print(f"Total dos pedidos de {cliente['nome']}: R$ {total:.2f}") # Exibe o total a pagar


# Função que realiza o pagamento, mostrando o total a pagar e permitindo escolher a forma de pagamento
def realizar_pagamento():
    if not pedidos: # Verifica se há pedidos registrados
        print("Nenhum pedido registrado.")
        return
    listar_clientes() # Exibe a lista de clientes cadastrados
    cliente_id = input("Digite o número do cliente para realizar o pagamento: ")
    try: # Converte o ID do cliente para inteiro
        cliente_id = int(cliente_id) - 1 # Obtém o cliente da lista
        cliente = clientes[cliente_id] 
    except (ValueError, IndexError):
        print("Cliente inválido.")
        return
    total = 0
    for pedido in pedidos:
        if pedido['cliente'] == cliente: # Verifica se o pedido é do cliente selecionado
            for item_id in pedido['itens']: # Obtém os IDs dos itens do pedido
                produto = next((item for item in cardapio if item['id'] == item_id), None) # Obtém o produto do cardápio
                if produto:
                    total += produto['preco'] # Adiciona o preço do produto ao total
    if total == 0: # Verifica se o total é zero
        print(f"{cliente['nome']} não possui pedidos para pagar.") # Se não houver pedidos, informa o cliente
        return
    print(f"Total a pagar para {cliente['nome']}: R$ {total:.2f}")
    print("Formas de pagamento: 1-Crédito  2-Débito  3-Dinheiro") # Exibe as formas de pagamento disponíveis
    forma = input("Escolha a forma de pagamento: ")
    if forma == '1':
        print("Pagamento no crédito realizado com sucesso!")
    elif forma == '2':
        print("Pagamento no débito realizado com sucesso!")
    elif forma == '3':
        print("Pagamento em dinheiro realizado com sucesso!")
    else:
        print("Forma de pagamento inválida.")
        return
    print("Obrigado pela preferência. Até logo!")
    exit()

# Começo do sistema, exibe o menu principal e aguarda a escolha do usuário
while True:
    menu_principal()
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        exibir_cardapio()
    elif opcao == '2':
        registrar_pedido()
    elif opcao == '3':
        registrar_cliente()
    elif opcao == '4':
        listar_clientes()
    elif opcao == '5':
        realizar_pagamento()  
    elif opcao == '0':
        print("Operação finalizada. Até logo!")
        break
    else:
>>>>>>> 0541926fc35d8ee88bada18498dc42157c223fc9
        print("Opção inválida. Tente novamente.")