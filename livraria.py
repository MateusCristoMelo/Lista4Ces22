class Livraria():
    """
    Classe da livraria em si.
    """
    def __init__(self):
        self.nomelivraria = "" # o nome da livraria
        self.localizacao = "" # localizacao da livraria

class Livro(Livraria):
    """Classe do livro"""
    def __init__(self):
        super().__init__
        self.autor = "" # nome do autor do livro
        self.titulo = "" # titulo do livro
        self.genero = "" # genero do livro
        self.editora = "" # editora do livro
        self.edicao = "" # edicao do livro

class CustosLivro(Livro):
    """Classe dos custos de cada livro"""
    def __init__(self):
        super().__init__
        self.precocusto = "" # preco de custo do livro
        self.precovenda = "" # preco de venda do livro

    def calcularimpostos(self):
        #codigo para o calculo dos impostos a partir do genero, preco de venda e preco de custo
        imposto = self.precovenda - self.precocusto #falta inserir o genero no calculo do imposto
        return imposto

class AdministracaoLivro(Livro):
    """Classe de administracao dos livros"""
    def __init__(self):
        super().__init__

    def inserirexemplar():
        #codigo para inserir um exemplar no estoque
        return

    def removerexemplar():
        #codigo para remover um exemplar do estoque
        return

    def consultaexemplar():
         #codigo para consultar quantos exemplares existem no estoque
         return

    def alteracaoexemplar():
        #codigo para alterar um dado exemplar
        return
    
class Autor(Livraria):
    """Classe dos autores"""
    def __init__(self):
        self.nomeautor = ""
        self.email = ""
        self.exemplaresdeautoria = ""

class OrdemdeCompra(Livraria):
    """Classe das ordens de compra"""
    def __init__(self):
        self.numerodaordem = "" #numero da ordem de compra
        self.cliente = "" #cliente que fez a compra
        self.exemplarescomprados = "" #exemplares que foram comprados

class AdministracaoOrdemdeCompra(OrdemdeCompra):
    """Classe de administracao dos livros"""
    def __init__(self):
        super().__init__

    def inseriroc():
        #codigo para inserir uma nova ordem de compra
        return

    def removeroc():
        #codigo para remover uma ordem de compra
        return

    def consultaroc():
        #codigo para consultar uma ordem de compra
        return

    def alteraroc():
        #codigo para alterar uma ordem de compra
        return

class Cliente(Livraria):
    """Classe dos clientes"""
    def __init__(self):
        self.nomecliente = ""
        self.email = ""

class AdministracaoCliente(Cliente):
    """Classe de administracao dos livros"""
    def __init__(self):
        super().__init__

    def inserircliente():
        #codigo para adicionar um novo cliente na base de dados
        return

    def removercliente():
        #codigo para remover um cliente da base de dados
        return

    def consultarcliente():
        #codigo para consultar cadastro do cliente
        return

    def alteracaocliente():
        #codigo para alterar cadastro do cliente
        return

class Cafeteria(Livraria):
    """Classe da cafeteria"""
