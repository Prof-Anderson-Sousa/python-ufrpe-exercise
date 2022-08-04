# ENTRADA
qtPao = float(input())
vlPao = float(input())
qtQueijo = float(input())
vlQueijo = float(input())

# PROCESSAMENTO
gPao = qtPao * vlPao
gQueijo = qtQueijo * vlQueijo
total = gPao + gQueijo

# SAÍDA
print("Pao: R$ " + str(gPao))
print("Queijo: R$ " + str(gQueijo))
print("Total: R$ " + str(total))
