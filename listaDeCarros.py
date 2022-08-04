carros = ["Fusca", "Uno", "Celta", "Ka"]
# COM OS COLCHETES
print(carros)
carros.append("Fiesta")
# SEM OS COLCHETES
print(*carros)
# SELECIONANDO DIRETAMENTE
print("O carro da posição 2 é: ", carros[2])
# ADICIONANDO EM POSIÇÃO ESPECÍFICA
carros[2] = "Gol"
print(carros[2])