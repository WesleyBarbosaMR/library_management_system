# Importação da biblioteca Pickle para manter a persistência dos dados sem precisar de BD.
import pickle

''' # ? Para tornar as verificações de tipo mais robustas,
    # ? a fim de garantir a correta inserção de dados.

    # * Importe a biblioteca typing
    from typing import Dict, Union

    # * Modifique o trecho de inicialização da Biblioteca (construtor def __init__) p/
    ```
        def __init__(self):
            self.livros: Dict[str, Livro] = {}
            self.usuarios: Dict[int, Usuario] = {}
    ```
'''

# * Declaração da classe Livro com seus atributos.
# TODO Lembrar de adicionar mais atributos ao Livro (ISBN ou ISSN principalmente)
# TODO Adicionar registro de quantidade, p/ evitar duplicidade de dados.
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = True

# * Declaração da classe Usuário com seus atributos.
# TODO Lembrar de adicionar mais atributos ao Usuário (Matrícula e/ou CPF e Email principalmente)
class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.livros_emprestados = set()

# * Declaração da classe Biblioteca com seus componentes(Livros e Usuários) e suas funções de gerenciamento.
class Biblioteca:
    # * Declaração dos componentes de um objeto Biblioteca(Livros e Usuários), usando dicionários.
    def __init__(self):
        self.livros: Livro = {}  # Usando um dicionário para mapear títulos para objetos Livro
        self.usuarios = {}  # Usando um dicionário para mapear IDs de usuário para objetos Usuario

    # * Implementação da função de inserção de novos livros.
    def cadastrar_livro(self, titulo: str, autor: str):

        # * Verifica se já existe um livro cadastrado, buscando pelo título.
        # TODO Mudar a busca de livro por título p/ busca por ISBN/ISSN.
        # TODO Considerando que pode ter Livros com o mesmo título ou que o usuário não saiba o título.
        if titulo in self.livros:
            print(f"Erro: Livro com título '{titulo}' já existe na biblioteca.\n")
        else:
            livro = Livro(titulo, autor)
            self.livros[titulo] = livro
            # TODO Adicionar demais informações do livro

    # * Implementação da função de inserção de novos usuários.
    def cadastrar_usuario(self, nome: str, id:int):

        # * Verifica se já existe um usuário cadastrado, buscando pelo id.
        # ? Mudar a busca de usuário por id p/ busca por CPF ou Matrícula, caso faça sentido.
        if id in self.usuarios:
            print(f"Erro: Usuário com ID '{id}' já existe na biblioteca.\n")
        else:
            usuario = Usuario(nome, id)
            self.usuarios[id] = usuario
            # TODO Adicionar demais informações do usuário
            print(f"{usuario.nome} foi cadastrado(a) com sucesso\n")

    # * Implementação da função de efetuar um empréstimo.
    def emprestar_livro(self, titulo: str, id_usuario: int):

        # * Recebendo os dados do empréstimo (Livro emprestado e Tomador do empréstimo)
        livro = self.livros.get(titulo)
        usuario = self.usuarios.get(id_usuario)

        # * Verifica se livro, usuario e disponibilidade do livro existem/são verdadeiros.
        # TODO Adicionar verificação da quantidade disponível da mesma obra, caso tenha.
        # TODO Lembrar antes de implementar o atributo quantidade na classe Livro,
        # TODO vide Linha 6 -> (file:///C:\Users\Paulo\Documents\GitHub\library_management_system\sg_bib_prototype_1.py#L6).
        
        if livro:
            if usuario:
                if livro.disponibilidade:
                    # * Caso seja verdade define a disponibilidade do livro como falsa, p/ impedir novo empréstimo da obra.
                    livro.disponibilidade = False

                    # * Adiciona o livro solicitado na lista de livros emprestados, utilizando o título como índice.
                    # TODO Modificar para identificar pelo isbn/issn como índice no lugar de título.
                    # TODO Lembrar antes de implementar a adição do atributo na classe e a mudança de índice na construção do dicionário,
                    # TODO vide Linha 5 -> (file:///C:\Users\Paulo\Documents\GitHub\library_management_system\sg_bib_prototype_1.py#L5)
                    # TODO e Linha 6 -> (file:///C:\Users\Paulo\Documents\GitHub\library_management_system\sg_bib_prototype_1.py#L32) respectivamente.
                    
                    usuario.livros_emprestados.add(titulo)

                    # * Imprime um registro do empréstimo na tela.
                    print(f"O {livro.titulo} foi emprestado para {usuario.nome}\n")
                else:
                    # * Informa que o livro solicitado não está disponível.
                    print(f"O {livro.titulo} se encontra indisponível\n")
            else:
                # * Imprime que o usuário solicitante não existe.
                print(f"O usuário solicitante do emprestimo não está cadastrado\n")
                print(f"Por favor, realize o cadastro e tente novamente.\n")
        else:
            # * Imprime que o livro solicitado não existe.
            print(f"O livro solicitado não está cadastrado\n")
            print(f"Por favor, registre a obra e tente novamente.\n")

    def devolver_livro(self, titulo: str, id_usuario: int):

        # * Recebendo os dados do empréstimo (Livro emprestado e Tomador do empréstimo)
        livro = self.livros.get(titulo)
        usuario = self.usuarios.get(id_usuario)

        if livro:
            if usuario:
                if not livro.disponibilidade and titulo in usuario.livros_emprestados:
                    livro.disponibilidade = True
                    usuario.livros_emprestados.remove(titulo)
                    print(f"O {livro.titulo} foi devolvido por {usuario.nome}\n")
                else:
                    print(f"O {livro.titulo} não se encontra em posse do usuário {usuario.nome}\n")
            else:
                # * Imprime que o usuário solicitante não existe.
                print(f"O usuário solicitante do emprestimo não está cadastrado\n")
                print(f"Por favor, realize o cadastro e tente novamente.\n")
        else:
            # * Imprime que o livro solicitado não existe.
            print(f"O livro solicitado não está cadastrado\n")
            print(f"Por favor, registre a obra e tente novamente.\n")

    def busca_por_titulo(self, titulo: str):

        # * Recebe como parâmetro o título e retorna as informações da obra.
        # TODO Adicionar as demais informações do livro. 
        livro = self.livros.get(titulo)
        if livro:
            # TODO Adicionar a quantidade quando disponível e retornar quando tiver sido emprestado.
            return f"Livro: '{titulo}'\n Autor: {livro.autor}\n"
        else:
            return "Livro não encontrado.\n"

    def busca_por_autor(self, autor: str):
        
        # * Recebe como parâmetro o autor e retorna as obras cadastradas com aquele autor.
        # * Contém um "for" que percorre o dicionário Livros em busca do nome do autor em cada um dos livros.
        # ? Examinar possibilidade/necessidade de fazer a busca dividindo na metade e buscando em um lado de cada vez. @Andravi
        # ? para reduzir a complexidade do algoritmo de busca.
        livros_do_autor = [livro.titulo for livro in self.livros.values() if livro.autor == autor]
        if livros_do_autor:
            return f"Livros do autor '{autor}': {', '.join(livros_do_autor)}\n"
        else:
            return "Autor não encontrado.\n"

    def relatorio_emprestimos(self):
        
        # * Contém um "for" que percorre o dicionário Usuarios e verifica para cada usuário,
        # * se existem livros emprestados. Caso existam, são impressos os nomes de cada um dos livros emprestados
        for usuario in self.usuarios.values():
            if usuario.livros_emprestados:
                livros_emprestados = ', '.join(usuario.livros_emprestados)
                print(f"{usuario.nome} tem os seguintes livros emprestados: {livros_emprestados}\n")

    # * Implementação do salvamento dos dados de gerenciamento da biblioteca.
    ''' Já que na atividade em questão não é permitido usar banco de dados,
        eu(@WesleyBarbosaMR) e @Andravi, após pequena pesquisa,
        tivemos a ideia de usar a biblioteca Pickle
        para armazenar os dados em um arquivo serializável ".pkl".
        Garantindo assim a persistência dos dados
        sem a implementação de um banco de dados.
    '''
    def salvar_dados(self):
        # * A função define um arquivo ".pkl" onde serão inseridas as informações
        # * e define a permissões de escrita (w) e define como um arquivo binário(b)
        with open('dados_biblioteca.pkl', 'wb') as arquivo:
            # * Em seguida atribui o conteúdo completo dos dois dicionários.
            ''' Inseridos sem modificações visuais, 
                já que não pretende-se que o arquivo seja lido por humanos,
                e sim apenas serializado para que o programa Python
                possa lê-lo novamente na próxima execução.
            '''
            dados = {'livros': self.livros, 'usuarios': self.usuarios}
            pickle.dump(dados, arquivo)

    def carregar_dados(self):
         # * Aqui, a função busca no diretório um arquivo ".pkl"
        # * e define a permissões de leitura (r) e define como um arquivo binário(b)
        try:
            with open('dados_biblioteca.pkl', 'rb') as arquivo:
                # * Em seguida carrega o conteúdo completo do arquivo
                # * e separa para os dois dicionários,
                # * utilizando os mesmos identificadores como referência.
                dados = pickle.load(arquivo)
                self.livros = dados.get('livros', {})
                self.usuarios = dados.get('usuarios', {})
        except FileNotFoundError:
            # * Caso o arquivo ainda não exista, não existe nada a carregar
            # * e a execução segue.
            pass
        except Exception as e:
            # * Caso o arquivo apresente algum erro ao carregar
            # * é exibido um aviso e a execução segue
            print(f"Erro ao carregar dados: {e}")
            pass

def main():
    biblioteca = Biblioteca()

    # Exemplo de uso
    biblioteca.cadastrar_livro("Harry Potter", "J.K. Rowling")
    biblioteca.cadastrar_livro("Percy Jackson", "Rick Riordan")
    biblioteca.cadastrar_livro("Livro Teste", "Wesley Barbosa")
    biblioteca.cadastrar_usuario("Maria", 1)
    biblioteca.cadastrar_usuario("João", 2)
    biblioteca.emprestar_livro("Harry Potter", 1)
    biblioteca.emprestar_livro("Percy Jackson", 1)
    biblioteca.emprestar_livro("Livro Teste", 2)

    biblioteca.relatorio_emprestimos()

    # Salvar e carregar dados
    biblioteca.salvar_dados()
    biblioteca.carregar_dados()

if __name__ == "__main__":
    main()
