from banco import (
    adicionar_livro,
    exibir_livros,
    atualizar_preco_livro,
    remover_livro,
    buscar_livros_por_autor,
    criar_tabela,  # Importe a função que cria a tabela
)
from arquivos import (
    exportar_para_csv,
    importar_de_csv,
    fazer_backup,
    limpar_backups_antigos,
)

def exibir_menu():
    print("\nSistema de Gerenciamento de Livraria")
    print("1. Adicionar novo livro")
    print("2. Exibir todos os livros")
    print("3. Atualizar preço de um livro")
    print("4. Remover um livro")
    print("5. Buscar livros por autor")
    print("6. Exportar dados para CSV")
    print("7. Importar dados de CSV")
    print("8. Fazer backup do banco de dados")
    print("9. Sair")

def main():
    # Crie a tabela logo no início, caso não exista
    criar_tabela()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Adicionar novo livro
            adicionar_livro()
        elif opcao == "2":
            # Exibir todos os livros
            exibir_livros()
        elif opcao == "3":
            # Atualizar preço de um livro
            atualizar_preco_livro()
        elif opcao == "4":
            # Remover um livro
            remover_livro()
        elif opcao == "5":
            # Buscar livros por autor
            buscar_livros_por_autor()
        elif opcao == "6":
            # Exportar dados para CSV
            exportar_para_csv('exports/livros_exportados.csv')
        elif opcao == "7":
            # Importar dados de CSV
            caminho_csv = input("Digite o caminho do arquivo CSV: ")
            importar_de_csv(caminho_csv)
        elif opcao == "8":
            # Fazer backup do banco de dados
            fazer_backup()
        elif opcao == "9":
            # Sair
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
