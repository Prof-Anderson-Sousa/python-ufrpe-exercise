inicial = int(input())
final = int(input())

while inicial <= final:
    if (inicial % 2 == 0) or (inicial % 3 == 0):
        print(inicial)

    inicial += 1
