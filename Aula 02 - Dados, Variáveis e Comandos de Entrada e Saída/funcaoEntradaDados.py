# função input.
nome = input('Qual o seu nome? ')
print('Seu nome é "{}". Bem-vindo!' .format(nome))

# input sempre retornará string. será necessário convertê-lo.
nota = float(input('Qual foi a sua nota nesta matéria? '))
print('Você tirou %.2f em Algoritmos' % nota)

# EXERCICIO: Receba dois números do usuário e faça a soma deles.
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
print('A som dos dois valores é: ', valor1+valor2)