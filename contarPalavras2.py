from operator import itemgetter
texto = input().lower()

# SEPARAR PALAVRAS ATRÁVES DO ESPAÇO
palavras = texto.split(" ")

# CRIANDO LISTA COM QUANTIDADE DE REPETIÇÕES
frequencia_palavras = {}
for palavra in palavras:
    frequencia_palavras[palavra] = frequencia_palavras.get(palavra, 0) + 1

print(frequencia_palavras)
# PASSANDO FREQUENCIA DE PALAVRAS PARA UMA TUPLA
listaPalavras = frequencia_palavras.items()

print(listaPalavras)
for palavra, qtde in listaPalavras:
    print(f'{palavra} - {qtde}')