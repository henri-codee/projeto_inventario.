import sqlite3
# Aqui vamos importar as funções que você já escreveu
# Para isso funcionar, os nomes dos arquivos devem estar simples

def menu():
    while True:
        print("\n--- 🛡️ SISTEMA DE CONTROLE DO BUNKER ---")
        print("1. Adicionar Item")
        print("2. Listar Inventário")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Em vez de reescrever tudo, podemos apenas rodar o código do outro arquivo
            import adicionar 
            # Dica: O ideal no futuro é transformar o código em funções (def)
        elif opcao == "2":
            import listar
        elif opcao == "0":
            print("Encerrando sistema... Fique seguro lá fora!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()