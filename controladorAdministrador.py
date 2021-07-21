from telaAdministrador import TelaAdministrador
from administradorDAO import AdministradorDAO


class ControladorAdministrador:
    
    def __init__(self):
        self.__tela_administrador = TelaAdministrador(self)
        self.__administrador_dao = AdministradorDAO()

    def cadastrar_administrador(self):
        while True:
            valores = self.__tela_administrador.tela_cadastrar_administrador()
            if not valores:
                break
            #existe_cpf = self.verifica_cpf_jah_existente(int(valores[2]))
            #if existe_cpf:
            #    self.__tela_administrador.tela_erro('\nNumero de CPF de administrador jah cadastrado!')
            #    continue
            sucesso_add = self.__administrador_dao.add(valores[0], valores[1])
            if not sucesso_add:
                self.__tela_administrador.tela_erro('Erro no cadastro')
            break

    def verifica_cadastro_completo(self, values):
        if values[0] == '' or values[1] == '':
            self.__tela_administrador.close_tela_cadastro()
            return False
        return True

    def remover_administrador(self):
        botao, num_titulo_informado = self.__tela_administrador.get_informacao('Remover Administrador', 'CPF do Administrador: ')
        if botao == 'Submit':
            sucesso_remover = self.__administrador_dao.remove(int(num_titulo_informado))
            if not sucesso_remover:
                self.__tela_administrador.tela_erro('Erro na remocao!\n Nome informado inexistente')
            else:
                self.__tela_administrador.aviso('Removido com sucesso.')
                self.registrar_op('remocao')

    def listar_administrador(self):
        dic_nome_num_administradores = {}
        lista_administradores= self.__administrador_dao.get_all()
        for administrador in lista_administradores:
            dic_nome_num_administradores[administrador.nome] = administrador.cpf
        self.__tela_administrador.mostrar_lista(dic_nome_num_administradores)

    def verifica_cpf_jah_existente(self, cpf):
        verificacao = self.__administrador_dao.get(cpf)
        if verificacao == None:
            return False
        return True

    def get_nome_administrador_by_titulo(self, num_titulo: int):
        administrador = self.__administrador_dao.get(num_titulo)
        return administrador.nome

    def abre_tela_inicial(self):
        while True:
            switcher = {1: self.cadastrar_administrador,
                        2: self.listar_administrador,
                        3: self.remover_administrador
                        }

            try:
                resposta = self.__tela_administrador.open()
                opcao = int(resposta[1].get(0))
                self.__tela_administrador.close_tela_principal()
                if opcao == 0:
                    break
            except TypeError:
                self.__tela_administrador.close_tela_principal()
                break
            except ValueError:
                self.__tela_administrador.close_tela_principal()
                self.__tela_administrador.tela_erro('Entre com uma opcao valida')
                continue
            try:
                funcao_escolhida = switcher[opcao]
                funcao_escolhida()
            except KeyError:
                self.__tela_administrador.tela_erro('Opcao invalida')

    def inicia(self):
        self.abre_tela_inicial()


    def finalizar(self):
        self.__tela_administrador.tela_finaliza()