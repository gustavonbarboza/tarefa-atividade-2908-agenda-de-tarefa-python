import sqlite3
from criar_banco import criar_conexao
from visualizar_tarefas import visualizar_tarefas_db, exibir_tarefas_formatadas

def atualizar_status_db(id_tarefa):
    """
    Conecta ao banco e executa o comando SQL UPDATE para alterar a situação
    de uma tarefa específica para 1 (Feito).
    """
    conn = criar_conexao()
    if not conn:
        return 0
    
    # Comando para atualizar a coluna 'situacao' para 1 onde o ID corresponder
    sql = 'UPDATE tarefas SET situacao = 1 WHERE id = ?'
    
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id_tarefa,))
        conn.commit()
        # Retorna o número de linhas afetadas, que deve ser 1 em caso de sucesso
        return cursor.rowcount
    except sqlite3.Error as e:
        print(f"Erro ao atualizar tarefa: {e}")
        return 0
    finally:
        if conn:
            conn.close()

def executar():
    """Função principal para ser chamada pelo menu."""
    print("\n--- ✅ Concluir Tarefa Pendente ✅ ---")
    
    # 1. Busca todas as tarefas e filtra apenas as pendentes
    todas_as_tarefas = visualizar_tarefas_db()
    tarefas_pendentes = [tarefa for tarefa in todas_as_tarefas if tarefa[6] == 0]
    
    # 2. Verifica se há tarefas para atualizar
    if not tarefas_pendentes:
        print("\n🎉 Todas as tarefas já estão concluídas! Nenhuma para atualizar.")
        return

    # 3. Mostra ao usuário apenas as tarefas que ele pode concluir
    print("\nTarefas pendentes que você pode concluir:")
    exibir_tarefas_formatadas(tarefas_pendentes)
    
    # Cria um conjunto de IDs válidos para verificação rápida
    ids_validos = {tarefa[0] for tarefa in tarefas_pendentes}
    
    # 4. Pede ao usuário para escolher o ID
    try:
        id_escolhido = int(input("\nDigite o ID da tarefa que você deseja marcar como 'Feita': "))
        
        # 5. Valida se o ID escolhido é de uma tarefa pendente
        if id_escolhido in ids_validos:
            # 6. Executa a atualização
            num_atualizadas = atualizar_status_db(id_escolhido)
            if num_atualizadas > 0:
                print(f"\n✅ Sucesso! A tarefa de ID {id_escolhido} foi marcada como 'Feita'.")
            else:
                print("\n❌ Falha ao atualizar a tarefa.")
        else:
            print("\n❌ Erro: O ID digitado não corresponde a uma tarefa pendente válida.")
            
    except ValueError:
        print("\n❌ Erro: Por favor, digite um número de ID válido.")
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")

if __name__ == '__main__':
    executar()