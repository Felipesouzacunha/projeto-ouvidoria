from operacoesbd import *

def listartudo(conexao):
    sqlListar = 'select * from ouvidoria'
    manifestacoes = listarBancoDados(conexao, sqlListar)
    print()
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
    valores = [titulo, comentario, nome, tipocomentario]
    insertNoBancoDados(conexao, sqlInsercao, valores)
