import metodo

usuarios = metodo.Usuario()

isTrue = True

nome = input('Digite seu nome e sobrenome para começarmos: ')
email = input('Agora digite seu e-mail: ')
usuarios.setNomeEmail(nome, email)

while isTrue:

    print('-' * 50)
    print(f'Olá, {nome}. Bem-vindo(a) à ouvidoria!\n')
    print('Menu:')
    print('1 - Cadastrar Ocorrências')
    print('2 - Listar Ocorrências')
    print('3 - Apagar Ocorrências')
    print('4 - Sair')
    print('-' * 50)
    a = input('Digite o serviço desejado: ')

    if (a == '1'):
        print('Cadastrar:')
        print('1 - Reclamação\n2 - Elogio\n3 - Sugestão')
        b = input()

        if (b == '1'):
            c = input('Ocorrência: ')
            usuarios.addOcorrencia(c, 'reclamacao')
            print('Ocorrência salva. Entraremos em contato em breve.')
            print('')

        elif (b == '2'):
            c = input('Ocorrência: ')
            usuarios.addOcorrencia(c, 'elogio')
            print('Ocorrência salva. Entraremos em contato em breve.')
            print('')
        
        elif (b == '3'):
            c = input('Ocorrência: ')
            usuarios.addOcorrencia(c, 'sugestao')
            print('Ocorrência salva. Entraremos em contato em breve.')
            print('')

        else:
            print('Digite uma opção válida')
            print('')



    elif (a == '2'):
        print('Digite a ocorrência que deseja listar:\n2')
        print('1 - Reclamações')
        print('2 - Elogios')
        print('3 - Sugestões')
        d = input()

        if (d == '1'):
            print('Reclamações cadastradas: ')
            usuarios.getOcorrencias('reclamacao')
            print('')
        
        elif (d == '2'):
            print('Elogios cadastrados: ')
            usuarios.getOcorrencias('elogio')
            print('')
    
        elif (d == '3'):
            print('Sugestões cadastradas: ')
            usuarios.getOcorrencias('sugestao')
            print('')



    elif (a == '3'):
        print('Digite a ocorrência que deseja apagar:\n2')
        print('1 - Reclamações')
        print('2 - Elogios')
        print('3 - Sugestões')
        print('4 - Tudo')
        apagar = input()

        if (apagar == '1'):
            usuarios.getOcorrencias('reclamacao')
            id = input('Qual reclamação deseja apagar? ')
            usuarios.deleteOneOcorrencia(id)
            print('Reclamação apagada.\n')

        elif  (apagar == '2'):
            usuarios.getOcorrencias('elogio')
            id = input('Qual elogio deseja apagar? ')
            usuarios.deleteOneOcorrencia(id)
            print('Elogio apagado.\n')

        elif (apagar == '3'):
            usuarios.getOcorrencias('sugestao')
            id = input('Qual sugestão deseja apagar? ')
            usuarios.deleteOneOcorrencia(id)
            print('Sugestão apagado.\n')

        elif (apagar == '4'):
            apagartudo = input('Deseja realmente apagar tudo? ')
            if (apagartudo == 'Sim' or apagartudo == 'sim'):
                usuarios.deleteAll()
                print('Ocorrências apagadas.\n')
            if (apagartudo == 'Não' or apagartudo == 'não'):
                continue


    else:
        isTrue = False
        usuarios.quit()
        print('Agradecemos por utilizar nossa ouvidoria.')
        print('Saindo...')


