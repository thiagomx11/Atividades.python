opcao=0
while opcao !=5:
    print("cardapio")
    print("1-hamburgue")
    print("2-pizza")
    print("3-salada")
    print("4-refrigeirante")
    print("5-sair")
    opcao=int(input("escolha uma opcao:"))
    if opcao ==1:
        print("voce escolheu a opcao 1.")
    elif opcao==2:
         print("voce escolheu a opcao 2.")
    elif opcao==3:
         print("voce escolheu a opcao 3.")
    elif opcao==4:
         print("voce escolheu a opcao 4.")
    elif opcao==5:
        print("saindo do cardapio...")
        break
    else:
        print("opcao invalida. tente novamente.")
        
            
    
    