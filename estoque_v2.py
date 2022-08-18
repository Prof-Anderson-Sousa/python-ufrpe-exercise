#VARIAVEIS
#computadas
codigoProdutos = [(1,"Biscoito","Doce"),(2,"Salgadinho","Salgado"),(3,"Batata Chips","Salgado"),(4,"Feijão","Preto"),(5,"Arroz","Parbolizado"),(6,"Macarrão","Massa"),(7,"Farinha","Temperada"),(8,"Açúcar","Demerara"),(9,"Sal","Refinado"),(10,"Escova","Cerdas Macias")]
quantidadeProdutos = [8,7,2,3,5,9,6,5,5,3]
quantidadeAcabando = []
#entradas
codigoCliente = 1
entradaProduto = 0
entradaQuantidade = 0

#Debug
for i in quantidadeProdutos:
    if i < 3:
        # Indice do Produto com Menor Estoque
        menor3 = quantidadeProdutos.index(i)
        print("------ Produtos com Menos de 3 Itens Disponíveis ------")
        print("Código:",codigoProdutos[menor3][0],"--- Nome:",codigoProdutos[menor3][1],"--- Descrição:",codigoProdutos[menor3][2])

print('=======================================================')
#ENTRADAS
while(codigoCliente != 0):
    codigoCliente = int(input('Qual o seu código de cliente: '))
    if(codigoCliente != 0):
        entradaProduto = int(input('Qual o codigo do produto: '))
        if(entradaProduto in codigoProdutos):
            indexProduto = codigoProdutos.index(entradaProduto)
            entradaQuantidade = int(input('Quantos: '))
            #Verifica a quantidade do produto digitado, caso seja menor ou igual, ele efetua a compra, caso não,
            if(entradaQuantidade <= quantidadeProdutos[indexProduto]):
                print('\nPedido atendido. Obrigado e volte sempre!')
                quantidadeProdutos[indexProduto] -= entradaQuantidade;
            else:
                print('\nNão temos estoque suficiente dessa mercadoria')
        else:
            print('\nCódigo inexistente')
    print('==============================================================')
print('=-=-=-=-=-=-=-=-OBRIGADO POR USAR O PROGRAMA=-=-=-=-=-=-=-=-')
print('Resultado Final\n')
print('Codigos: {}'.format(codigoProdutos))
print('Quantidade: {}'.format(quantidadeProdutos))