# CADASTRO DE ALUNOS - FACULDADE
cadastroDeAlunos = {}

inicio = input("Podemos Iniciar o Programa?\nDigite 'S' para Sim, ou 'N' para Não: ").upper()

while(inicio == "S"):
    print('=======================================================')
    print("Bem-Vindo ao Softex-UFRPE 2.0")
    print("Opções Disponíveis no Sistema")
    print("01 - Adicionar Aluno ao Sistema")
    print("02 - Consultar Cadastro de Aluno")
    print("03 - Remover Aluno do Sistema")
    print("04 - Cadastrar Nova Disciplina")
    print("05 - Consultar Matricula em Disciplina")
    print("06 - Sair")
    print('=======================================================')
    solicitacao = input("Digite o Número da Opção Desejada: ").upper()


    def addAluno():
        cpf = int(input("Digite o CPF do Aluno: "))
        nome = input("Digite o Nome do Aluno: ")
        disciplina = input("Digite o Nome da Disciplina: ")
        codigo = input("Digite o Código da Disciplina: ")
        semestre = input("Digite o Semestre da Disciplina: ")

        if cadastroDeAlunos.get(cpf):
            print("Já temos um cadastro com este CPF:",cpf)
            print('=======================================================')
        else:
            cadastroDeAlunos[cpf] = (nome, disciplina, codigo, semestre, set())
            print(cadastroDeAlunos)
            print("Aluno Cadastrado com Sucesso!")
            print('=======================================================')
            return

    def consultCad():
        cpf = int(input("Digite o CPF Cadastrado: "))

        if cadastroDeAlunos.get(cpf):
            print("Já temos um cadastro com este CPF:",cpf)
            print('=======================================================')
        else:
            print("Já temos um cadastro com este CPF:",cpf)
            print('=======================================================')
            return
    
    def removeAluno():
        cpf = int(input("Digite o CPF do Aluno que deseja remover: "))
        
        if cadastroDeAlunos.get(cpf):
            cadastroDeAlunos.pop(cpf, None)
            print("Aluno Removido com Sucesso")
            print('=======================================================')
            return
        else:
            print('Não Temos Aluno Cadastrado com esse CPF, tente novamente!')
            print('=======================================================')
            return
    
    def cadNovaDisciplina():
        cpf = int(input("Digite o CPF do Aluno para Adicionar Nova Disciplina: "))
        novaDisciplina = input("Digite o Nome da Nova Disciplina: ")
        codNovaDisciplina = input("Digite o Código da Nova Disciplina: ")
        semNovaDisciplina = input("Digite o Semestre da Nova Disciplina: ")
        disciplinas = (novaDisciplina, codNovaDisciplina, semNovaDisciplina)
        cadastroDeAlunos[cpf][4].add(disciplinas)
        print(cadastroDeAlunos)
    
    def consultMat():
        cpf = int(input("Digite o CPF do Aluno para Verificar a Matricula: "))
        codigo = input("Digite o código da Disciplina: ")
        if codigo in cadastroDeAlunos[cpf]:
            print("Aluno está Matriculado na Disciplina")
        else:
            print("Aluno não está Matriculado na Disciplina")

    if (solicitacao == "1" or solicitacao == "01"):
        addAluno()

    elif (solicitacao == "2" or solicitacao == "02"):
        consultCad()

    elif (solicitacao == "3" or solicitacao == "03"):
        removeAluno()

    elif (solicitacao == "4" or solicitacao == "04"):
        cadNovaDisciplina()

    elif (solicitacao == "5" or solicitacao == "05"):
        consultMat()

    elif (solicitacao == "6" or solicitacao == "06"):
        print("Programa encerrado, até a Próxima")
        break

else:
    if(inicio == "N"):
        print("Programa encerrado, até a Próxima")
    elif(inicio != "N" or "S"):
        print("Digite um Caractere Válido")