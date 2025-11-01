class Paciente():
    dic = {}
    
    def __init__(self):
        self.__nome = None
        self.__idade = None
        self.__quarto = None
        self.__crm = None
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, value):
        self.__idade = value
    
    @property
    def quarto(self):
        return self.__quarto
    
    @quarto.setter
    def quarto(self, value):
        self.__quarto = value
    
    @property
    def crm(self):
        return self.__crm
    
    @crm.setter
    def crm(self, value):
        self.__crm = value
    
    def cadastro(self):
        if self.__nome in Paciente.dic:
            print("paciente ja cadastrado")
        else:
            Paciente.dic[self.__nome] = self
            print("paciente cadastrado com sucesso")
    
    @classmethod
    def ListPacientes(cls):
        print("-----LISTA DE PACIENTES-----")
        for x in cls.dic.values():
            print(f"Paciente: {x.nome} - Idade: {x.idade}")

    @classmethod
    def buscarPacientes(cls, nome):
        paciente = cls.dic.get(nome)
        if paciente:
            print("----- DADOS DO PACIENTE -----")
            print(f"Nome: {paciente.nome}")
            print(f"Idade: {paciente.idade}")
            print(f"Quarto: {paciente.quarto}")
            print(f"CRM Médico Responsável: {paciente.crm}")
