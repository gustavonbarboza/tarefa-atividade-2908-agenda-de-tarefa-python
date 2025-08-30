import sqlite3
from criar_banco import criar_conexao
from visualizar_tarefas import visualizar_tarefas_db, exibir_tarefas_formatadas

def deletar_pendentes_db():
    """
    Conecta ao banco e executa o comando SQL DELETE para remover todas as
    tarefas cuja situação é 0 (Pendente).
    """
    conn = criar_conexao()
    if not conn:
        return 0
    
    # O comando SQL para deletar linhas baseado em uma condição
    # A cláusula WHERE é crucial para não apagar tudo!
    sql = 'DELETE FROM tarefas WHERE situacao = 0'
    
    try:
        cursor = conn.cursor()
        # Executa o comando
        cursor.execute(sql)
        # Confirma (salva) a exclusão no banco
        conn.commit()
        # Retorna o número de linhas que foram afetadas (deletadas)
        return cursor.rowcount
    except sqlite3.Error as e:
        print(f"Erro ao deletar tarefas pendentes: {e}")
        return 0
    finally:
        # Garante que a conexão seja sempre fechada
        if conn:
            conn.close()

# --- Bloco de Execução Principal ---
def executar():
    """Função principal para ser chamada pelo menu."""
    todas_as_tarefas = visualizar_tarefas_db()
    tarefas_pendentes = [tarefa for tarefa in todas_as_tarefas if tarefa[6] == 0]
    print("\n--- 🗑️ Deletar Tarefas Pendentes 🗑️ ---")
    if not tarefas_pendentes:
        print("\n✅ Nenhuma tarefa pendente encontrada. Nada a fazer.")
    else:
        print("\nAVISO: As seguintes tarefas pendentes serão DELETADAS PERMANENTEMENTE:")
        exibir_tarefas_formatadas(tarefas_pendentes)
        try:
            confirmacao = input("\nVocê tem certeza? (s/n): ").lower()
        except KeyboardInterrupt:
            confirmacao = 'n'
        if confirmacao in ['s', 'sim']:
            num_deletadas = deletar_pendentes_db()
            print(f"\n✅ Sucesso! {num_deletadas} tarefa(s) foram deletadas.")
        else:
            print("\n❌ Operação cancelada.")

if __name__ == '__main__':
    executar()