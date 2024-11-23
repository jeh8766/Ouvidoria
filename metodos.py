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

def adicionar_manifestacao(conexao):

    status_manifestacoes = ['Reclamação', 'Elogio', 'Sugestão']

    while True: #segundo menu para escolha de manifestação e sua adição, interrompe apenas por escolha.
        sql = 'insert into manifestacoes(autor, descricao, categoria) values(%s,%s,%s)'
        nome_cliente = 'anônimo'
        mensagem = ''

        print("\tQual o tipo de manifestação que deseja fazer?\n",
              "1. Reclamação\n",
              "2. Elogio\n",
              "3. Sugestão\n",
              "4. Cancelar")
        menu_secundario = int(input("Qual deseja escolher?\n"))

        if menu_secundario == 4:
            print("Operação cancelada")
            return
        if menu_secundario not in [1,2,3]:
            print("Opção escolhida inválida. Tente novamente")
            continue

        print("Deseja se identificar nessa manifestação?\n",
              "1. Sim\n",
              "2. Não")
        anonimato = int(input("(1-2): "))

        if anonimato not in [1,2]:
            print("Opção escolhida inválida. Tente novamente")
            continue

        nome_cliente = input("Digite o seu nome: ") if anonimato == 1 else "anônimo"

        tipo = status_manifestacoes[menu_secundario-1]
        mensagem = input("Digite sua Mensagem: ")

        valores = [nome_cliente, mensagem, tipo]

        insertNoBancoDados(conexao,sql,valores)
        print("Manifestação Cadastrada com Sucesso!")
        return

