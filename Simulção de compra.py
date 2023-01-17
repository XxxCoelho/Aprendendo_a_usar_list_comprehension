def Preco_total(lista):
    total = sum([float(valor[1]) for valor in lista])
    return total


Carrinho = []
print(""" Produtos da loja:
[1] = Brinquedo R$ 300.00
[2] = Ferramenta R$ 150.00
[3] = Camisa R$ 50.00
[4] = Bota R$ 100.00
[5] = Ver seu Carrinho
[6] = Preço total a pagar
[0] = Sair da loja""")
print()
while True:
    Pedidos = input('O que deseja comprar?')
    if Pedidos in '1':
        Carrinho.append(('Brinquedo', 300.00))
        print('Adicionado ao seu Carrinho')
    elif Pedidos in '2':
        Carrinho.append(('Ferramenta', 150.00))
        print('Adicionado ao seu Carrinho')
    elif Pedidos in '3':
        Carrinho.append(('Camisa', 50.00))
        print('Adicionado ao seu Carrinho')
    elif Pedidos in '4':
        Carrinho.append(('Bota', 100.00))
        print('Adicionado ao seu Carrinho')
    elif Pedidos in '5':
        print('Seus pedidos:')
        for pedidos in Carrinho:
            print(f'{pedidos[0]} R$ {pedidos[1]}')
    elif Pedidos in '0':
        break
    elif Pedidos in '6':
        Valor_total = Preco_total(Carrinho)
        print(f'Total a pagar das suas comprar: {Valor_total:.2f}')
    else:
        print('Digite o que gostaria de comprar:')
        continue
