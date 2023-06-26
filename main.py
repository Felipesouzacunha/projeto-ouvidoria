from operacoesbd import *
from metodos import *

conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria')
manifestacao = []
tipodocomentarios = ''
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
            print('Não há manifestações cadastradas!')
        else:
            for manifestacao in manifestacoes:
                print(
                    f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - Descrição da '
                    f'manifestação: {manifestacao[3]} - Tipo da manifestação: {manifestacao[4]}')

    elif opcao == 2:
        print('Listagem de manifestação por tipo: ')
        opcaodelistagem = int(input('1)Reclamação\n2)Sugestão\n3)Elogio\nEscolha a opção desejada: '))
        manifestacoes = listarportipo(conexao, opcaodelistagem)
        if opcaodelistagem == 1:
            if len(manifestacoes) > 0:
                print('Listagem de Reclamação: ')
                for manifestacao in manifestacoes:
                    print(f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - Descri'
                          f'ção da manifestação: {manifestacao[3]}')
            else:
                print('Não há Elogios cadastrados!')

        elif opcaodelistagem == 2:
            manifestacoes = listarportipo(conexao, opcaodelistagem)
            if len(manifestacoes) > 0:
                print('Listagem de Sugestões: ')
                for manifestacao in manifestacoes:
                    print(f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - Descri'
                          f'ção da manifestação: {manifestacao[3]}')
            else:
                print('Não há Sugestões cadastradas!')

        elif opcaodelistagem == 3:
            manifestacoes = listarportipo(conexao, opcaodelistagem)
            if len(manifestacoes) > 0:
                print('Listagem de Elogio: ')
                for manifestacao in manifestacoes:
                    print(f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - Descri'
                          f'ção da manifestação: {manifestacao[3]}')
            else:
                print()
                print('Não há Reclamações cadastradas! ')

    elif opcao == 3:
        print()
        print("3) Criar uma nova Manifestação")
        print()
        print("Escolha o tipo de Manifestação:")
        print("1)Reclamações 2)Sugestões 3)Elogios ")
        opcaotipo = 0
        while opcaotipo != 1 and opcaotipo != 2 and opcaotipo != 3:
            opcaotipo = int(input("Digite o seu tipo de manifestação: "))
            if opcaotipo == 1:
                tipodocomentarios = "Reclamação"
            elif opcaotipo == 2:
                tipodocomentarios = "Sugestão"
            elif opcaotipo == 3:
                tipodocomentarios = "Elogio"
            else:
                print("Opção invalida")

        titulo = input("Digite o título: ")
        comentario = input("Digite o seu comentario: ")
        nome = input("Digite o seu nome: ")
        criarmanifestacao(conexao, titulo, comentario, nome, tipodocomentarios)
        print("Comentario cadastrado com sucesso!")

    elif opcao == 4:
        resultado= contagemdemanifestacao(conexao)
        if len(resultado) > 0:
            print(f'Há {resultado[0][0]} manifestações cadastradas')
        else:
            print('Não há nenhum item na lista!')

    elif opcao == 5:
        print()
        ouvidoriacodigo = input("Digite o codigo da Manifestação: ")
        manifestacao = pesquisarPorCodigo(conexao, ouvidoriacodigo)
        if len(manifestacao) == 0:
            print("Codigo invalido")
        else:
            for elementos in manifestacao:
                print(f'Nome: {elementos[1]} - Titulo: {elementos[2]} - Descrição da manifestação: {elementos[3]} - Tipo da manifestação: {elementos[4]}')

    elif opcao == 6:
        codigo = input('Digite o codigo de manifestação que deseja alterar: ')
        print()
        resultado = checagemdemanifestcao(conexao, codigo)
        if resultado[0][0] == 0:
            print('Manifetação não existente!')
        else:
            novotitulo = input('Novo titulo: ')
            novadescricao = input('Nova descrição: ')
            alterarmanifestacao(conexao, codigo, novotitulo, novadescricao)
            print('Manifestação atualizada com sucesso! ')
            
    elif opcao == 7:
        manifestacoes = listartudo(conexao)
        if len(manifestacoes) == 0:
            print('Não há manifestações cadastradas!')
        else:
            for manifestacao in manifestacoes:
                print(
                    f'Codigo: {manifestacao[0]} - Nome: {manifestacao[1]} - Titulo: {manifestacao[2]} - Descrição da '
                    f'manifestação: {manifestacao[3]} - Tipo da manifestação: {manifestacao[4]}')
                
            print()
            ouvidoriacodigo = input("Digite o codigo da Manifestação a ser deletada: ")
            resultado = checagemdemanifestcao(conexao, ouvidoriacodigo)
            if resultado[0][0] == 0:
                print('Manifetação não existente!')
            else:
                manisfestacao = deletarManifestacaoPorCodigo(conexao,ouvidoriacodigo)
                print("Manifestação deletada com sucesso")        
            
    elif opcao == 8:
        print()
        print('Obrigrado por usar a nossa ouvidoria!')
        print('Saindo do sistema...')
        
    else:
        print('Opção inválida!')

encerrarBancoDados(conexao)
