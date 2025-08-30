import sqlite3
import datetime
from criar_banco import criar_conexao

def inserir_tarefa_db(tarefa):
    """
    Esta é a função que efetivamente se conecta ao banco e executa o comando SQL INSERT.
    Ela recebe uma tupla 'tarefa' com os dados a serem inseridos.
    """
    # Abre a conexão com o banco
    conn = criar_conexao()
    # Se a conexão falhar, interrompe a função
    if not conn:
        return None
    
    # Comando SQL para inserir dados na tabela 'tarefas'
    # Usamos '?' para evitar injeção de SQL, uma prática de segurança essencial
    sql = ''' INSERT INTO tarefas(nome, descricao, data_inicial, data_final, tipo, situacao)
              VALUES(?,?,?,?,?,?) '''
    try:
        cursor = conn.cursor()
        # Executa o SQL, passando a tupla 'tarefa' para substituir os '?'
        cursor.execute(sql, tarefa)
        # Confirma (salva) a transação no banco de dados
        conn.commit()
        # Retorna o ID da linha que acabamos de inserir
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Erro ao inserir tarefa: {e}")
        return None
    finally:
        # Garante que a conexão seja sempre fechada, mesmo se ocorrer um erro
        if conn:
            conn.close()

def obter_dados_da_tarefa():
    """
    Esta função interage com o usuário para coletar os dados da nova tarefa.
    Ela também faz algumas validações simples.
    """
    print("\n--- 📝 Adicionar Nova Tarefa 📝 ---")
    
    # Coleta e valida o nome da tarefa
    nome = input("Nome da Tarefa: ")
    while not nome.strip():
        print("Erro: O nome da tarefa não pode ser vazio.")
        nome = input("Nome da Tarefa: ")

    descricao = input("Descrição (opcional): ")
    
    # Coleta e valida a data inicial
    while True:
        data_inicial_str = input(f"Data de Início (AAAA-MM-DD, hoje é {datetime.date.today()}): ")
        try:
            datetime.date.fromisoformat(data_inicial_str)
            break # Data válida, sai do loop
        except ValueError:
            print("Erro: Formato de data inválido. Por favor, use AAAA-MM-DD.")

    # Coleta e valida a data final
    while True:
        data_final_str = input("Data Final (AAAA-MM-DD): ")
        try:
            data_final_obj = datetime.date.fromisoformat(data_final_str)
            data_inicial_obj = datetime.date.fromisoformat(data_inicial_str)
            if data_final_obj >= data_inicial_obj:
                break # Data válida e não anterior à inicial, sai do loop
            else:
                print("Erro: A data final não pode ser anterior à data inicial.")
        except ValueError:
            print("Erro: Formato de data inválido. Por favor, use AAAA-MM-DD.")

    tipo = input("Tipo/Categoria (ex: Trabalho, Pessoal, Estudo): ")
    
    # Coleta e valida a situação da tarefa (Feito ou Não Feito)
    while True:
        situacao_input = input("A tarefa já foi concluída? (s/n): ").lower()
        if situacao_input in ['s', 'sim']:
            situacao = 1  # 1 representa "Feito"
            break
        elif situacao_input in ['n', 'nao', 'não']:
            situacao = 0  # 0 representa "Não Feito"
            break
        else:
            print("Erro: Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

    # Retorna uma tupla com todos os dados coletados na ordem correta para o SQL
    return (nome, descricao, data_inicial_str, data_final_str, tipo, situacao)

# --- Bloco de Execução Principal ---
# Este código só roda quando o script é executado diretamente
def executar():
    """Função principal para ser chamada pelo menu."""
    nova_tarefa_dados = obter_dados_da_tarefa()
    novo_id_tarefa = inserir_tarefa_db(nova_tarefa_dados)
    if novo_id_tarefa:
        print(f"\n✅ Tarefa '{nova_tarefa_dados[0]}' inserida com sucesso! ID: {novo_id_tarefa}")
    else:
        print("\n❌ Falha ao inserir a tarefa.")

if __name__ == '__main__':
    executar()