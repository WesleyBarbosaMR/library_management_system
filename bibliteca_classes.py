from library_management_system.biblioteca import ArvoreBinaria, Node


class Usuario(Node):
    """Usuários sadsadsadsadsa"""
    def __init__(self, nome, cpf, endereco):
        super().__init__(cpf)
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco


    def __str__(self):
        return f"{self.nome} - {self.cpf}"


class Livro(Node):
    """livro"""
    def __init__(self, titulo, autor, ano_publicacao, categoria, quantidade):
        super().__init__(titulo)
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.categoria = categoria
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.ano_publicacao}"


class ArvoreLivros(ArvoreBinaria):
    """Arvore de Usuários sadsadsadsadsa"""
    def __init__(self):
        super().__init__()
        self.__tot_livros:int = None


    def __len__(self) -> int:
        if self.__tot_livros < 0:
            return -1
        return  self.__tot_livros


class ArvoreUsuarios(ArvoreBinaria):
    """Arvore de Usuários sadsadsadsadsa"""
    def __init__(self):
        super().__init__()
        self.__tot_usuarios:int = None


    def __len__(self) -> int:
        if self.__tot_usuarios < 0:
            return -1
        return  self.__tot_usuarios

usuarios: ArvoreBinaria = ArvoreUsuarios()
livros: ArvoreBinaria = ArvoreLivros()
emprestimos: list = []


# usuarios.inserir(Usuario("Carlos Douglas", 20202020, "De baixo da ponte"))
# usuarios.inserir(Usuario("joão", 200, "De baixo da ponte"))
# usuarios.inserir(Usuario("joão", 201, "De baixo da ponte"))

# print(usuarios)
# print("===================")

# livros.inserir(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "1954", ["fantasia", "aventura"], 10))
# print(livros)

# print("===================")
# print(usuarios)