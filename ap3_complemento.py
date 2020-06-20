from random import choice


def boneco(erros):
    if erros == 0:
        print('--------------')
        print('|            |')
        print('|             ')
        print('|             ')
        print('|             ')
        print('|             ')
        print('|')
    elif erros == 1:
        print('--------------')
        print('|            |')
        print('|            O')
        print('|             ')
        print('|             ')
        print('|             ')
        print('|             ')
        print('|')
    elif erros == 2:
        print('--------------')
        print('|            |')
        print('|            O')
        print('|            |')
        print('|             ')
        print('|             ')
        print('|             ')
        print('|')
    elif erros == 3:
        print('--------------')
        print('|            |')
        print('|            O')
        print('|           -|')
        print('|             ')
        print('|             ')
        print('|             ')
        print('|')
    elif erros == 4:
        print('--------------')
        print('|            |')
        print('|            O')
        print('|           -|-')
        print('|             ')
        print('|             ')
        print('|             ')
        print('|')
    elif erros == 5:
        print('--------------')
        print('|            |')
        print('|            O')
        print('|           -|-')
        print('|           / ')
        print('|             ')
        print('|             ')
        print('|')
    elif erros == 6:
        print('--------------')
        print('|            |')
        print('|            O')
        print('|           -|-')
        print('|           / \\')
        print('|             ')
        print('|          Perdeu!')
        print('|')


def selecionar_palavra():
    """selecionar a palavra, mostrar quantas letras tem e a dica

    :return:
    palavra = a palavra escolhida aleatoriamente
    dica = a dica da palavra escolhida
    """
    try:
        palavras = open('palavra_forca.txt', 'r')
    except:
        palavras = open('palavra_forca.txt', 'x+')
        palavras.write("""\"\"\"
Não modificar esse texto
adicionar palavras como no exemplo
        
'palavra': 'dica'
\"\"\"

exemplo: exemplo de dica""")
    dicionario = {}
    for a in palavras.readlines()[7:]:
        dicionario[a[0:a.find(':')]] = a[a.find(':') + 2:]
    palavras.close()
    escolha = []
    for a in dicionario.keys():
        escolha.append(a)
    palavra = choice(escolha)
    dica = dicionario[palavra]
    return palavra, dica
