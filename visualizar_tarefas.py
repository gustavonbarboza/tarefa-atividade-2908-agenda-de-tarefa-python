import sqlite3
from criar_banco import criar_conexao

def visualizar_tarefas_db():
    """
    Esta função se conecta ao banco de dados e executa o comando SQL SELECT
    para buscar todas as tarefas.
    """
    # Abre a conexão com o banco
    conn = criar_conexao()
    # Se a conexão falhar, retorna uma lista vazia
    if not conn:
        return []
    
    try:
        cursor = conn.cursor()
        # Executa o comando SQL para selecionar todas as colunas de todas as linhas
        # ORDER BY id DESC faz com que as tarefas mais recentes apareçam primeiro
        cursor.execute("SELECT * FROM tarefas ORDER BY id DESC")
        # Pega todos os resultados da consulta
        rows = cursor.fetchall()
        # Retorna a lista de tarefas encontradas
        return rows
    except sqlite3.Error as e:
        print(f"Erro ao visualizar tarefas: {e}")
        return []
    finally:
        # Garante que a conexão seja sempre fechada
        if conn:
            conn.close()

def exibir_tarefas_formatadas(tarefas):
    """
    Recebe uma lista de tarefas e as exibe no terminal de forma organizada.
    """
    print("\n--- 📋 LISTA DE TAREFAS 📋 ---")
    
    # Verifica se a lista de tarefas está vazia
    if not tarefas:
        print("Nenhuma tarefa encontrada no banco de dados.")
    else:
        # Imprime o cabeçalho da tabela formatado
        print(f"{'ID':<4} | {'Nome da Tarefa':<30} | {'Data Final':<12} | {'Situação':<10}")
        print("-" * 70)
        
        # Itera sobre cada tarefa na lista para imprimi-la
        for tarefa in tarefas:
            # Desempacota a tupla da tarefa em variáveis para facilitar a leitura
            id_tarefa    = tarefa[0]
            nome         = tarefa[1]
            data_final   = tarefa[4]
            situacao_num = tarefa[6]
            
            # Traduz a situação de número (0/1) para um texto mais amigável com emoji
            situacao_texto = "✅ Feito" if situacao_num == 1 else "⏳ Pendente"
            
            # Limita o tamanho do nome para evitar que a tabela quebre a formatação
            if len(nome) > 28:
                nome = nome[:25] + "..."

            # Imprime a linha da tarefa com o espaçamento correto
            print(f"{id_tarefa:<4} | {nome:<30} | {data_final:<12} | {situacao_texto:<10}")
            
    print("-" * 70)


# --- Bloco de Execução Principal ---
# Este código só roda quando o script é executado diretamente
def executar():
    """Função principal para ser chamada pelo menu."""
    lista_de_tarefas = visualizar_tarefas_db()
    exibir_tarefas_formatadas(lista_de_tarefas)

if __name__ == '__main__':
    executar()