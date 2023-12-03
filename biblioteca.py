"""Sistema de Biblioteca"""
# representação em terminal por https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python



class Node:
    """Nó genérico"""
    def __init__(self, data = None, pai = None) -> None:
        self.data = data
        self.esquerda:Node = None
        self.direita:Node = None
        self.__pai = pai
        self.bf = 0

    def __le__(self, other):
        if isinstance(other, Node):
            return self.data <= other.data

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

    def __inserir_filho(self, root:Node, node): # TODO Agora só usar nos casos certos
        if node <= root:
            if not root.esquerda:
                root.esquerda = node
                root.esquerda.set_parent(root)
            else:
                self.__inserir_filho(root.esquerda, node)  # sub-árvore esquerda
        else:
            if not root.direita:  # não existe nó a direta (caso base)
                root.direita = node
                root.direita.set_parent(root)
            else:
                self.__inserir_filho(root.direita, node)  # sub-árvore direta

        # Sistema de balanceamento 
        # print(root)
        root.bf = (self.getHeightL(root.esquerda) - self.getHeightR(root.direita))
        
        # print(f'{root} -> {root.bf}')
        # if (root.data == 15):
        #     print("é " + str(self.getHeightL(root.esquerda) - self.getHeightR(root.direita)) )
        if root.bf > 1:
            if root.esquerda.bf == 1:
                self.girar_direita(root)
            elif root.esquerda.bf == -1:
                self.girar_esquerda_direita(root)

        elif root.bf < -1:
            if root.direita.bf == -1:
                self.girar_esquerda(root)
            elif root.direita.bf == 1:
                self.girar_direita_esquerda(root)
                
            
        # Update the balance factor and balance the tree
        # balanceFactor = self.getBalance(root)

        
        # if balanceFactor > 1:
        #     if node.data < root.esquerda.data:
        #         self.girar_direita(root)
        #     else:
        #         self.girar_esquerda_direita(root)

        # if balanceFactor < -1:
        #     if node.data > root.direita.data:
        #         self.girar_esquerda(root)
        #     else:
        #         self.girar_direita_esquerda(root)


        # print(self)
        
        return node


    def inserir(self, node:Node):
        """Inseri num determinado lugar dependendo da data(Idenficador)"""
        if self.raiz is None:
            self.raiz = node
        else:
            self.__inserir_filho(self.raiz, node)


    def getBF(self, root):
        return 

    def getHeightL(self, root):
        if not root:
            return 0
        return 1 + self.getHeightL(root.esquerda)


    def getHeightR(self, root):
        if not root:
            return 0
        return 1 + self.getHeightR(root.direita)


    # # Get balance factore of the node
    # def getBalance(self, root:Node): # TODO Ajeitar o sistema de pesos
    #     if not root:
    #         return 0
    #     return self.getHeightL(root.esquerda) - self.getHeightR(root.direita)


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


    # -2
    def girar_direita(self, node: Node):
        """Realiza o movimento de girar uma subarvore para direita"""
        y:Node = node.esquerda
        node_root: Node = node.get_parent()
        if node_root:
            if node_root.direita == node:
                node_root.direita = y
            else:
                node_root.esquerda = y
        else:
            self.raiz = y

        y.set_parent(node_root)
        node.set_parent(y)

        node.esquerda = y.direita
        if y.direita is not None:
            node.esquerda.set_parent(node)
        y.direita = node


        node.height = (self.getHeightL(node.esquerda) - self.getHeightR(node.direita))
        y.height = (self.getHeightL(y.esquerda) - self.getHeightR(y.direita))

        return y


    # +2
    def girar_esquerda(self, node: Node):
        """Realiza o movimento de girar uma subarvore para esquerda"""
        y:Node = node.direita
        node_root: Node = node.get_parent()
        if node_root:
            if node_root.esquerda == node:
                node_root.esquerda = y
            else:
                node_root.direita = y
        else:
            self.raiz = y

        y.set_parent(node_root)
        node.set_parent(y)

        node.direita = y.esquerda
        if y.esquerda is not None:
            node.direita.set_parent(node)
        y.esquerda = node

        node.height = (self.getHeightL(node.esquerda) - self.getHeightR(node.direita))
        y.height = (self.getHeightL(y.esquerda) - self.getHeightR(y.direita))
        return y


    def girar_direita_esquerda(self, node:Node):
        """Realiza o movimento para o -2 1 0"""

        self.girar_direita(node.direita)
        self.girar_esquerda(node)


    def girar_esquerda_direita(self, node:Node):
        """Realiza o movimento para o -2 -11 0"""
        self.girar_esquerda(node.esquerda)
        self.girar_direita(node)


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



t = ArvoreBinaria()
# t.inserir(Node(15))
# t.inserir(Node(5))
# t.inserir(Node(3))

# t.inserir(Node(16))
# t.inserir(Node(12))
# t.inserir(Node(10))




# t.inserir(Node(6))
# t.inserir(Node(7))




# t.inserir(Node(13))
# t.inserir(Node(20))
# t.inserir(Node(23))

# t.inserir(Node(65))
# t.inserir(Node(14))

for i in range(0, 40):
    t.inserir(Node(i))

print("===================")
# Quase mas cansei # TODO COlocar a formula de fazer a conta da altura certa
print(t)
