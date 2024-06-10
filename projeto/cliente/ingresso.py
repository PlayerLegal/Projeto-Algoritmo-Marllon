from admin.ingresso import ingressos
ingressos_vendidos = []
def listar_ingressos_cliente(login_cliente):
    resultados = [i for i in ingressos if i["cliente"] == login_cliente]
    if resultados:
        for ingresso in resultados:
            print(f"Filme: {ingresso['titulo_filme']}")
    else:
        print(f"Você não comprou nenhum ingresso ainda.")


def gerar_arquivo_ingressos_cliente(login_cliente):
    resultados = [i for i in ingressos if i["cliente"] == login_cliente]
    if resultados:
        nome_arquivo = f"ingressos_cliente_{login_cliente}.txt"
        with open(nome_arquivo, 'w') as arquivo:
            for ingresso in resultados:
                arquivo.write(f"Filme: {ingresso['titulo_filme']}\n")
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
    else:
        print(f"Você não comprou nenhum ingresso ainda.")
