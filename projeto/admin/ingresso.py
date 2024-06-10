ingressos = []
def listar_ingressos_vendidos():
    for ingresso in ingressos:
        print(f"Código Filme: {ingresso['codigo_filme']}, Título Filme: {ingresso['titulo_filme']}, Cliente: {ingresso['cliente']}")

def listar_ingressos_filme():
    codigo = int(input("Digite o código do filme: "))
    resultados = [i for i in ingressos if i["codigo_filme"] == codigo]
    if resultados:
        for ingresso in resultados:
            print(f"Cliente: {ingresso['cliente']}, Título Filme: {ingresso['titulo_filme']}")
    else:
        print(f"Nenhum ingresso encontrado para o filme com código {codigo}.")

def gerar_arquivo_ingressos():
    codigo = int(input("Digite o código do filme: "))
    resultados = [i for i in ingressos if i["codigo_filme"] == codigo]
    if resultados:
        nome_arquivo = f"ingressos_filme_{codigo}.txt"
        with open(nome_arquivo, 'w') as arquivo:
            for ingresso in resultados:
                arquivo.write(f"Cliente: {ingresso['cliente']}, Título Filme: {ingresso['titulo_filme']}\n")
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
    else:
        print(f"Nenhum ingresso encontrado para o filme com código {codigo}.")
