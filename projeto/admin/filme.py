filmes = []

def cadastrar_filme():
    titulo = input("Digite o título do filme: ")
    sala = input("Digite a sala do filme: ")
    capacidade = int(input("Digite a capacidade da sala: "))
    valor_ingresso = float(input("Digite o valor do ingresso: "))
    horario = input("Digite o horário do filme: ")
    genero = input("Digite o gênero do filme")

    filme = {
        "codigo": len(filmes) + 1,
        "titulo": titulo,
        "sala": sala,
        "capacidade": capacidade,
        "valor_ingresso": valor_ingresso,
        "horario": horario,
        "ingressos_vendidos": 0,
        "genero" : genero,
        "gorjeta" : None
    }
    filmes.append(filme)
    print(f"Filme '{titulo}' cadastrado com sucesso!")

def buscar_filme_titulo():
    termo_busca = input("Digite o termo de busca (título): ")
    filme_encontrado = None
    for filme in filmes:
        if termo_busca.lower() in filme["titulo"].lower():
            filme_encontrado = filme
            break
    if filme_encontrado:
        print(f"\n**Filme Encontrado:**")
        print(f"Código: {filme_encontrado['codigo']}")
        print(f"Título: {filme_encontrado['titulo']}")
    else:
        print(f"Filme '{termo_busca}' não encontrado.")

def buscar_filme_codigo():
    codigo_filme = int(input("Digite o código do filme: "))
    filme_encontrado = None
    for filme in filmes:
        if filme["codigo"] == codigo_filme:
            filme_encontrado = filme
            break
    if filme_encontrado:
        print(f"\n**Filme Encontrado:**")
        print(f"Código: {filme_encontrado['codigo']}")
        print(f"Título: {filme_encontrado['titulo']}")
    else:
        print(f"Filme com código {codigo_filme} não encontrado.")

def atualizar_filme():
    codigo_filme = int(input("Digite o código do filme a ser atualizado: "))
    filme_encontrado = None
    for filme in filmes:
        if filme["codigo"] == codigo_filme:
            filme_encontrado = filme
            break
    if filme_encontrado:
        print(f"\n**Filme Encontrado:**")
        print(f"Código: {filme_encontrado['codigo']}")
        print(f"Título: {filme_encontrado['titulo']}")
        # Atualize os campos desejados aqui
        filme_encontrado['titulo'] = input("Digite o novo título do filme: ")
        filme_encontrado['sala'] = input("Digite a nova sala do filme: ")
        filme_encontrado['capacidade'] = int(input("Digite a nova capacidade da sala: "))
        filme_encontrado['valor_ingresso'] = float(input("Digite o novo valor do ingresso: "))
        filme_encontrado['horario'] = input("Digite o novo horário do filme: ")
        filme_encontrado['genero'] = input("Digite o novo horário do filme: ")
        print("Filme atualizado com sucesso!")
    else:
        print(f"Filme com código {codigo_filme} não encontrado.")

def remover_filme():
    codigo_filme = int(input("Digite o código do filme a ser removido: "))
    filme_encontrado = None
    for filme in filmes:
        if filme["codigo"] == codigo_filme:
            filme_encontrado = filme
            break
    if filme_encontrado:
        filmes.remove(filme_encontrado)
        print(f"Filme com código {codigo_filme} removido com sucesso!")
    else:
        print(f"Filme com código {codigo_filme} não encontrado.")

def listar_filmes():
    if not filmes:
        print("Nenhum filme cadastrado.")
    else:
        print("\n--- Lista de Filmes ---")
        for filme in filmes:
            print(f"Código: {filme['codigo']}, Título: {filme['titulo']}, Sala: {filme['sala']}, Capacidade: {filme['capacidade']}, Valor Ingresso: {filme['valor_ingresso']}, Horário: {filme['horario']}, Ingressos Vendidos: {filme['ingressos_vendidos']}, Gênero: {filme['genero']}\n")
