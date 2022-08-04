# PROGRAMA PARA ADVINHAR NÚMERO PENSADO PELO USUÁRIO
# IMPORTANDO BIBLIOTECA
import random

# PERGUNTA INICIAL
print("PENSE NUM NÚMERO DE 0 A 100")
print("RESPONDA 'S', PARA SIM E 'N', PARA NÃO!")
p1 = input("JÁ PENSOU? ").upper()

# MENSAGEM DE INÍCIO
if p1 == "S":
  inicio = True
  print("Legal, Vamos Iniciar o Jogo!")

else:
  print("Até a Próxima!")

# PERGUNTA 50%
if inicio == True:
  maior = input("Seu Numéro é Igual ou Maior que 50? ").upper()
  
if maior == "S":
  number = random.randint(50, 101)
  print("-------------------------------")
  print("Seu Número é", number)
  result = input("Acertamos o Valor? ").upper()
  if result == "S":
    check = True
    print("-------------------------------")
# PERGUNTA 25%
  maior1 = input("Seu Numéro é Maior ou Igual a 75? ").upper()
  
  if maior1 == "S":
    check = False
    while (check == False):
        number = random.randint(75, 101)
        print("-------------------------------")
        print("Seu Número é", number)
        result = input("Acertamos o Valor? ").upper()
        if result == "S":
          check = True
          print("-------------------------------")
          print("Conseguimos, Uau, Até a Próxima")
        continue
      
  if maior1 == "N":
    check = False
    while (check == False):
        number = random.randint(50, 76)
        print("-------------------------------")
        print("Seu Número é", number)
        result = input("Acertamos o Valor? ").upper()
        if result == "S":
          check = True
          print("-------------------------------")
          print("Conseguimos, Uau, Até a Próxima")
        continue
            
elif maior == "N":
  number = random.randint(0, 51)
  print("-------------------------------")
  print("Seu Número é", number)
  result = input("Acertamos o Valor? ").upper()
  if result == "S":
    check = True
    print("-------------------------------")
  maior1 = input("Seu Numéro é Maior ou Igual a 25? ").upper()
  
  if maior1 == "S":
    check = False
    while (check == False):
        number = random.randint(25, 51)
        print("-------------------------------")
        print("Seu Número é", number)
        result = input("Acertamos o Valor? ").upper()
        if result == "S":
          check = True
          print("-------------------------------")
          print("Conseguimos, Uau, Até a Próxima")
        continue
      
  if maior1 == "N":
    check = False
    while (check == False):
        number = random.randint(0, 26)
        print("-------------------------------")
        print("Seu Número é", number)
        result = input("Acertamos o Valor? ").upper()
        if result == "S":
          check = True
          print("-------------------------------")
          print("Conseguimos, Uau, Até a Próxima")
        continue

# MENSAGEM DE ERROS
else:
  print("Digite uma Opção Válida")