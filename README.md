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

1. **Abra o terminal e navegue até a pasta do projeto:**
   ```sh
   cd caminho/para/a/pasta/do/projeto
   ```

2. **Execute o sistema principal:**
   ```sh
   python3 main.py
   ```

## ⚠️ Primeira Execução

Na **primeira vez** que for utilizar o sistema, é necessário criar o banco de dados e a tabela de tarefas. Para isso, execute o seguinte comando no terminal **antes de rodar o main.py**:

```sh
python3 cria_banco.py
```

Esse comando irá gerar o arquivo `gerenciador_tarefas.db` na pasta do projeto.

Depois disso, basta rodar o sistema principal normalmente:

```sh
python3 main.py
```

A partir daí, você poderá utilizar todas as funcionalidades do gerenciador de tarefas pelo menu interativo.

---

## 📄 Licença

Este projeto está sob a licença MIT.

## 👤 Autor

Feito por [Gustavo Barboza & Tiago Geraldo].