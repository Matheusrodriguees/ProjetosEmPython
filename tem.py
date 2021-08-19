arquivo = 'test.py'

with open(arquivo) as linhas:
    for linha in linhas:
        #Quebra a linha pelo delimitador
        conteudo = linha.split(";")
        # Atribuindo a primeira parte ANTES de ;
        nome = conteudo[0]
        # Atribuindo a segunda parte APOS ;
        numero = conteudo[1]
        # Imprimindo NOME
        print(f'Nome: {nome}')
        # Imprimindo NUMERO
        print(f'Numero: {numero}')