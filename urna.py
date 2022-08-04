eleitor = int(input())
José_Alfredo = 0
Maria_Junqueira = 0
Marivaldo_Silva = 0
Juliana_Antônia = 0
nulo = 0
for x in range(eleitor):
    voto = input().strip()
    if (voto == '1'):
        José_Alfredo += 1

    elif (voto == '2'):
        Maria_Junqueira += 1

    elif (voto == '3'):
        Marivaldo_Silva += 1

    elif (voto == '4'):
        Juliana_Antônia += 1

    elif (voto == 'sair'):
        eleitor = x
        break
    else:
        nulo += 1

print(f'Nome--------------Votos--------------Porcentagem')
print(
    f'José Alfredo ------ {José_Alfredo} ------------------- {(José_Alfredo * 100) / eleitor:.2f}%'
)
print(
    f'Maria Junqueira --- {Maria_Junqueira} ------------------- {(Maria_Junqueira * 100) / eleitor:.2f}%'
)
print(
    f'Marivaldo Silva --- {Marivaldo_Silva} ------------------- {(Marivaldo_Silva * 100) / eleitor:.2f}%'
)
print(
    f'Juliana Antônia --- {Juliana_Antônia} ------------------- {(Juliana_Antônia * 100) / eleitor:.2f}%'
)
print(
    f'Nulo -------------- {nulo} ------------------- {(nulo * 100) / eleitor:.2f}%'
)