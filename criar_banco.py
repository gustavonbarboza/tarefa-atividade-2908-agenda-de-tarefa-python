import sqlite3
from sqlite3 import Error

def criar_conexao():
    """
    Cria e retorna uma conexão com o banco de dados SQLite.
    O arquivo do banco será 'gerenciador_tarefas.db'.
    """
    conn = None
    try:
        conn = sqlite3.connect('gerenciador_tarefas.db')
        return conn
    except Error as e:
        print(f"Ocorreu um erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabela(conn):
    """
    Cria a tabela 'tarefas' no banco de dados se ela ainda não existir.
    Utiliza a conexão fornecida como argumento.
    """
    # Comando SQL para criar a tabela com todas as colunas necessárias
    sql_criar_tabela_tarefas = """
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        data_inicial TEXT NOT NULL,
        data_final TEXT NOT NULL,
        tipo TEXT,
        situacao INTEGER NOT NULL -- Usamos 0 para 'Não Feito' e 1 para 'Feito'
    );
    """
    try:
        # Cria um cursor, que é usado para executar comandos SQL
        cursor = conn.cursor()
        # Executa o comando SQL
        cursor.execute(sql_criar_tabela_tarefas)
        print("Tabela 'tarefas' criada com sucesso ou já existente.")
    except Error as e:
        print(f"Ocorreu um erro ao criar a tabela: {e}")

# --- Bloco de Execução Principal ---
# Este código só roda quando o script é executado diretamente,
# não quando ele é importado.
if __name__ == '__main__':
    print("Iniciando a configuração do banco de dados...")
    
    # Tenta criar uma conexão com o banco
    conexao = criar_conexao()
    
    # Se a conexão for bem-sucedida...
    if conexao:
        # ...chama a função para criar a tabela...
        criar_tabela(conexao)
        # ...e fecha a conexão para salvar e liberar o arquivo.
        conexao.close()
        print("Configuração do banco de dados finalizada. Conexão fechada.")
    else:
        print("Não foi possível criar a conexão com o banco de dados.")