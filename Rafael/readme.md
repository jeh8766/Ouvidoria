# Sistema de Ouvidoria

Este é um sistema simples de **ouvidoria**, onde os usuários podem registrar e consultar manifestações, como **reclamações**, **elogios** e **sugestões**. Ele utiliza **Python** para a lógica e interage com um banco de dados MySQL para armazenar as informações.

## Funcionalidades

- **Adicionar manifestação**: Permite registrar uma manifestação do tipo **reclamação**, **elogio** ou **sugestão**.
- **Listar manifestações**: Exibe todas as manifestações registradas no sistema.
- **Filtrar manifestações por tipo**: Permite listar manifestações filtradas por tipo (reclamação, elogio ou sugestão).
- **Exibir quantidade de manifestações**: Mostra o total de manifestações registradas e a quantidade por tipo.
- **Pesquisar manifestação por código**: Permite pesquisar uma manifestação usando seu **ID**.
- **Excluir manifestação por código**: Exclui uma manifestação usando o **ID**.

## Pré-requisitos

1. **Python 3.x** instalado em sua máquina.  
   [Baixar Python](https://www.python.org/downloads/)

2. **Biblioteca MySQL Connector** para Python:
   Execute o seguinte comando para instalar a biblioteca necessária:

   ```bash
   pip install mysql-connector-python

