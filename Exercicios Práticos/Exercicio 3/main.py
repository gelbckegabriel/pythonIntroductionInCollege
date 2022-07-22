print('Olá, seja bem-vindo a Gelbcke´s Feijoada!');  #identificador pessoal.

print('-----------------------------------------');

def volumeFeijoada(): # função para a seleção do volume da feijoada.
    print('Menu - Volume feijoada:');
    global volume;
    global valor;
    global valorVolume;
    try:
        volume = int(input('Digite a quantidade de feijoada que deseja (ml): '));
        if(volume < 300 or volume > 5000): # condição para quantidade mínima e máxima.
            print('O valor citado não é aceito. A quantidade mínima é de 300ml e a máxima é de 5000ml !');
            print(' ');
            volumeFeijoada();
        else: # condição para quando o valor está correto.
            valor = float(volume * 0.08);
            print(' ');
            valorVolume = valor;
            print('O valor da quantidade da feijoada é de R$ %.2f !' % valor)

    except ValueError: # except para quando o digito não é um número
        print('O valor digitado precisa ser um número!')
        print(' ');
        volumeFeijoada();

def opcaoFeijoada():
    global valor;
    global valorOpcao;
    print('Menu - Opção feijoada:');
    opcao = input('Digite a sua opção de feijoada: \n B- Básica = feijão + paiol + costelinha \n P- Premium = feijão + paiol + costelinha + partes de porco \n S- Suprema = feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon \n Entre com a letra desejada: ');
    if (opcao != 'B' and opcao != 'P' and opcao != 'S'):  # condicional para verificar a letra digitada pelo usuário.
        print('Código inválido, por gentileza digitar em letra maiuscula as letras da opção desejada !');
        print(' ');
        opcaoFeijoada();
    elif (opcao == 'B'):
        valor = valor * 1;
        valorOpcao = 1.0;
        print('O Valor com esta opção ficou de R$ %.2f !' % valor);
    elif (opcao == 'P'):
        valor = valor * 1.25;
        valorOpcao = 1.25;
        print('O Valor com esta opção ficou de R$ %.2f !' % valor);
    elif (opcao == 'S'):
        valor = valor * 1.50;
        valorOpcao = 1.50;
        print('O Valor com esta opção ficou de R$ %.2f !' % valor);

valorAcompanhamento = 0;  # tive que iniciar o valor com 0 fora da função, pois estava tendo problema de inicialização.

def acompanhamentoFeijoada():
    global valor;
    global valorAcompanhamento;
    print('Menu - Acompanhamento feijoada:');
    acompanhamento = int(input('Deseja mais algum acompanhamento na sua feijoada: \n 0 - Não desejo mais acompanhamentos (Encerrar pedido). \n 1 - 200g de Arroz. \n 2 - 150g de Farofa Especial. \n 3 - 100g de Couve Cozida. \n 4 - 1Unid. de Laranja Descascada. \n Resposta: '))
    if (acompanhamento == 0):
        print('Finalização de pedido!');
    elif (acompanhamento == 1):
        valor = valor + 5.00;
        valorAcompanhamento = valorAcompanhamento + 5.00;
        print('Adição de Arroz!');
        print(' ');
        acompanhamentoFeijoada();
    elif (acompanhamento == 2):
        valor = valor + 6.00;
        valorAcompanhamento = valorAcompanhamento + 6.00;
        print('Adição de Farofa Especial!');
        print(' ');
        acompanhamentoFeijoada();
    elif (acompanhamento == 3):
        valor = valor + 7.00;
        valorAcompanhamento = valorAcompanhamento + 7.00;
        print('Adição de Couve Cozida!');
        print(' ');
        acompanhamentoFeijoada();
    elif (acompanhamento == 4):
        valor = valor + 3.00;
        valorAcompanhamento = valorAcompanhamento + 3.00;
        print('Adição de Laranja Descascada!');
        print(' ');
        acompanhamentoFeijoada();

def soma():
    print('Menu - Finalização da Compra:');
    print('Descritivo:');
    print('Volume: R$%.2f.' % valorVolume);
    print('Opção: Volume * {}.'.format(valorOpcao));
    print('Acompanhamento: R$%.2f.' % valorAcompanhamento);
    print('O valor total da sua compra é de R$%.2f.' % valor, );

volumeFeijoada();
print('-----------------------------------------');
opcaoFeijoada();
print('-----------------------------------------');
acompanhamentoFeijoada();
print('-----------------------------------------');
soma();
