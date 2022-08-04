# PROGRAMA PARA CALCULAR INFORMAÇÕES DOS PRIMEIROS 6 NÚMEROS DIGITADOS
print("Por favor digite 6 números")
lista = []
for x in range(0, 6, 1):
  numero = int(input("Por favor digite o número na posição " +str(x) + ": "))
  lista.append(numero)
print(*lista)
print(sum(lista))