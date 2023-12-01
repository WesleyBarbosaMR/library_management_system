"""Sistema de Biblioteca"""
# representação em terminal por https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python



class Node:
    """Nó genérico"""
    def __init__(self, data = None, pai = None) -> None:
        self.data = data
        self.esquerda:Node = None
        self.direita:Node = None
        self.__pai = pai

    def display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.direita is None and self.esquerda is None:
            line = str(self.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.direita is None:
            lines, n, p, x = self.esquerda.display_aux()
            s = str(self.data)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.esquerda is None:
            lines, n, p, x = self.direita.display_aux()
            s = str(self.data)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.esquerda.display_aux()
        right, m, q, y = self.direita.display_aux()
        s = str(self.data)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    def set_parent(self, parent) -> None:
        """definir Pai do nó"""
        self.__pai = parent
    

    def get_parent(self) -> object:
        """Returna o Pai do nó"""
        return self.__pai
    
    def has_left_child(self):
        return self.esquerda is not None
    
    def has_right_child(self):
        return self.direita is not None

    
    
    def __str__(self) -> str:
        return self.data.__str__()



class ArvoreBinaria:
    """Arvore Binária"""
    def __init__(self):
        self.raiz = None


    def inserir(self, node:Node):
        """Inseri num determinado lugar dependendo da data(Idenficador)"""
        if self.raiz is None:
            self.raiz = node
            return

        no = self.raiz
        while True:
            if node.data < no.data:
                if no.esquerda is None:
                    no.esquerda = node
                    node.set_parent(no)
                    break
                no = no.esquerda
            else:
                if no.direita is None:
                    no.direita = node
                    node.set_parent(no)
                    break
                no = no.direita


    def encontrar(self, identificador) -> (bool, Node | None):
        """Encontra um determinador Nó com base no seu identificador"""
        no = self.raiz
        while no is not None:
            if identificador == no.data:
                return (True, no)
            elif identificador < no.data:
                no = no.esquerda
            else:
                no = no.direita
        return (False, None)

    def __str__(self) :
        self.__display()
        return ""


    def minimum(self, root):
        """Retorna o o menor valor de uma arvore balanceada"""
        result = root
        while result.esquerda:
            result = result.esquerda
        return result


    def successor(self, node:Node):
        """Retorna o proximo nó menor que o atual"""
        belongs, n = self.encontrar(node.data)
        if belongs:
            if n.direita:
                return self.minimum(n.direita)
            else:
                return n
        else:
            return None



    def delete(self, value): # Issue, as vezes retorna o próximo numero
        """Deletar um nó da arvore"""
        belongs, z = self.encontrar(value)
        if belongs:
            if not z.has_left_child() or not z.has_right_child():
                y: Node = z
            else:
                y = self.successor(z)

            if y.esquerda:
                x = y.esquerda
            else:
                x = y.direita

            if x:
                x.set_parent(y.get_parent())

            if not y.get_parent():
                self.raiz = x
            elif y == y.get_parent().esquerda:
                y.get_parent().esquerda = x
            else:
                y.get_parent().direita = x

            if y != z: # não entendi
                z.data = y.data

            return y


        return None


    def __display(self):
        lines, *_ = self.raiz.display_aux()
        for line in lines:
            print(line)


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

print("===================")
print(usuarios)


t = ArvoreBinaria()
t.inserir(Node(15))
t.inserir(Node(5))
t.inserir(Node(3))
t.inserir(Node(16))
t.inserir(Node(12))
t.inserir(Node(10))
t.inserir(Node(6))
t.inserir(Node(7))
t.inserir(Node(13))
t.inserir(Node(20))
t.inserir(Node(23))

print("===================")

print(t)
t.delete(12)
print(t)
