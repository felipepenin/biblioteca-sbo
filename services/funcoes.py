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
    print('6 - Sair')

    while True:
        try:
            opcao = int(input('\nDigite a opção: '))

            if opcao not in (1, 2, 3, 4, 5, 6):
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

        print(f'\n{i + 1} - Titulo: {livro.titulo}')
        print(f'\nAutor: {livro.autor}')
        print(f'Status: {status}')

def buscar():
    nome = input('Digite o titulo do livro que deseja buscar: ').strip().lower()
    encontrou = False

    for livro in livros:
        if nome == livro.titulo.lower():
            print(f'Encontrado! {livro.titulo}')
            print(f'\n{livro.autor}')
            encontrou = True
            return

    if not encontrou:
        print('Livro não encontrado!')

def emprestar():
    nome = input('Qual livro deseja emprestar? ').strip().lower()

    for livro in livros:
        if nome == livro.titulo.lower():
            livro.emprestar()
            return

    print('Livro não encontrado.')

def devolver():
    nome = input('Qual livro deseja devolver? ').strip().lower()

    for livro in livros:
        if nome == livro.titulo.lower():
            livro.devolver()
            return

    print('Livro não encontrado.')
