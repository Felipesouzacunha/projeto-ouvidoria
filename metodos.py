from operacoesbd import *

def listartudo(conexao):
    sqlListar = 'select * from ouvidoria'
    manifestacoes = listarBancoDados(conexao, sqlListar)
    return manifestacoes

def listarportipo(conexao, opcaodelistagem):
    if opcaodelistagem == 1:
        tipo = "'Reclamação'"
    elif opcaodelistagem == 2:
        tipo = "'Sugestão'"
    elif opcaodelistagem == 3:
        tipo = "'Elogio'"

    sqllistar = 'select * from ouvidoria where tipodocomentarios =' + tipo
    manifestacoes = listarBancoDados(conexao, sqllistar)
    return manifestacoes

def criarmanifestacao(conexao, titulo, comentario, nome, tipocomentario):
    sqlInsercao = 'insert into ouvidoria (titulo, comentario, nome, tipodocomentarios) values (%s,%s,%s,%s)'
    valores = [titulo, comentario, nome, tipocomentario]
    insertNoBancoDados(conexao,sqlInsercao,valores)

def pesquisarPorCodigo(conexao,ouvidoriacodigo):
    listaPorTipo = 'select * from ouvidoria where codigo = ' + ouvidoriacodigo
    manifestacao = listarBancoDados(conexao, listaPorTipo)
    return manifestacao

def contagemdemanifestacao(conexao):
    sqlcontagem = 'select count(*) from ouvidoria'
    resultado = listarBancoDados(conexao, sqlcontagem)
    return resultado

def checagemdemanifestcao(conexao, codigo):
    sqllistar = 'select count(*) from ouvidoria where codigo =' + codigo
    resultado = listarBancoDados(conexao, sqllistar)
    return resultado

def alterarmanifestacao(conexao, codigo, novotitulo, novadescricao):
    sqlalterar = 'update ouvidoria set titulo = %s, comentario = %s where codigo = %s'
    valores = [novotitulo, novadescricao, codigo]
    atualizarBancoDados(conexao, sqlalterar, valores)


def deletarManifestacaoPorCodigo(conexao,codigodelete):
    manifestacao = 'delete from ouvidoria where codigo = %s '
    dados = [codigodelete]
    excluirBancoDados(conexao, manifestacao, dados)
    return manifestacao
