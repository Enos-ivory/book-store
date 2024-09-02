lista_livro = []
id_global = 0

while True:
    print('Bem vindo a Livraria do Enos Yvori'.center(48))
    print('-' * 48)
    print('MENU PRINCIPAL'.center(48, '-'))
    print('Escolha a opção desejada')
    print('1 - Cadastrar livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover livro')
    print('4 - Sair')
    print('-' * 48)
    print('')


    def cadastrar_livro(id):
        print('-' * 48)
        print('MENU CADASTRA LIVRO'.center(48, '-'))
        print(' Id do livro', id)
        nome = input('Por favor entre com o nome do livro: ')
        autor = input('Por favor entre com o autor do livro: ')
        editora = input('Por favor entre com a editora do livro: ')
        print('-' * 48)

        livro = {
            "id": id,
            "nome": nome,
            "autor": autor,
            "editora": editora,
        }
        lista_livro.append(livro)
        global id_global
        id_global += 1


    def consulta_livro():
        while True:
            print('-' * 48)
            print('MENU CADASTRAR LIVRO'.center(48, '-'))
            print('Escolha a opção desejada')
            print('1 - Consultar todos')
            print('2 - Consultar por id')
            print('3 - Consultar por autor')
            print('4 - Retomar ao menu')
            print('-' * 48)

            opcao = int(input())
            if opcao == 1:
                for livro in lista_livro:
                    print('Id: ', livro['id'])
                    print('Nome: ', livro['nome'])
                    print('Autor: ', livro['autor'])
                    print('Editora: ', livro['editora'])
                    print('')
            elif opcao == 2:
                numero = int(input('id: '))
                for livro in lista_livro:
                    if livro['id'] == numero:
                        print('Id: ', livro['id'])
                        print('Nome: ', livro['nome'])
                        print('Autor: ', livro['autor'])
                        print('Editora: ', livro['editora'])
                        print('')
            elif opcao == 3:
                autor = input('nome do autor: ')
                for livro in lista_livro:
                    if livro['autor'] == autor:
                        print('Id: ', livro['id'])
                        print('Nome: ', livro['nome'])
                        print('Autor: ', livro['autor'])
                        print('Editora: ', livro['editora'])
                        print('')
            elif opcao == 4:
                break

            else:
                print('Opção invalida')
                continue


    def remover_livro():
        delete = int(input('id do livro: '))
        for i in range(len(lista_livro)):
            if lista_livro[i]['id'] == delete:
                lista_livro.pop(i)
                return
            else:
                remover_livro()
                break


    opcao = int(input())

    if opcao == 1:
        cadastrar_livro(id_global)
    elif opcao == 2:
        consulta_livro()
    elif opcao == 3:
        remover_livro()
    elif opcao == 4:
        exit('Encerrando programa')
        break
