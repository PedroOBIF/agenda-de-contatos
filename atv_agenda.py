import json

agenda = []

def carregar_agenda():
    try:
        with open('agenda.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def salvar_agenda():
    with open('agenda.json', 'w') as f:
        json.dump(agenda, f, indent=4)

def validar_telefone(telefone):
    if not telefone.isdigit() or len(telefone) < 10:
        raise ValueError("Por favor, insira um número de telefone válido (apenas números e com pelo menos 10 dígitos).")

def adicionar_contato():
    nome = input("Insira o nome do contato: ").strip()
    if not nome:
        print("O nome do contato não pode ser vazio.")
        return
    telefone = input("Insira o telefone do contato: ")
    try:
        validar_telefone(telefone)
    except ValueError as e:
        print(e)
        return

    while True:
        try:
            favorito = input("O contato é favorito? (s/n): ").lower()
            if favorito not in ['s', 'n']:
                raise ValueError("Por favor, digite apenas 's' ou 'n'.")
            favorito = favorito == 's'
            break
        except ValueError as e:
            print(e)

    contato = {"nome": nome, "telefone": telefone, "favorito": favorito}
    agenda.append(contato)
    salvar_agenda()
    print("Contato adicionado.")

def listar_contatos():
    if not agenda:
        print("Nenhum contato cadastrado.")
    else:
        for contato in agenda:
            status_favorito = " (Favorito)" if contato["favorito"] else ""
            print(f"{contato['nome']} - {contato['telefone']}{status_favorito}")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ").strip()
    if not nome:
        print("O nome não pode ser vazio.")
        return
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            status_favorito = " (Favorito)" if contato["favorito"] else ""
            print(f"Contato encontrado: {contato['nome']} - {contato['telefone']}{status_favorito}")
            return
    print("Contato não encontrado.")

def atualizar_contato():
    nome = input("Digite o nome do contato que deseja atualizar: ").strip()
    if not nome:
        print("O nome não pode ser vazio.")
        return
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            contato["nome"] = input("Novo nome: ") or contato["nome"]
            contato["telefone"] = input("Novo telefone: ") or contato["telefone"]
            
            while True:
                try:
                    favorito = input("O contato é favorito? (s/n): ").lower()
                    if favorito not in ['s', 'n']:
                        raise ValueError("Por favor, digite apenas 's' ou 'n'.")
                    contato["favorito"] = favorito == 's'
                    break
                except ValueError as e:
                    print(e)

            salvar_agenda()
            print("Contato atualizado.")
            return
    print("Contato não encontrado.")

def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ").strip()
    if not nome:
        print("O nome não pode ser vazio.")
        return
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            agenda.remove(contato)
            salvar_agenda()
            print("Contato removido.")
            return
    print("Contato não encontrado.")

def marcar_desmarcar_favorito():
    nome = input("Digite o nome do contato que deseja marcar ou desmarcar como favorito: ").strip()
    if not nome:
        print("O nome não pode ser vazio.")
        return
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            contato["favorito"] = not contato["favorito"]
            status = "marcado" if contato["favorito"] else "desmarcado"
            salvar_agenda()
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
    global agenda
    agenda = carregar_agenda()

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
        
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao < 1 or opcao > 8:
                raise ValueError("Opção inválida.")
        except ValueError as e:
            print(f"Erro: {e}")
            continue
        
        if opcao == 1:
            adicionar_contato()
        elif opcao == 2:
            listar_contatos()
        elif opcao == 3:
            buscar_contato()
        elif opcao == 4:
            atualizar_contato()
        elif opcao == 5:
            remover_contato()
        elif opcao == 6:
            marcar_desmarcar_favorito()
        elif opcao == 7:
            listar_favoritos()
        elif opcao == 8:
            print("Saindo do programa...")
            break

menu()

# Pedro Oliveira - 3º Informática