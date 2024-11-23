from operacoesbd import *

def adicionar_manifestacao(conexao):

    status_manifestacoes = ['Reclamação', 'Elogio', 'Sugestão']

    while True: #segundo menu para escolha de manifestação e sua adição, interrompe apenas por escolha.
        sql = 'insert into manifestacao(autor, descricao, categoria) values(%s,%s,%s)'
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

def listar_manifestacao(conexao):

    sql = ('select id, tipo, nome_cliente, mensagem from manifestacao')
    manifestacoes = listarBancoDados(conexao,sql)

    if not manifestacoes:
        print("Nenhuma manifestação cadastradas!")
    else:
        print('-' * 40)
        for manifestacao in manifestacoes:
            print('id =',manifestacao[0],'Tipo:',manifestacao[1],',Remetente:',manifestacao[2],'\nMensagem:',manifestacao[3])
            print('-' * 40)

def listar_manifestacao_pTipo(conexao):
    sql = ('select id, tipo, nome_cliente, mensagem from manifestacao where tipo = %s')
    status_manifestacoes = ['Reclamação', 'Elogio', 'Sugestão']

    while True:
        print("Escolha o tipo de Manifestação\n",
              '1. Reclamação\n',
              '2. Elogio\n',
              '3. Sugestão\n',
              '4. Cancelar Pesquisa por Tipo')
        menu_secundario = int(input('(1-4): '))

        if menu_secundario == 4:
            print("Pesquisa Cancelada")
            return

        if menu_secundario not in[1,2,3]:
            print("Opção escolhida inválida. Tente novamente")
            continue

        valor = [status_manifestacoes[menu_secundario-1]]
        manifestacoes = listarBancoDados(conexao, sql, valor)

        if not manifestacoes:
            print("Nenhuma Manifestação Encontrada!")
            return
        else:
            for manifestacao in manifestacoes:
                print('ID:',manifestacao[0],'Tipo:', manifestacao[1]+', Remetente:',manifestacao[2],'\nMensagem:', manifestacao[3])
                print('-' * 40)
            return

def exibir_quantidade(conexao):
    sql_todos = 'select count(*) from manifestacao'
    listagem_todos = listarBancoDados(conexao,sql_todos)
    quantidade_todos = listagem_todos[0][0]

    sql_tipo = 'select tipo, count(*) from manifestacao group by tipo'
    listagem_tipo = listarBancoDados(conexao, sql_tipo)
    print('-' * 40)
    print("Atualmente temos",quantidade_todos,"Manifestações cadastradas, sendo elas:")

    for contagem in listagem_tipo:
        print('Do tipo:',contagem[0],'a quantidade é:',contagem[1])
    print('-' * 40)

def pesquisar_pCodigo(conexao):
    sql = 'select id, tipo, nome_cliente, mensagem from manifestacao where id = %s'
    valor_pesquisa = [int(input("Qual o ID que deseja procurar?"))]
    manifestacao = listarBancoDados(conexao,sql,valor_pesquisa)


    if not manifestacao:
        print('Nenhuma Manifestação econtrado pelo ID fornecido')
        return

    print('-' * 40)
    print('ID:', manifestacao[0][0], 'Tipo:', manifestacao[0][1]+ ', Remetente:', manifestacao[0][2], '\nMensagem:', manifestacao[0][3])
    print('-' * 40)

def excluir_pCodigo(conexao):
    sql = 'delete from manifestacao where id = %s'
    valor = [int(input('Qual o ID da Manifestação que deseja remover? '))]

    resultado = excluirBancoDados(conexao,sql,valor)

    print("Removido com sucesso") if resultado > 0 else print("Nenhuma Manifestação encontrada pelo ID")