def salvarAluno(aluno, disciplinas) :

  cadastroCompleto = [ aluno, disciplinas]

  print(cadastroCompleto)

 

def cadastro(cadastro) : 

  cadastro = input("Deseja cadastrar um aluno? 's' para sim e 'n' para não").lower()

 

aluno = {

      "CPF": 0,

      "Nome" :""

}

 

disciplinas = {

    "Código" : 0,

    "Descrição" : "",

    "Semestre": 0
}

 

cadastroCompleto = [aluno, disciplinas]

    

 

cadastro()

while cadastro == 's' :

 

  print("Digite os campos abaixo para cadastrar um aluno")

  for chave in aluno : 

    aluno[chave] = input(chave + ":")

 

for entry in aluno:

    #if aluno['CPF'] == aluno['CPF'] :

      print("Aluno já cadastrado!")

      print("Digite os dados das disciplinas para cadastro (OBS: Para o semestre digite 1 ou 2)")

      for chave in disciplinas : 

          disciplinas[chave] = input(chave + ":")
else : 

      salvarAluno(aluno, disciplinas)

      cadastroCompleto.append(salvarAluno)

      print(cadastroCompleto)

      cadastro()