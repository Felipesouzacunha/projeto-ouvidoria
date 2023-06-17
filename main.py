from operacoesbd import *
from metodos import *

conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria')
manifestacao = []
tipo = ''
opcao = 0
while opcao != 8:
    print()
    print(f'1) Listagem das Manifestações  {"2) Listagem de Manifestações por Tipo":^62}')
    print(f'3) Criar uma nova Manifestação  {"4) Exibir quantidade de manifestações": ^60}')
    print(f'5) Pesquisar uma manifestação por código {"6) Alterar o Título e Descrição de uma Manifestação": ^55} ')
    print(f'7) Excluir uma Manifestação pelo Código {" 8) Sair do Sistema.": ^25}')
    opcao = int(input('Qual a sua opção? '))

    if opcao == 1:
        manifestacoes = listartudo(conexao)
        if len(manifestacoes) == 0:
            print('Não há manifestações!')
        else:
            for manifestacao in manifestacoes:
                print(
                    f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - Descrição da manifestação: {manifestacao[3]} - Tipo da manifestação: {manifestacao[4]}')

    elif opcao == 2:
        print('Listagem de manifestação por tipo: ')
        opcaodelistagem = int(input('1)Elogios\n2)Sugestão\n3)Reclamações\nEscolha a opção desejada: '))
        manifestacoes = listarportipo(conexao, opcaodelistagem)
        if opcaodelistagem == 1:
            if len(manifestacoes) > 0:
                print('Listagem de Elogios: ')
                for manifestacao in manifestacoes:
                    print(f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - Descrição da manifestação: {manifestacao[3]}')
            else:
                print('Não há Elogios!')

        elif opcaodelistagem == 2:
            manifestacoes = listarportipo(conexao, opcaodelistagem)
            if len(manifestacoes) > 0:
                print('Listagem de Sugestões: ')
                for manifestacao in manifestacoes:
                    print(f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - Descrição da manifestação: {manifestacao[3]}')
            else:
                print('Não há Sugestões!')

        elif opcaodelistagem == 3:
            manifestacoes = listarportipo(conexao, opcaodelistagem)
            if len(manifestacoes) > 0:
                print('Listagem de Reclamações: ')
                for manifestacao in manifestacoes:
                    print(f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - Descrição da manifestação: {manifestacao[3]}')
            else:
                print()
                print('Não há Reclamações! ')

    elif opcao != 8:
        print('Opção inválida!')

print()
print('Obrigrado por usar a nossa ouvidoria!')
print('Saindo do sistema...')
encerrarBancoDados(conexao)
