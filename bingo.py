# PROGRAMA PARA SORTEAR BINGO
from random import randint

print("Vamos Iniciar o Bingo 🥳🎉🎊")
convite = input("Digite 'S' para Sim, ou 'N' para Não: ").upper()
bingo = set({})


while (convite == "S"):
    print("Vamos Iniciar a Próxima Rodada")
    proxRod = input("Digite 'S' para Sim, ou 'N' para Não: ").upper()
    if (proxRod == "S"):
        numSort = randint(0,99)
        bingo.add(numSort)
        print("🌐 O Número Sorteado foi:",numSort)
        print("🌐 Numéros Sorteados:",bingo)
    elif(proxRod == "N"):
        print("🛑 O Bingo foi encerrado parabéns ao vencedor 👏👏👏")
        break
    elif(proxRod != "S" or "N"):
        print("❌ Digite uma opção válida!")
else:
    print("✔️ OK, Até uma Próxima!")