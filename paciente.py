class Paciente():
    dic = {}
    
    def __init__(self):
        self.nome = None
        self.idade = None
        self.acom = None
        self.quarto = None
        self.crm = None
        
    def cadastro(self):
        if self.nome in Paciente.dic:
            print("paciente ja cadastrado")
        else:
            Paciente.dic[self.nome] = self
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
            print(f"Acompanhante: {paciente.acom}")
            print(f"Quarto: {paciente.quarto}")
            print(f"CRM Médico Responsável: {paciente.crm}")
