

from abc import ABC, abstractmethod
from abc import ABC


class Pessoa(ABC):

    def __init__(self, nome: str, cpf: str):
        
        super().__init__(nome, cpf)
        self.__login = ''
        self.__senha = ''

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