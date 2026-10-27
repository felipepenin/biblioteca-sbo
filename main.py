from services.funcoes import menu, cadastrar, listar, buscar, emprestar, devolver, cont_disponiveis
import time

while True:
    opcao = menu()

    if opcao == 1:
        cadastrar()

    elif opcao == 2:
        listar()

    elif opcao == 3:
        buscar()

    elif opcao == 4:
        emprestar()

    elif opcao == 5:
        devolver()

    elif opcao == 6: 
        cont_disponiveis()

    elif opcao == 7:
        print('Encerrando...')
        time.sleep(2)
        print('Encerrado. Obrigado por usar nossa Biblioteca, volte sempre!')
        break