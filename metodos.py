from operacoesbd import *

def listartudo(conexao):
    sqlListar = 'select * from ouvidoria'
    manifestacoes = listarBancoDados(conexao, sqlListar)
    return manifestacoes

def listarportipo(conexao, opcaodelistagem):
    if opcaodelistagem == 1:
        sqlListar = "select * from ouvidoria where tipodocomentarios = 'Reclamação'"
        manifestacoes = listarBancoDados(conexao, sqlListar)
        return manifestacoes

    if opcaodelistagem == 2:
        sqllistar = "select * from ouvidoria where tipodocomentarios = 'Sugestão'"
        manifestacoes = listarBancoDados(conexao, sqllistar)
        return manifestacoes

    if opcaodelistagem == 3:
        sqllistar = "select * from ouvidoria where tipodocomentarios = 'Elogio'"
        manifestacoes = listarBancoDados(conexao, sqllistar)
        return manifestacoes

def criarmanifestacao(conexao, titulo, comentario, nome, tipocomentario):
    sqlInsercao = 'insert into ouvidoria (titulo, comentario, nome, tipodocomentarios) values (%s,%s,%s,%s)'

def pesquisarPorCodigo(conexao,ouvidoriacodigo):
    listaPorTipo = 'select * from ouvidoria where codigo = ' + ouvidoriacodigo
    manifestacao = listarBancoDados(conexao, listaPorTipo)

    valores = [titulo, comentario, nome, tipocomentario]
    insertNoBancoDados(conexao, sqlInsercao, valores)

def contagemdemanifestacao(conexao):
    sqlcontagem = 'select count (*) from ouvidoria '
    resultado = listarBancoDados(conexao, sqlcontagem)
    return resultado

def alterarmanifestacao(conexao, codigo, novotitulo, novadescricao):
    sqlalterar = 'update ouvidoria set titulo = %s, descricao = %s where codigo = %s'
    valores = [novotitulo, novadescricao, codigo]
    atualizarBancoDados(conexao,sqlalterar, valores)
