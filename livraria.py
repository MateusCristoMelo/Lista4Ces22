class Livraria():
    """
    Classe da livraria em si.
    """
    def __init__(self, livraria, localizacao):
        self.nomelivraria = livraria # o nome da livraria
        self.localizacao = localizacao # localizacao da livraria

class Livro(Livraria):
    """Classe do livro"""
    def __init__(self, autor, titulo, genero, editora, edicao):
        super().__init__
        self.autor = autor # nome do autor do livro
        self.titulo = titulo # titulo do livro
        self.genero = genero # genero do livro
        self.editora = editora # editora do livro
        self.edicao = edicao # edicao do livro

class CustosLivro(Livro):
    """Classe dos custos de cada livro"""
    def __init__(self, precocusto, precovenda):
        super().__init__
        self.precocusto = precocusto # preco de custo do livro
        self.precovenda = precovenda # preco de venda do livro

    def pegar_genero(self):
        if(self.genero == "Romance"):
            return 1.1
        elif(self.genero == "Suspense"):
            return 1.2
        else:
            return  1

    def calcularimpostos(self):
        #codigo para o calculo dos impostos a partir do genero, preco de venda e preco de custo
        imposto = (self.precovenda - self.precocusto) * self.pegar_genero #falta inserir o genero no calculo do imposto
        return imposto

class AdministracaoLivro(Livro):
    """Classe de administracao dos livros"""
    def __init__(self):
        self.lista = []

    def inserirexemplar(self, livro):
        self.lista.append(livro)

    def removerexemplar(self, name):
        for i in self.lista:
            if(i.nome == name):
                self.lista.pop(i)
                return

    def consultaexemplar(self, name, edicao):
        c = 0
        for i in self.lista:
            if(i.nome == name and i.edicao == edicao):
                c += 1
        return c

    def alteracaoexemplar(self, name, propriedade, mudanca):
        for i in self.lista:
            if(i.nome == name):
                i.propriedade = mudanca
    
class Autor(Livraria):
    """Classe dos autores"""
    def __init__(self, nomeautor, email,exemplaresdeautoria):
        self.nomeautor = nomeautor
        self.email = email
        self.exemplaresdeautoria = exemplaresdeautoria

class OrdemdeCompra(Livraria):
    """Classe das ordens de compra"""
    def __init__(self, numerodaordem, exemplarescomprados, cliente):
        self.numerodaordem = numerodaordem #numero da ordem de compra
        self.cliente = cliente #cliente que fez a compra
        self.exemplarescomprados = exemplarescomprados #exemplares que foram comprados

class AdministracaoOrdemdeCompra(OrdemdeCompra):
    """Classe de administracao dos livros"""
    def __init__(self):
        self.lista = []

    def inseriroc(self, oc):
        self.lista.append(oc)

    def removeroc(self, name):
        for i in self.lista:
            if(i.nome == name):
                self.lista.pop(i)

    def consultaroc(self, numero):
        for i in self.lista:
            if(i.nome == numero):
                return True
        return False

    def alteraroc(self, name, propriedade, mudanca):
        for i in self.lista:
            if(i.nome == name):
                i.propriedade = mudanca

class Cliente(Livraria):
    """Classe dos clientes"""
    def __init__(self, nomecliente, email):
        self.nomecliente = nomecliente
        self.email = email

class AdministracaoCliente(Cliente):
    """Classe de administracao dos clientes"""
    def __init__(self):
        super().__init__

    def inserircliente(self, cliente):
        self.lista.append(cliente)

    def removercliente(self, name):
        for i in self.lista:
            if(i.nome == name):
                self.lista.pop(i)

    def consultarcliente(self, numero):
        for i in self.lista:
            if(i.nome == numero):
                return True
        return False

    def alteracaocliente(self, name, propriedade, mudanca):
        for i in self.lista:
            if(i.nome == name):
                i.propriedade = mudanca

class Cafeteria(Livraria):
    """Classe da cafeteria"""
