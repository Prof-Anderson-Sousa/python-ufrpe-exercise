texto = input().lower()

texto_sem_pontuacao = ''
for c in texto:
    if c.isalpha() or c == ' ':
        texto_sem_pontuacao += c

print("---------------------------------------------------------------")
print(texto)
print(f'{len(texto)} caracteres carregados')
print("---------------------------------------------------------------")
print(texto_sem_pontuacao)
print(f'{len(texto_sem_pontuacao)} caracteres carregados após limpeza')

palavras = texto_sem_pontuacao.split()
print(palavras)
print(f'{len(palavras)} palavras carregadas')

frequencia_palavras = {}
for palavra in palavras:
    if palavra not in frequencia_palavras:
        frequencia_palavras[palavra] = 0
    frequencia_palavras[palavra] += 1
print(frequencia_palavras)
print(f'{len(frequencia_palavras)} palavras únicas carregadas')

frequencia_palavras1 = {}
for palavra in palavras:
    frequencia_palavras1[palavra] = frequencia_palavras1.get(palavra, 0) + 1

print(frequencia_palavras1)
print(f'{len(frequencia_palavras1)} palavras únicas carregadas com get')

# CONSULTAR PALAVRAS NA LISTA
p = "o"
print(f'{p} - {frequencia_palavras1[p]}')

