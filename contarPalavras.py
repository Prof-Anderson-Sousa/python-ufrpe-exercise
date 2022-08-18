from operator import itemgetter
texto = input().lower()

# REMOVER CARACTERES ESPECIAIS
# texto_sem_pontuacao = ''
# for c in texto:
#     if c.isalpha() or c == ' ':
#         texto_sem_pontuacao += c

palavras = texto.split()

frequencia_palavras = {}
for palavra in palavras:
    frequencia_palavras[palavra] = frequencia_palavras.get(palavra, 0) + 1

# CRIAR LISTA COM PALAVRA E QUANTIDADE
listaPalavras = frequencia_palavras.items()

for palavra, qtde in listaPalavras:
    print(f'{palavra} - {qtde}')