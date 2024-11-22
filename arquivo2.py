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
        criarManifestacao=adicionar(conexao, tipo, descricao, autor)
        if criarManifestacao > 0:
            print("MANIFESTAÇÃO CRIADA COM SUCESSO.")
    elif escolha == 4:
        quantidade=metodoQuantidade(conexao)
        if len(quantidade) > 0:
            print("Atualmente temos", quantidade[0][0], "manifestações")
        else:
            print("Não há manifestações no momento!")
    elif escolha == 5:
        codigo=int(input("Digite o código da manifestação: "))
        pesquisa=pesquisarCodigo(conexao,codigo)
        if len(pesquisa)>0:
            print(pesquisa[0][1],"-",pesquisa[0][2])
        else:
            print("Não há manifestação com esse código")
    elif escolha == 6:
        codigoDelete = int(input("Qual o código da manifestação que deseja excluir? "))
        deletar=delete(conexao, codigoDelete)
        if deletar > 0:
            print("MANIFESTAÇÃO EXCLUÍDA COM SUCESSO.")
        else:
            print("NÃO HÁ MANIFESTAÇÃO COM ESSE CÓDIGO.")
    elif escolha != 7:
        print("ESCOLHA INVÁLIDA")

encerrarConexao(conexao)
