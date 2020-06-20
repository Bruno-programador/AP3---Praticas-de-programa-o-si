from ap3_complemento import boneco, selecionar_palavra


def jogo():
    erros = 0
    selecionar_palavra()
    situacao = []
    for a in palavra:
        if a == ' ':
            situacao.append('-')
        elif a == '-':
            situacao.append('-')
        else:
            situacao.append('_')
    while True:
        boneco(erros)
        print(situacao)
        print(dica)
        # pedir uma letra
        while True:
            resposta = input('Selecione uma letra:')
            if len(resposta) == 1:
                break
            else:
                print('apenas uma letra')

        #verificar se a resposta esta certa, se estiver mostra na situacao
        for a in range(len(palavra)):
            if resposta == palavra[a]:
                situacao[a] = resposta

        #verificar se a resposta esta errada, se estiver adiciona 1 em erros
        if resposta not in palavra:
            erros += 1

        #verifica se perdeu ou ganhou
        if erros == 6:
            boneco(erros)
            return False
        if '_' not in situacao:
            print(situacao)
            print('VITORIA')
            return True
        print('\n\n')


ganhou = 0
perdeu = 0
nome = input('Nome do jogador:')
while True:
    palavra, dica = selecionar_palavra()
    if jogo():
        ganhou += 1
    else:
        perdeu += 1
    while True:
        continuar = input('Deseja continuar jogando: S/N')
        if continuar in 'SsNn' and len(continuar) == 1:
            break
        else:
            print('resposta invalida')
    if continuar in 'Nn':
        print(f'{nome} jogou {ganhou + perdeu} partidas, ganhou {ganhou} e perdeu {perdeu}')
        break
