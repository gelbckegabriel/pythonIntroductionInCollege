print('Olá, seja bem-vindo a loja do Gelbcke!');  #identificador pessoal.
print('--------------------------------------')
valor = float(input('Digite o valor do produto que deseja: R$'));  #input de valor do produto.
quantidade = int(input('Digite a quantidade que deseja: '));  #input da quantidade do produto.

print('--------------------------------------')

valorTotal = float(valor * quantidade);  #cálculo sem desconto.
print('O valor total da compra foi: R$ %.2f (sem desconto)' % valorTotal);

#desconto de 3%.
if (quantidade >= 5 and quantidade <= 19):
    desconto = float(valorTotal * 0.03);
    valorAtualizado = float(valorTotal - desconto);
    print('O valor com desconto foi de R$ {:.2f} (desconto de 3%)' .format(valorAtualizado));

#desconto de 6%.
elif (quantidade >= 20 and quantidade <= 99):
    desconto = float(valorTotal * 0.06);
    valorAtualizado = float(valorTotal - desconto);
    print('O valor com desconto foi de R$ {:.2f} (desconto de 6%)' .format(valorAtualizado));

#desconto de 10%.
elif (quantidade >= 100):
    desconto = float(valorTotal * 0.1);
    valorAtualizado = float(valorTotal - desconto);
    print('O valor com desconto foi de R$ {:.2f} (desconto de 10%)' .format(valorAtualizado));

#desconto não se aplica.
else:
    print('O desconto não se aplica neste caso.');