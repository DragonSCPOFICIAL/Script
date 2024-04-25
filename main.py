import os
import sys
from menu_options.menu1 import generate_and_test_proxies
from menu_options.menu2 import generate_payloads
from menu_options.menu3 import test_individual_proxy
from menu_options.menu4 import generate_and_test_proxies_by_operator
from menu_options.menu5 import check_updates
from menu_options.menu0 import exit_program

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("==== Menu Principal ====")
        print("1 - Gerar e Testar Proxies")
        print("2 - Gerar Payloads")
        print("3 - Testar Proxy Individual")
        print("4 - Gerar e Testar Proxies por Operadora")
        print("5 - Verificar Atualizações")
        print("0 - Sair")
        choice = input("Escolha uma opção ou pressione Enter para sair: ")

        if choice == '1':
            generate_and_test_proxies()
        elif choice == '2':
            generate_payloads()
        elif choice == '3':
            test_individual_proxy()
        elif choice == '4':
            generate_and_test_proxies_by_operator()
        elif choice == '5':
            check_updates()
        elif choice == '0':
            exit_program()
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
