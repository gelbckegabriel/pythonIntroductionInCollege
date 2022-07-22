print('Olá, seja bem-vindo a pizzaria do Gelbcke!');  #identificador pessoal.
print(' ');

#cardápio.
print('--------------------- Cardápio ---------------------');
print('| Código | Descrição  | Pizza Média | Pizza Grande |');
print('|   21   | Napolitana |  R$ 20,00   |   R$ 26,00   |');
print('|   22   | Margherita |  R$ 20,00   |   R$ 26,00   |');
print('|   23   | Calabresa  |  R$ 25,00   |   R$ 32,50   |');
print('|   24   | Toscana    |  R$ 30,00   |   R$ 39,00   |');
print('|   25   | Portuguesa |  R$ 30,00   |   R$ 39,00   |');
print('----------------------------------------------------');
valor = 0

while (True):
    tamanho = input('Qual o tamanho da pizza que deseja (M/G)? ');  # escolher tamanho da pizza.
    codigo = int(input('Digite o código do sabor que deseja: '));  # escolher sabor da pizza.

    # condicional para pedido.
    # pizzas médias.
    if ((tamanho == 'M') and (codigo == 21)):
        print('Você pediu uma pizza "Napolitana"');
        valor = valor + 20.00
    elif ((tamanho == 'M') and (codigo == 22)):
        print('Você pediu uma pizza "Margherita"');
        valor = valor + 20.00
    elif ((tamanho == 'M') and (codigo == 23)):
        print('Você pediu uma pizza "Calabresa"');
        valor = valor + 25.00
    elif ((tamanho == 'M') and (codigo == 24)):
        print('Você pediu uma pizza "Toscana"');
        valor = valor + 30.00
    elif ((tamanho == 'M') and (codigo == 25)):
        print('Você pediu uma pizza "Portuguesa"');
        valor = valor + 30.00
    # pizzas grandes.
    elif ((tamanho == 'G') and (codigo == 21)):
        print('Você pediu uma pizza "Napolitana"');
        valor = valor + 26.00
    elif ((tamanho == 'G') and (codigo == 22)):
        print('Você pediu uma pizza "Margherita"');
        valor = valor + 26.00
    elif ((tamanho == 'G') and (codigo == 23)):
        print('Você pediu uma pizza "Calabresa"');
        valor = valor + 32.50
    elif ((tamanho == 'G') and (codigo == 24)):
        print('Você pediu uma pizza "Toscana"');
        valor = valor + 39.00
    elif ((tamanho == 'G') and (codigo == 25)):
        print('Você pediu uma pizza "Portuguesa"');
        valor = valor + 39.00
    # caso dígito esteja incorreto.
    else:
        print('Opção inválida!');
        print('---------------');
        continue;

    # pedido adicional.
    print('--------------------------------');
    print('Deseja pedir mais alguma coisa? ');
    print('0 - Não');
    print('1 - Sim');
    adicional = int(input('Resposta: '));

    # condicional para recusa ou realização de novo pedido.
    if (adicional == 0):
        print('--------------------------------');
        break;
    else:
        print('--------------------------------');
        continue;

print('O valor total da sua compra é de R$%.2f' % valor)
