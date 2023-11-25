"""Sistema de Biblioteca"""




class Node:
    """Nó genérico"""
    def __init__(self, data) -> None:
        self.data = data
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    """Arvore Binária"""
    def __init__(self):
        self.raiz = None


    def inserir(self, node):
        """Inseri num determinado lugar dependendo da data(Idenficador)"""
        if self.raiz is None:
            self.raiz = node
            return

        no = self.raiz
        while True:
            if node.data < no.data:
                if no.esquerda is None:
                    no.esquerda = node
                    break
                no = no.esquerda
            else:
                if no.direita is None:
                    no.direita = node
                    break
                no = no.direita


    def encontrar(self, identificador) -> Node | None:
        """Encontra um determinador Nó com base no seu identificador"""
        no = self.raiz
        while no is not None:
            if identificador == no.data:
                return no
            elif identificador < no.data:
                no = no.esquerda
            else:
                no = no.direita
        return None

    def __str__(self) :
        return self._ler_in_order(self.raiz)


    # reprecentaçãográfica da Arvore
    def _ler_in_order(self, node) -> str:
        representation = ""

        self.__ler_a_esquerda(node)
        print(node)
        self.__ler_a_direita(node)

        return representation


    def __ler_a_esquerda(self, node:Node):
        if not node.esquerda:
            return
        else:
            self._ler_in_order(node.esquerda)


    def __ler_a_direita(self, node):
        if not node.direita:
            return
        else:
            self._ler_in_order(node.direita)


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


usuarios.inserir(Usuario("Carlos Douglas", 20202020, "De baixo da ponte"))
usuarios.inserir(Usuario("joão", 200, "De baixo da ponte"))
usuarios.inserir(Usuario("joão", 201, "De baixo da ponte"))
print(usuarios)
print("===================")
livros.inserir(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "1954", ["fantasia", "aventura"], 10))
print(livros)


