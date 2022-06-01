while True:
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')

    if nome != senha:
        print('loguin efetuado')
        break
    else:
        print('Erro. A senha deve ser diferente do nome.')
