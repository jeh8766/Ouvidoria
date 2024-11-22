from operacoesbd import *

def listagem(conexao):
    consultaListagem = 'select * from manifestacoes'
    manifestacoes = listarBancoDados(conexao, consultaListagem)
    return manifestacoes

def listagemTipo(conexao, opcao):
    if opcao == 1:
        consultaReclamacao = 'select * from manifestacoes where categoria="reclamacao"'
        reclamacoes = listarBancoDados(conexao, consultaReclamacao)
        if len(reclamacoes) > 0:
            for item in reclamacoes:
                print(item[0], "-", item[1], "-", item[2])
        else:
            print("Não há reclamação a ser exibida.")
    if opcao == 2:
        consultaSugestao = 'select * from manifestacoes where categoria="sugestao"'
        sugestoes = listarBancoDados(conexao, consultaSugestao)
        if len(sugestoes) > 0:
            for item in sugestoes:
                print(item[0], "-", item[1], "-", item[2])
        else:
            print("Não há sugestão a ser exibida.")
    if opcao == 3:
        consultaElogio = 'select * from manifestacoes where categoria="elogio"'
        elogios = listarBancoDados(conexao, consultaElogio)
        if len(elogios) > 0:
            for item in elogios:
                print(item[0], "-", item[1], "-", item[2])
        else:
            print("Não há sugestão a ser exibida.")


def adicionar(conexao, tipo, descricao, autor):
    if tipo == 1:
        categoria = "reclamacao"
    elif tipo == 2:
        categoria = "sugestao"
    elif tipo == 3:
        categoria = "elogio"
    consultaInsert = 'insert into manifestacoes(descricao,autor,categoria) values (%s,%s,%s)'
    valores = descricao, autor, categoria
    criarManifestacao = insertNoBancoDados(conexao, consultaInsert, valores)
    return criarManifestacao


def metodoQuantidade(conexao):
    quantidade = listarBancoDados(conexao, 'select count(*) from manifestacoes')
    return quantidade


def pesquisarCodigo(conexao,codigo):
    consultaCodigo = 'select * from manifestacoes where codigo=%s'
    valor= [codigo]
    pesquisaCodigo=listarBancoDados(conexao,consultaCodigo,valor)
    return pesquisaCodigo


def delete(conexao, codigoDelete):
    consultaDelete = 'delete from manifestacoes where codigo=%s'
    valorDelete = [codigoDelete]
    delete = excluirBancoDados(conexao, consultaDelete, valorDelete)
    return delete

