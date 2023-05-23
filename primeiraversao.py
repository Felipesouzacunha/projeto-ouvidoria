ocorrencias = ['dfhs', 'asadad']
opcao = 1

while opcao != 5:
    print()
    print('-=-'*25)
    print('[1]Listar ocorrências [2]Adicionar [3]Remover [4]Pesquisar [5]Sair')
    opcao = int(input('Qual a opção desejada? '))

    if opcao == 1:
        if len(ocorrencias) == 0:
            print()
            print('Não temos nenhuma ocorrência no momento! ')
        else:
            print()
            for i in range(len(ocorrencias)):
                print(i+1, ocorrencias[i])

    elif opcao == 2:
        novaOcorrencia = str(input('Qual a a sua ocorrência? '))
        ocorrencias.append(novaOcorrencia)
        print('Ocorrência adicionada com sucesso!')

    elif opcao == 3:
        print()
        for i in range(len(ocorrencias)):
            print(i+1, ocorrencias[i])
        removerOcorrencia = int(input('Número da ocrrência que deseja remover: '))
        ocorrencias.pop(removerOcorrencia-1)
        print()
        print('Ocorrência Removida com sucesso!')

    elif opcao == 4:
        numerodaocorrencia = int(input('Número da ocorrencia que deseja pesquisar: '))
        print('Pesquisando...')
        print()
        print(ocorrencias[numerodaocorrencia-1])
    elif opcao != 5:
        print('Opção inválida!')

print('=='*25)
print()
print('Saindo do programa!')
