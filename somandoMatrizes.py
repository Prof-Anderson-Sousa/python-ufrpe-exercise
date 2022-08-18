# ENTRADA

# MATRIZ 1
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
n6 = int(input())
n7 = int(input())
n8 = int(input())
n9 = int(input())
# MATRIZ 2
n10 = int(input())
n11 = int(input())
n12 = int(input())
n13 = int(input())
n14 = int(input())
n15 = int(input())
n16 = int(input())
n17 = int(input())
n18 = int(input())

# PROCESSAMENTO

# MATRIZ 1
matriz1 = []
matriz1.append([n1,n2,n3],)
matriz1.append([n4,n5,n6],)
matriz1.append([n7,n8,n9],)
print(matriz1)

# MATRIZ 2
matriz2 = []
matriz2.append([n10,n11,n12],)
matriz2.append([n13,n14,n15],)
matriz2.append([n16,n17,n18])
print(matriz2)

# SOMA DAS MATRIZES INDÍCE 0
matriz3_1 = []
soma1 = matriz1[0][0] + matriz2[0][0]
soma2 = matriz1[0][1] + matriz2[0][1]
soma3 = matriz1[0][2] + matriz2[0][2]
matriz3_1.append(soma1)
matriz3_1.append(soma2)
matriz3_1.append(soma3)


# SOMA DAS MATRIZES INDÍCE 1
matriz3_2 = []
soma4 = matriz1[1][0] + matriz2[1][0]
soma5 = matriz1[1][1] + matriz2[1][1]
soma6 = matriz1[1][2] + matriz2[1][2]
matriz3_2.append(soma4)
matriz3_2.append(soma5)
matriz3_2.append(soma6)


# SOMA DAS MATRIZES INDÍCE 2
matriz3_3 = []
soma7 = matriz1[2][0] + matriz2[2][0]
soma8 = matriz1[2][1] + matriz2[2][1]
soma9 = matriz1[2][2] + matriz2[2][2]
matriz3_3.append(soma7)
matriz3_3.append(soma8)
matriz3_3.append(soma9)

# SAÍDA

print(matriz3_1)
print(matriz3_2)
print(matriz3_3)

