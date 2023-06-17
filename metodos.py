from operacoesbd import *

def listartudo(conexao):
    sqlListar = 'select * from manifestacao'
    manifestacoes = listarBancoDados(conexao, sqlListar)
    print()
    return manifestacoes

def listarportipo(conexao, opcaodelistagem):
    if opcaodelistagem == 1:
        sqlListar = "select * from manifestacao where tipo = 'Elogio'"
        manifestacoes = listarBancoDados(conexao, sqlListar)
        return manifestacoes

    if opcaodelistagem == 2:
        sqllistar = "select * from manifestacao where tipo = 'Sugestão'"
        manifestacoes = listarBancoDados(conexao, sqllistar)
        return manifestacoes

    if opcaodelistagem == 3:
        sqllistar = "select * from manifestacao where tipo = 'Reclamação'"
        manifestacoes = listarBancoDados(conexao, sqllistar)
        return manifestacoes