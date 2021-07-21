import pickle
from administrador import Administrador


class AdministradorDAO():
    def __init__(self, datasource = 'administrador.pkl'):
        self.datasource = datasource
        self.object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.object_cache, open(self.datasource, 'wb'))

    def __load(self):
        self.object_cache = pickle.load(open(self.datasource, 'rb'))

    def add(self, nome, cpf):
        if (isinstance(nome, str) and
            isinstance(cpf, str)):
                novo_admin = Administrador(nome, cpf)
                self.object_cache[novo_admin.cpf] = novo_admin
                self.__dump()
                return True
        return False

    def get(self, key):
        if isinstance(key, int):
            try:
                return self.object_cache[key]
            except KeyError:
                return None

    def remove(self, key):
        if isinstance(key, str):
            try:
                self.object_cache.pop(key)
                self.__dump()
                return True
            except KeyError:
                return False

    def get_all(self):
        return self.object_cache.values()
