ocorrencias = []
opcao = 1

while opcao != 6:
    print()
    print('-=-'*42)
    print('[1]Listar ocorrências [2]Adicionar ocorrência [3]Remover ocorrência [4]Alterar ocorrência [5]Pesquisar ocorrência [6]Sair')
    opcao = int(input('Qual a opção desejada? '))

    if opcao == 1:
        if len(ocorrencias) == 0:
            print()
            print('Não temos nenhuma ocorrência no momento!')
        else:
            print()
            for i in range(len(ocorrencias)):
                print(i+1, ocorrencias[i])

    elif opcao == 2:
        novaOcorrencia = str(input('Qual é a sua ocorrência? '))
        ocorrencias.append(novaOcorrencia)
        print('Ocorrência adicionada com sucesso!')

    elif opcao == 3:
        print()
        for i in range(len(ocorrencias)):
            print(i+1, ocorrencias[i])
        removerOcorrencia = int(input('Número da ocorrência que deseja remover: '))
        ocorrencias.pop(removerOcorrencia-1)
        print()
        print('Ocorrência Removida com sucesso!')

    elif opcao == 4:
        if len(ocorrencias) > 0:
            for i in range(len(ocorrencias)):
                print(i + 1, ocorrencias[i])
            alterarocorrencia = int(input('Qual ocorrência deseja alterar? '))
            alterarocorrencia -= 1
            quantidadedeItens = len(ocorrencias)
            if alterarocorrencia not in range(0, quantidadedeItens):
                print('Não existe esta ocorrência. Tente novamente!')
            else:
                ocorrencias[alterarocorrencia] = str(input('Digite a nova ocorrência: '))
                print('Nova ocorrênncia salva!')
        else:
            print('Não há ocorrências para alterar!')

    elif opcao == 5:
        numerodaocorrencia = int(input('Número da ocorrência que deseja pesquisar: '))
        print('Pesquisando...')
        numerodaocorrencia -= 1
        quantidadedeItens = len(ocorrencias)
        print()
        if numerodaocorrencia not in range(0,quantidadedeItens):
            print('Não há esta ocorrência!')
        else:
            print(ocorrencias[numerodaocorrencia])

    elif opcao != 6:
        print('Opção inválida!')

print('=='*42)
print()
print('Obrigado por usar nosso sistema!')
