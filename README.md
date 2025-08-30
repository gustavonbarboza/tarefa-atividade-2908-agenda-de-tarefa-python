# ⚙️ Gerenciador de Tarefas em Linha de Comando ⚙️

Um sistema simples e eficiente para gerenciar suas tarefas diretamente do terminal, construído com Python e SQLite. Este projeto foi desenvolvido com uma arquitetura modular, onde cada funcionalidade principal reside em seu próprio arquivo, tornando o código limpo, organizado e fácil de estender.

## ✨ Funcionalidades Principais

* **✔️ Adicionar Tarefas:** Crie novas tarefas com título, descrição, datas de início e fim, tipo e situação inicial.
* **✔️ Visualizar Lista Completa:** Veja todas as suas tarefas em uma tabela organizada, com as mais recentes aparecendo primeiro.
* **✔️ Busca Inteligente:** Procure por tarefas específicas usando palavras-chave que correspondam ao título ou à descrição. A busca não diferencia maiúsculas/minúsculas.
* **✔️ Concluir Tarefas:** Marque tarefas que estavam pendentes como "Feitas" de forma interativa.
* **✔️ Limpeza Segura:** Exclua em massa todas as tarefas que já foram marcadas como pendentes, com um passo de confirmação para evitar acidentes.
* **✔️ Interface de Menu:** Todas as funcionalidades são acessíveis através de um menu principal interativo e fácil de usar.
* **✔️ Persistência de Dados:** Suas tarefas são salvas em um banco de dados SQLite (`gerenciador_tarefas.db`), garantindo que os dados não sejam perdidos ao fechar o programa.

## 🔧 Tecnologias Utilizadas

* **Python 3:** Linguagem principal do projeto.
* **SQLite 3:** Banco de dados relacional embarcado, utilizado através da biblioteca padrão `sqlite3` do Python.

## 📂 Estrutura do Projeto

O projeto foi organizado de forma modular para promover a clareza e a separação de responsabilidades:

```
.
├── cria_banco.py                 # Script para criar o banco de dados e a tabela (setup inicial).
├── inserir_nova_tarefa.py        # Módulo para adicionar uma nova tarefa.
├── visualizar_tarefas.py         # Módulo para listar todas as tarefas.
├── buscar_tarefas.py             # Módulo para a funcionalidade de busca.
├── atualizar_tarefa_status.py    # Módulo para marcar uma tarefa como concluída.
├── deletar_tarefas_pendentes.py  # Módulo para excluir tarefas pendentes.
├── main.py                       # Ponto de entrada principal, com o menu interativo.
└── gerenciador_tarefas.db        # Arquivo do banco de dados (criado após a primeira execução).
```

## 🚀 Como Usar

Para executar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

Você precisa ter o **Python 3** instalado em seu sistema. Para verificar se você o tem, abra seu terminal e digite:

```sh
python3 --version
```

Se não estiver instalado, você pode baixá-lo em [python.org](https://www.python.org/).

### Passos para Execução

**Clone ou baixe o projeto:**  
Salve todos os arquivos `.py` em uma única pasta em seu computador.

**Navegue até a pasta do projeto:**  
Use o comando `cd` no seu terminal para entrar na pasta onde você salvou os arquivos.

```sh
cd caminho/para/a/pasta/do/projeto
```

**Configure o Banco de Dados (Apenas na primeira vez):**  
Antes de usar o menu principal, você precisa criar o arquivo