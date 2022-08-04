# PROGRAMA VALIDADOR DE SENHAS
check = False
while (check == False):
    # Entrada
    senha1 = str(input()).strip("\r")
    senha2 = str(input()).strip("\r")

    # Processamento
    if len(senha1) < 7:
        print("Senha inválida")
    elif len(senha1) > 8:
        print("Senha inválida")
    elif senha1.islower():
        print("Senha inválida")
    elif senha1.isalpha():
        print("Senha inválida")
    elif senha1 != senha2:
        print("Senha inválida")
    else:
        check = True
        print("Senha válida")
    continue