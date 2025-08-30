import os
import time

# Importa as funções 'executar' de cada um dos nossos módulos
import visualizar_tarefas
import inserir_nova_tarefa
import atualizar_tarefa_status
import deletar_tarefas_pendentes
import buscar_tarefas  # NOVO - Importa o módulo de busca

# Importa as funções de setup do banco
from criar_banco import criar_conexao, criar_tabela

def limpar_tela():
    """Limpa o terminal para uma melhor experiência de usuário."""
    os.system('cls' if os.name == 'nt' else 'clear')

def configurar_banco_de_dados():
    """Função para rodar a configuração inicial do banco de dados."""
    print("Configurando o banco de dados...")
    conexao = criar_conexao()
    if conexao:
        criar_tabela(conexao)
        conexao.close()
    print("Configuração finalizada.")
    time.sleep(2)

def exibir_menu():
    """Exibe o menu principal da aplicação."""
    limpar_tela()
    print("--- ⚙️ GERENCIADOR DE TAREFAS ⚙️ ---")
    print("\nEscolha uma opção:")
    print("1. Visualizar todas as tarefas")
    print("2. Buscar tarefa por termo")  # NOVO
    print("3. Adicionar uma nova tarefa") # Renumerado
    print("4. Concluir uma tarefa pendente") # Renumerado
    print("5. Deletar todas as tarefas pendentes") # Renumerado
    print("------------------------------------")
    print("9. (Re)Criar e configurar o banco de dados")
    print("0. Sair do programa")
    print("-" * 36)

def main():
    """Função principal que executa o loop do menu."""
    while True:
        exibir_menu()
        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            limpar_tela()
            visualizar_tarefas.executar()
        elif escolha == '2': # NOVO
            limpar_tela()
            buscar_tarefas.executar()
        elif escolha == '3': # Renumerado
            limpar_tela()
            inserir_nova_tarefa.executar()
        elif escolha == '4': # Renumerado
            limpar_tela()
            atualizar_tarefa_status.executar()
        elif escolha == '5': # Renumerado
            limpar_tela()
            deletar_tarefas_pendentes.executar()
        elif escolha == '9':
            limpar_tela()
            configurar_banco_de_dados()
        elif escolha == '0':
            print("\nSaindo do programa. Até mais!")
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.")
            time.sleep(1.5)
            continue

        print("\nPressione Enter para voltar ao menu...")
        input()

if __name__ == '__main__':
    main()