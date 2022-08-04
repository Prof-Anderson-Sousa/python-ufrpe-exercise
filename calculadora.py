# CALCULADORA BY: ANDERSON SOUSA
print("--- Vamos Por a Mão na Massa com os Calculos ---")

# IMPORTANDO BIBLIOTECA MATH
import math

# APRESENTAÇÃO DAS OPÇÕES
print("--------- Escola a Operação Desejada: ----------\n")

print(" 1 - ADIÇÃO (+)\n 2 - SUBTRAÇÃO (-)\n 3 - MULTIPLICAÇÃO (*)\n 4 - DIVISÃO (÷)\n 5 - RAIZ QUADRADA (√)\n 6 - MAIOR DE 3 NUMÉROS (>)\n 7 - MÉDIA ENTRE 4 NÚMEROS (M)\n 8 - SAIR")

# ESCOLHA DA OPERAÇÃO
option = input("Digite o Número da Opção Desejada!\n")

# ADIÇÃO
if option == "1":
  print("------------------------------------------------")

  a = float(input("Digite o Primeiro Valor: "))
  b = float(input("Digite o Segundo Valor: "))
  print("------------------------------------------------")
  adicao = a + b
  print("O Resultado da soma de", a, "+", b, "é igual a", adicao)
  print("------------------------------------------------")

# SUBTRAÇÃO
elif option == "2":
  a = float(input("Digite o Primeiro Valor: "))
  b = float(input("Digite o Segundo Valor: "))
  print("------------------------------------------------")
  subtracao = a - b
  print("O Resultado da Subtração de", a, "-", b, "é igual a", subtracao)
  print("------------------------------------------------")

# MULTIPLICAÇÃO
elif option == "3":
  a = float(input("Digite o Primeiro Valor: "))
  b = float(input("Digite o Segundo Valor: "))
  print("------------------------------------------------")
  multiplicacao = a * b
  print("O Resultado da Multiplicação de", a, "*", b, "é igual a", multiplicacao)
  print("------------------------------------------------")

# DIVISÃO
elif option == "4":
  a = float(input("Digite o Primeiro Valor: "))
  b = float(input("Digite o Segundo Valor: "))
  print("------------------------------------------------")
  divisao = a / b
  print("O Resultado da Divisão de", a, "÷", b, "é igual a", divisao)
  print("------------------------------------------------")

# RAIZ QUADRADA
elif option == "5":
  a = float(input("Digite o Valor e Descubra a Raiz: "))
  print("------------------------------------------------")
  raiz = math.sqrt(a)
  print("O Resultado da Raiz Quadrada de", a, "é igual a", raiz)
  print("------------------------------------------------")

# MAIOR DE 3 NÚMEROS
elif option == "6":
  a = float(input("Digite o Primeiro Valor: "))
  b = float(input("Digite o Segundo Valor: "))
  c = float(input("Digite o Terceiro Valor: "))
  print("------------------------------------------------")
  if a > b and a > c:
    print("O Maior Valor é", a)
  elif b > a and b > c:
    print("O Maior Valor é", b)
  else:
    print("O Maior Valor é", c)
    print("------------------------------------------------")

# MÉDIA ENTRE 4 NÚMEROS
elif option == "7":
  a = float(input("Digite o Primeiro Valor: "))
  b = float(input("Digite o Segundo Valor: "))
  c = float(input("Digite o Terceiro Valor: "))
  d = float(input("Digite o Terceiro Valor: "))
  media = (a + b + c + d) / 4
  print("------------------------------------------------")
  print("A Média Aritmética é", media)
  print("------------------------------------------------")

# SAIR
elif option == "8":
  print("Até a Próxima")

# MENSAGEM DE ERRO
else:
  print("Digite um valor válido!")