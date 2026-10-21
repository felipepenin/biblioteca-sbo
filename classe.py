class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'Livro {self.titulo} emprestado com sucesso!')
        else:
            print('Esse livro já está emprestado.')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'Livro {self.titulo} devolvido com sucesso!')
        else:
            print('Este livro já está disponivel!')