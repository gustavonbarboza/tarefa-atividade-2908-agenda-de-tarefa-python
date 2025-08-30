import sqlite3
from criar_banco import criar_conexao
from visualizar_tarefas import exibir_tarefas_formatadas

def buscar_tarefas_db(termo_busca):
    """
    Conecta ao banco e busca tarefas onde o termo aparece no nome ou na descrição.
    A busca não diferencia maiúsculas/minúsculas.
    """
    conn = criar_conexao()
    if not conn:
        return []
    
    try:
        cursor = conn.cursor()
        
        # Prepara o termo de busca para usar com o operador LIKE
        # '%' é um coringa que significa "qualquer sequência de caracteres"
        # O termo de busca é colocado entre '%' para encontrar correspondências em qualquer lugar do texto
        termo_formatado = f'%{termo_busca.lower()}%'
        
        # O comando SQL usa LIKE para buscas parciais e LOWER() para ignorar maiúsculas/minúsculas
        sql = "SELECT * FROM tarefas WHERE LOWER(nome) LIKE ? OR LOWER(descricao) LIKE ?"
        
        # Executa a busca passando o termo formatado para ambos os campos (nome e descrição)
        cursor.execute(sql, (termo_formatado, termo_formatado))
        
        resultados = cursor.fetchall()
        return resultados
    except sqlite3.Error as e:
        print(f"Erro ao buscar tarefas: {e}")
        return []
    finally:
        if conn:
            conn.close()

def executar():
    """Função principal para ser chamada pelo menu."""
    print("\n--- 🔎 Buscar Tarefas 🔎 ---")
    termo = input("Digite o termo que deseja buscar no título ou na descrição: ")
    
    # Verifica se o usuário digitou algo
    if not termo.strip():
        print("\n❌ Nenhum termo de busca inserido. Operação cancelada.")
        return
        
    print(f"\nBuscando por '{termo}'...")
    
    # Chama a função que executa a busca no banco de dados
    tarefas_encontradas = buscar_tarefas_db(termo)
    
    # Mostra os resultados usando nossa função de exibição padronizada
    # A função já trata o caso de a lista estar vazia
    exibir_tarefas_formatadas(tarefas_encontradas)

if __name__ == '__main__':
    executar()