print("Iniciando Quiz em Python - UFRPE")
print("Quem disse a famosa frase \"penso, logo, existo?\"")
print("A) Decartes - B) Aristóteles - C) Platão - D) Sócrates")
pontos = 0
resp1 = input()
print("Você selecionou a alternativa: " + resp1)
if resp1 == "A":
    print("Acertou, Parabéns!")
    pontos = pontos + 1

else:
    print("A alternativa correta era letra: A")

print("-------------------------------------------------------")

print("Quem pintou a Monalisa?")
print("A) Tarsila do Amaral  - B) DaVinci - C) Michelangelo - D) Picasso")
resp2 = input()
print("Você selecionou a alternativa: " + resp2)
if resp2 == "B":
    print("Acertou, Parabéns!")
    pontos = pontos + 1
else:
    print("A alternativa correta era letra: B")

print("-------------------------------------------------------")

print("Qual ideia rendeu a Einstein o premio Nobel?")
print("A) Fórmula da Gravidade - B) Teoria da Relatividade  - C) Invenção da Luz - D) Efeito Fotoelétrico")
resp3 = input()
print("Você selecionou a alternativa: " + resp3)
if resp3 == "D":
    print("Acertou, Parabéns!")
    pontos = pontos + 1
else:
    print("A alternativa correta era letra: D")
    pontos = pontos + 1
print("-------------------------------------------------------")

print("Qual o maior rio do mundo?")
print("A) Rio Amazonas - B) Rio Nilo  - C) Rio Mississipi - D) Rio Sena")
resp4 = input()
print("Você selecionou a alternativa: " + resp4)
if resp4 == "A":
    print("Acertou, Parabéns!")
    pontos = pontos + 1
else:
    print("A alternativa correta era letra: A")

print("-------------------------------------------------------")

print("O que a palavra legend significa em português?")
print("A) Legenda  - B) Legendário  - C) Lenda - D) Lendário")
resp5 = input()
print("Você selecionou a alternativa: " + resp5)
if resp5 == "C":
    print("Acertou, Parabéns!")
    pontos = pontos + 1
else:
    print("A alternativa correta era letra: A")


print("-------------------------------------------------------")
print("Você acertou " + str(pontos) + " de 5 Perguntas")
