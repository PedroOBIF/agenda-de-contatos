agenda = []

def adicionar_contato():
    nome = input("Insira o nome do contato: ")
    telefone = input("Insira o telefone do contato: ")
    favorito = input("O contato é favorito? (s/n): ").lower() == 's'
    contato = {"nome": nome, "telefone": telefone, "favorito": favorito}
    agenda.append(contato)
    print("Contato adicionado.")

def listar_contatos():
    if not agenda:
        print("Nenhum contato cadastrado.")
    else:
        for contato in agenda:
            status_favorito = " (Favorito)" if contato["favorito"] else ""
            print(f"{contato['nome']} - {contato['telefone']}{status_favorito}")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            status_favorito = " (Favorito)" if contato["favorito"] else ""
            print(f"Contato encontrado: {contato['nome']} - {contato['telefone']}{status_favorito}")
            return
    print("Contato não encontrado.")

def atualizar_contato():
    nome = input("Digite o nome do contato que deseja atualizar: ")
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            contato["nome"] = input("Novo nome: ") or contato["nome"]
            contato["telefone"] = input("Novo telefone: ") or contato["telefone"]
            favorito = input("O contato é favorito? (s/n): ").lower()
            if favorito in ['s', 'n']:
                contato["favorito"] = favorito == 's'
            print("Contato atualizado.")
            return
    print("Contato não encontrado.")

def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ")
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            agenda.remove(contato)
            print("Contato removido.")
            return
    print("Contato não encontrado.")

def marcar_desmarcar_favorito():
    nome = input("Digite o nome do contato que deseja marcar ou desmarcar como favorito: ")
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            contato["favorito"] = not contato["favorito"]
            status = "marcado" if contato["favorito"] else "desmarcado"
            print(f"Contato {status} como favorito.")
            return
    print("Contato não encontrado.")

def listar_favoritos():
    favoritos = [contato for contato in agenda if contato["favorito"]]
    if not favoritos:
        print("Nenhum contato favorito cadastrado.")
    else:
        for contato in favoritos:
            print(f"{contato['nome']} - {contato['telefone']} (Favorito)")

def menu():
    while True:
        print("\nAGENDA DE CONTATOS")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Atualizar contato")
        print("5. Remover contato")
        print("6. Favoritar/Desfavoritar contato")
        print("7. Listar contatos favoritos")
        print("8. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '4':
            atualizar_contato()
        elif opcao == '5':
            remover_contato()
        elif opcao == '6':
            marcar_desmarcar_favorito()
        elif opcao == '7':
            listar_favoritos()
        elif opcao == '8':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

menu()

# Pedro Oliveira - 3º Informática