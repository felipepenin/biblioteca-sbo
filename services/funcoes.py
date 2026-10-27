from models.classe import Livro

livros = []

def menu():
    print('\n=====================')
    print('  BIBLIOTECA DE SBO  ')
    print('=====================')
    print('\n1 - Cadastrar Livro')
    print('2 - Listar Livros')
    print('3 - Buscar Livro')
    print('4 - Emprestar Livro')
    print('5 - Devolver Livro')
    print('6 - Disponiveis')
    print('7 - Sair')

    while True:
        try:
            opcao = int(input('\nDigite a opção: '))

            if opcao not in (1, 2, 3, 4, 5, 6, 7):
                print('ERRO: Digite uma opção válida.')
                continue
            break

        except ValueError:
            print('ERRO: Digite uma opção válida!')

    return opcao
        
def cadastrar():
    while True:
        titulo = input('\nTítulo do Livro: ').strip()

        if not titulo:
            print('O título não pode ficar vazio')
            continue

        encontrou = False

        for livro in livros:
            if livro.titulo.lower() == titulo.lower():
                encontrou = True
                print('Este livro já está cadastrado!')
                break

        if encontrou:
            continue

        autor = input('Autor do Livro: ').strip()

        if not autor:
            print('O autor não pode ficar vazio.')
            continue

        livro = Livro(titulo, autor)
        livros.append(livro)
        return

def listar():
    print('=====================')
    print('  BIBLIOTECA DE SBO  ')
    print('=====================')

    if not livros:
        print('\nNenhum livro cadastrado.')
        return

    for i, livro in enumerate(livros, start=1):
        status = 'Disponivel' if livro.disponivel else 'Emprestado'

        print(f'\n{i} - Titulo: {livro.titulo}')
        print(f'Autor: {livro.autor}')
        print(f'Status: {status}')

def buscar():
    nome = input('\nDigite o titulo do livro que deseja buscar: ').strip().lower()
    encontrou = False

    for livro in livros:
        status = 'Disponivel' if livro.disponivel else 'Emprestado'
        
        if nome == livro.titulo.lower():
            print('\nEncontrado!')
            print(f'\nTítulo: {livro.titulo}')
            print(f'Autor: {livro.autor}')
            print(f'Status: {status}')
            encontrou = True
            return

    if not encontrou:
        print('Livro não encontrado!')

def emprestar():
    nome = input('\nQual livro deseja emprestar? ').strip().lower()

    for livro in livros:
        if nome == livro.titulo.lower():
            livro.emprestar()
            return

    print('\nLivro não encontrado.')

def devolver():
    nome = input('\nQual livro deseja devolver? ').strip().lower()

    for livro in livros:
        if nome == livro.titulo.lower():
            livro.devolver()
            return

    print('\nLivro não encontrado.')

def cont_disponiveis():
    disponivel = 0
    emprestado = 0

    for livro in livros:
        if livro.disponivel:
            disponivel += 1
        else:
            emprestado += 1

    print(f'\nExistem {disponivel} livros disponíveis na biblioteca.')
    print(f'Existem {emprestado} livros emprestados na biblioteca.')