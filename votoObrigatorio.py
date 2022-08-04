# PROGRAMA PARA CONFERIR SE O VOTO É OBRIGATÓRIO

# ENTRADA

idade = int(input())
analfabeto = str(input()).upper()

# PROCESSAMENTO / SAÍDA

if idade > 18 and idade <= 70 and analfabeto == "N":
    print("Voto obrigatório")

elif idade <= 18 and analfabeto == "N":
    print("Voto não obrigatório")

elif idade > 70 and analfabeto == "N":
    print("Voto não obrigatório")

elif analfabeto == "S":
    print("Voto não obrigatório")

