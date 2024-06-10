from admin.filme import filmes, listar_filmes
from admin.ingresso import ingressos

def comprar_ingresso(login_cliente):
    listar_filmes()
    troco = None
    codigo = int(input("Digite o código do filme : "))
    valor_ingresso = float(input('Digite o valor a ser pago: '))
    filme = next((f for f in filmes if f["codigo"] == codigo), None)
    if filme and filme['ingressos_vendidos'] < filme['capacidade'] and filme['capacidade'] != 0:
        filme['ingressos_vendidos'] += 1
        filme['capacidade'] -= 1
        ingresso = {
            "cliente": login_cliente,
            "codigo_filme": filme['codigo'],
            "titulo_filme": filme['titulo']
        }

        ingressos.append(ingresso)
        print(f"Ingresso para o filme '{filme['titulo']}' comprado com sucesso!")
        print(f"Capacidade atual: {filme['capacidade']}")
        if valor_ingresso > filme['valor_ingresso']:
            troco = valor_ingresso - filme['valor_ingresso']
            print(f'O seu troco foi de {troco} reais')   
        elif valor_ingresso < filme['valor_ingresso']:
            print('Valor insuficiente, vá trabalhar')   
    else:
        print(f"Não há ingressos disponíveis para o filme com código {codigo}.")

gorjetas_recebida = []
doacoes = []

def gorjeta():
    gorjeta_recebida = float(input("Digite o valor da gorjeta: "))
    gorjetas_recebida.append(gorjeta_recebida) 
    print("Gorjeta registrada com sucesso!")

def listar_gorjetas():
    if gorjetas_recebida:
        print("Gorjetas recebidas:")
        for g in gorjetas_recebida:
            print(f"- {g:.2f}")
    else:
        print("Nenhuma gorjeta recebida até o momento.")

def doar_gorjeta():
    if not gorjetas_recebida:
        print("Nenhuma gorjeta disponível para doação.")
        return
    
    print("Gorjetas disponíveis para doação:")
    for i, g in enumerate(gorjetas_recebida, start=1):
        print(f"{i} - {g:.2f}")
    
    indice = int(input("Digite o número da gorjeta que deseja doar: ")) - 1
    if 0 <= indice < len(gorjetas_recebida):
        valor_doacao = gorjetas_recebida.pop(indice)
        programa_social = input("Digite o nome do programa social: ")
        doacoes.append({"valor": valor_doacao, "programa_social": programa_social})
        print(f"Gorjeta de {valor_doacao:.2f} doada para o programa social '{programa_social}' com sucesso!")
    else:
        print("Número inválido. Nenhuma gorjeta foi doada.")

def listar_doacoes():
    if doacoes:
        print("Doações realizadas:")
        for doacao in doacoes:
            print(f"Valor: {doacao['valor']:.2f}, Programa Social: {doacao['programa_social']}")
    else:
        print("Nenhuma doação realizada ainda.")