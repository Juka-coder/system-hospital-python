class Medico():
    dic = {}
        
    def __init__(self):
        self.__nome = None
        self.__crm = None
    
    @property
    def nome_medico(self):
        return self.__nome
    
    @nome_medico.setter
    def nome_medico(self, novo):
        self.__nome = novo
    
    @property
    def crm_medico(self):
        return self.__crm
    
    
    @crm_medico.setter
    def crm_medico(self, novo):
        self.__crm = novo
    
    def cadastro(self):
        if self.__nome in Medico.dic:
            print("Medico já cadastrado")
        else:
            Medico.dic[self.__nome] = self
    
    def Medicos_cadastrados(self):
        for x in Medico.dic.values():
            print(f"Doutor(a): {x.nome} - CRM: {x.crm}")