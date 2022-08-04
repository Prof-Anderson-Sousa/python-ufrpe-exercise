# PROGRAMA PARA GERENCIAR ESTOQUE DE MERCADO
qtd_estoque = [0,50,50,50,50,50,50,50,50,50,50]

name = input("-------------- Olá Cliente, Digite seu nome: ").upper()
print("------------------- Olá,", name, "-------------------")
print("-------- Seja Bem-Vindo ao Mercadão da UFRPE --------")
print("--- Uma Loja Totalmente Inserida no Mundo Digital ---")
usuario = input("Digite seu Código de Cadastro: ").upper()
while True:
    print("----------------------------------------------------")
    print("-------- Caso deseje sair da loja, digite: 0 -------")
    print("----------------------------------------------------")
    if usuario == 0:
        print("-------- Obrigado por visitar nosso mercado ---------")
        break
    produtos = int(input("Qual item você deseja levar: \n 01 - BISCOITO\n 02 - SALGADINHO \n 03 - SORVETE\n 04 - ESCOVA\n 05 - IOGURTE\n 06 - REFRIGERANTE\n 07 - SABONETE\n 08 - REQUEIJAO\n 09 - DESODORANTE\n 10 - ACHOCOLATADO\n ----------------------------------------------------\n Digite o Código do Produto: "))
    if produtos > 10:
      print(" Código Inexistente")
      print("----------------------------------------------------")
      continue
    elif produtos == 0:
      print("-------- Obrigado por visitar nosso mercado ---------")
      break
    else:
      pass
      qtd_de_produtos = int(input(" Qual a quantidade? "))
      print("----------------------------------------------------")
      estoque = qtd_estoque[produtos] - qtd_de_produtos

      # ATT DO ESTOQUE DE PRODUTOS 
      if qtd_de_produtos > qtd_estoque[produtos]:
        print('Temos no momento apenas: ', 
   qtd_estoque[produtos],"Produtos.")
        print("----------------------------------------------------")
        continue
      else:
        pass
        qtd_estoque[produtos] = estoque

        # ESTOQUE ATUALIZADO
        print("--------------- Estoque Atualizado ---------------")
        print("----------------------------------------------------")
        print(' Quantidade de Biscoito:',qtd_estoque[1],'\n','Quantidade de Salgadinho:',qtd_estoque[2],'\n','Quantidade de Sorvete:',qtd_estoque[3],'\n','Quantidade de Escova:',qtd_estoque[4],'\n','Quantidade de Iogurte:',qtd_estoque[5],'\n','Quantidade de Refrigerante:',qtd_estoque[6],'\n','Quantidade de Sabonete:',qtd_estoque[7],'\n','Quantidade de Requeijao:',qtd_estoque[8],'\n','Quantidade de Desodorante:',qtd_estoque[9],'\n','Quantidade de Achocolatado:',qtd_estoque[10])
  