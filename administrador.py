from pessoa import Pessoa


class Administrador:

    def __init__(self, nome: str, cpf: str):
        
        
        self.__nome = nome
        self.cpf = cpf
        #super().__init__(nome, cpf)
        #self.__login = ''
        #self.__senha = ''
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf
        
'''
    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: int):
        self.__senha = senha
'''