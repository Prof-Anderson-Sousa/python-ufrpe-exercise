# Programa para receber 6 números
# Atribuição
soma = 0.0
maior = 0
menor = 0
media = 0.0
numeros = []
for i in range(0, 6, 1):
    valor = float(input("Por favor digite o próximo número: "))
    numeros.append(valor)
    print("A lista está assim: ", *numeros)
    # acumulador
    soma = soma + valor
    # acumulador contraido
    # soma += valor
    if i == 0:
        maior = valor
        menor = valor
        indexMaior = i
        indexMenor = i
    elif valor > maior:
        maior = valor
        indexMaior = 1
    elif valor < menor:
        menor = valor
        indexMenor = i
print("\n\nSua lista final é: ", *numeros)
# for contador in range(0, len(numeros),1):
#    print(numeros[numeros])
# for numero in numeros:
print("A soma é: ", sum(numeros))
print("O primeiro é : {:.0f}".format(numeros[0]))
tamanho = len(numeros)
media = (float(soma) / float(tamanho))
print("O tamanho é: {:.2f}".format(len(numeros)))
print("A média é: ", media)
print("O maior é: ", max(numeros), "e está na posição ", numeros.index(max(numeros)))
print("O menor é: ", min(numeros), "e está na posição ", indexMenor)