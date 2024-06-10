from admin.filme import cadastrar_filme, buscar_filme_titulo, buscar_filme_codigo, atualizar_filme, remover_filme, listar_filmes
from admin.ingresso import listar_ingressos_vendidos, listar_ingressos_filme, gerar_arquivo_ingressos
from cliente.compra import comprar_ingresso, gorjeta, listar_gorjetas, doar_gorjeta, listar_doacoes
from cliente.ingresso import listar_ingressos_cliente, gerar_arquivo_ingressos_cliente

usuarios_adm = {'leandro': '123', 'marllon': '321'}
usuarios_cliente = {'teste': 'testesenha'}

def menu_principal():
    print('\n------------------ Menu ------------------')
    print('⌬ 1 - Gerenciar Filmes')
    print('⌬ 2 - Comprar ingresso ')
    print('⌬ 3 - Cadastrar usuário')
    print('⌬ 0 - Sair do sistema')
    return int(input('Digite a opção desejada: '))

def validar_login(login, senha, usuarios):
    return usuarios.get(login) == senha

def menu_administrador():
    print('\n---- Menu do Administrador ----')
    print('1 - Cadastrar filme')
    print('2 - Buscar filme por título')
    print('3 - Buscar filme por código')
    print('4 - Atualizar filme')
    print('5 - Remover filme')
    print('6 - Listar todos os ingressos vendidos')
    print('7 - Listar ingressos vendidos para um filme')
    print('8 - Gerar arquivo TXT com ingressos vendidos para um filme')
    print('💰9 - Visualizar Saldo Gorjeta')
    print('🧸10 - Destinar Cashback para Programas Sociais ')
    print('🐱‍🏍11 - Listar Doações')
    print('🏳 0 - Logout')

    return int(input('Digite a opção desejada: '))

def cadastrar_usuario():
    print('\n--- Cadastro de Usuário ---')
    nome = input('Digite seu nome completo: ')
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    perfil = int(input('Digite 1 para cliente ou 2 para administrador: '))
    if perfil == 1:
        usuarios_cliente[login] = senha
    elif perfil == 2:
        usuarios_adm[login] = senha
    print('Cadastro realizado com sucesso!')

def main():
    while True:
        opcao = menu_principal()
        if opcao == 0:
            break
        elif opcao == 1:
            login = input('Digite seu login: ')
            senha = input('Digite sua senha: ')
            if validar_login(login, senha, usuarios_adm):
                while True:
                    opcao_adm = menu_administrador()
                    if opcao_adm == 0:
                        break
                    elif opcao_adm == 1:
                        cadastrar_filme()
                    elif opcao_adm == 2:
                        buscar_filme_titulo()
                    elif opcao_adm == 3:
                        buscar_filme_codigo()
                    elif opcao_adm == 4:
                        atualizar_filme()
                    elif opcao_adm == 5:
                        remover_filme()
                    elif opcao_adm == 6:
                        listar_ingressos_vendidos()
                    elif opcao_adm == 7:
                        listar_ingressos_filme()
                    elif opcao_adm == 8:
                        gerar_arquivo_ingressos()
                    elif opcao_adm == 9:
                        listar_gorjetas()
                    elif opcao_adm == 10:
                        doar_gorjeta()
                    elif opcao_adm == 11:
                        listar_doacoes()
                    else:
                        print("Opção inválida.")
            else:
                print('Login ou senha inválidos.')
        elif opcao == 2:
            login = input('Digite seu login: ')
            senha = input('Digite sua senha: ')
            if validar_login(login, senha, usuarios_cliente):
                while True:
                    print("\n---- Menu de Compra ----")
                    print("1 - Comprar ingresso")
                    print("2 - Listar ingressos comprados")
                    print("3 - Gerar arquivo TXT com ingressos comprados")
                    print("4 - Gorjeta")
                    print("0 - Logout")
                    opcao_compra = int(input("Digite a opção desejada: "))
                    if opcao_compra == 0:
                        break
                    elif opcao_compra == 1:
                        comprar_ingresso(login)
                    elif opcao_compra == 2:
                        listar_ingressos_cliente(login)
                    elif opcao_compra == 3:
                        gerar_arquivo_ingressos_cliente(login)
                    elif opcao_compra == 4:
                        gorjeta()
                    else:
                        print("Opção inválida.")
            else:
                print('Login ou senha inválidos.')
        elif opcao == 3:
            cadastrar_usuario()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
  