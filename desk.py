import medico as med
import paciente as pac

while True:
    print("1. CADASTRAR")
    print("2. BUSCAR")
    print("0. SAIR")

    op = int(input())

    if op == 1:
        print("1. CADASTRAR PACIENTE")
        print("2. CADASTRAR MEDICO")
        op3 = int(input())
        if op3 == 1:
            pacs = pac.Paciente()
            pacs.nome = input("Nome do paciente: ").lower().strip()
            pacs.idade = int(input("Idade do paciente: "))
            pacs.acom = input("Nome do acompanhante: ").lower().strip()
            pacs.crm = int(input("Numero do CRM do medico: "))
            pacs.quarto = input("Numero da sala: ").lower().strip()
            pacs.cadastro()

        else:
            meds = med.Medico()
            meds.crm = int(input("CRM do medico: "))
            meds.nome = input("Nome do medico: ").lower().strip()
            meds.cadastro()
            
    elif op == 2:
        print("1. BUSCAR PACIENTE")
        print("2. LISTA DE PACIENTES")
        print("3. LISTA DE MEDICOS")

        op2 = int(input())

        if op2 == 1:
            nome = input("Nome do Paciente: ").lower()
            print("ola")
            pacs = pac.Paciente()
            pacs.buscarPacientes(nome)

        elif op2 == 2:
            pacs = pac.Paciente()
            pacs.ListPacientes()
        else:
            meds = med.Medico()
            meds.Medicos_cadastrados()

    else:
        break