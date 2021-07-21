import PySimpleGUI as sg


class TelaAdministrador:

    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = None
        self.__window_sec = None

    def init_components(self):
        layout = [
        [sg.Text('Menu de opcoes:')],
        [sg.Text('1- Cadastrar novo Administrador')],
        [sg.Text('2- Listar Administradores')],
        [sg.Text('3- Remover Administrador')],
        [sg.Text('0- Encerrar')],
        [sg.Text('opcao', size=(15, 1)), sg.InputText('')],
        [sg.Submit()]
        ]
        self.__window = sg.Window('Gerenciar Administrador').Layout(layout)

    def msg_encerrar(self):
        layout2 = [
        [sg.Text('O programa será encerrado. Deseja continuar?')],
        [sg.Submit(), sg.Cancel()]
        ]
        self.__window_sec = sg.Window('Encerramento').Layout(layout2)
        resposta = self.__window_sec.Read()
        return resposta

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values

    def close_tela_principal(self):
        self.__window.Close()

    def close_tela_secundaria(self):
        self.__window_sec.Close()

    def tela_cadastrar_administrador(self):
        while True:
            layout_cadastro = [
            [sg.Text('Preencha os dados abaixo:')],
            [sg.Text('Nome do Aministrador', size=(20, 1)), sg.InputText('')],
            [sg.Text('Cpf do Administrador', size=(20, 1)), sg.InputText('')],
            [sg.Button('Enviar Dados'), sg.Cancel()]
            ]
            tela_cadastro = sg.Window('Cadastrar Administrador').Layout(layout_cadastro)
            button, values = tela_cadastro.Read()
            tela_cadastro.Close()
            if button == 'Cancel':
                return False
            cadastro_ok = self.__controlador.verifica_cadastro_completo(values)
            if cadastro_ok:
                return values
            self.aviso('Cadastro incompleto. Repita a operação.')

    def get_informacao(self, msg_cabecalho, msg_corpo):
        layout_info = [
        [sg.Text(msg_corpo, size=(30, 1)), sg.InputText('')],
        [sg.Submit(), sg.Cancel()]
        ]
        tela_get_info = sg.Window(msg_cabecalho).Layout(layout_info)
        button, values = tela_get_info.Read()
        tela_get_info.Close()
        return button, values[0]

    def mostrar_lista(self, lista_dic):
        layout_lista = [
        [sg.Text('Nome - CPF')],
        [sg.Text('------------------------------------')],
        [sg.Text('\n'.join(nome + '  -  ' + str(lista_dic[nome]) for nome in lista_dic))],
        [sg.Ok()]
        ]
        tela_lista = sg.Window('Lista de Administradores').Layout(layout_lista)
        tela_lista.Read()
        tela_lista.Close()


    def tela_erro(self, msg_erro):
        layout_erro = [
        [sg.Text(msg_erro)],
        [sg.Ok()]
        ]
        tela_erro = sg.Window('Erro').Layout(layout_erro)
        tela_erro.Read()
        tela_erro.Close()
 
    def tela_finaliza(self):
        retorno = self.msg_encerrar()
        if retorno[0] == 'Submit':
            self.close_tela_secundaria()
            self.close_tela_principal()
            exit(0)
        else:
            self.close_tela_secundaria()
