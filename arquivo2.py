from operacoesbd import *
from metodos import *

conexao = criarConexao('127.0.0.1', 'root', 'G172680', 'ouvidoria')
escolha = 1
while escolha != 7:
    print(
        "\n|1| Listagem das Manifestações \n|2| Listagem de Manifestações por Tipo \n|3| Criar uma nova Manifestação\n|4| Exibir quantidade de manifestações \n|5| Pesquisar uma manifestação por código \n|6| Excluir uma Manifestação pelo Código \n|7| Sair do Sistema.")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        manifestacoes = listagem(conexao)
        if len(manifestacoes) > 0:
            for item in manifestacoes:
                print(item[0], "-", item[1])
        else:
            print("Não há manifestação")
    elif escolha == 2:
        print("\tDigite: \n|1| para reclamação \n|2| para sugestão \n|3| para elogio")
        opcao = int(input("Digite qual lista de manifestações deseja ver: "))
        listagemTipo(conexao,opcao)
    elif escolha == 3:
        print("\n|1| para reclamação \n|2| para sugestão \n|3| para elogio")
        tipo = int(input("Qual tipo de manifestação deseja adicionar? "))
        descricao = input("Descreva sua manifestação: ")
        autor = input("Autor da manifestação: ")
        adicionar(conexao, tipo, descricao, autor)
    elif escolha == 4:
        quantidade(conexao)
    elif escolha == 5:
        consultaCodigo(conexao)
    elif escolha == 6:
        codigoDelete = int(input("Qual o código da manifestação que deseja excluir? "))
        delete(conexao, codigoDelete)
    elif escolha != 7:
        print("ESCOLHA INVÁLIDA")

encerrarConexao(conexao)
