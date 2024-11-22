from operacoesbd import *
from metodos import *

conexao = criarConexao('localhost', 'root', '172a820B.', 'ouvidoria_caseira')
menu_principal = 0

while menu_principal != 7:
    print("\tMenu Ouvidoria\n",
          "1. Adicionar nova manifestação\n",
          "2. Listar Manifestação\n",
          "3. Listar Manifestação por Tipo\n",
          "4. Quantidade de Manifestação\n",
          "5. Pesquisar Manifestação por Código\n",
          "6. Excluir por Código\n",
          "7. Encerrar Sistema")
    menu_principal = int(input("(1-7): "))

    if menu_principal == 1:
        adicionar_manifestacao(conexao)
        
    if menu_principal == 2:
        listar_manifestacao(conexao)
        
    if menu_principal == 3:
        listar_manifestacao_pTipo(conexao)
        
    if menu_principal == 4:
        exibir_quantidade(conexao)
        
    if menu_principal == 5:
        pesquisar_pCodigo(conexao)

    if menu_principal == 6:
        excluir_pCodigo(conexao)

    if menu_principal != 7:
        print("Valor escolhido inválido. Tente Novamente!")

print("Finalizado com Sucesso, até!")
encerrarConexao(conexao)