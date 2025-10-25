class Medico():
    dic = {}
        
    def __init__(self):
        self.nome = None
        self.crm = None
    
    def cadastro(sefl):
        if self.nome in Medico.dic:
            print("Medico não encontrado")
        else:
            Medico.dic[sefl.nome] = self
    
    def Medicos_cadastrados(self):
        for x in Medico.dic:
            print(f"Doutor(a): {x.nome} - CRM: {x.crm}")