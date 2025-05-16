num1 = 0 
num2 =0
opcao =0
while opcao !=5:
    print("🧮​👨🏻‍💻​🧠​🧠​CALCULADORA SIMPLES🧮​👨🏻‍💻​🧠​🧠​")
    print("1- Soma")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("5- Sair")
    opcao = int(input("Escolha uma opção:🧮​👨🏻‍💻​🧠​🧠​ "))
    if opcao !=5:
        num1 = int(input("🧮​👨🏻‍💻​🧠​🧠​Escolha um número:"))
        num2 = int(input("Escolha um número:"))
    if opcao ==1:
        print ("Você escolheu a opção somav🧮​👨🏻‍💻​🧠​🧠​")
        print (f" 🧮​👨🏻‍💻​🧠​🧠​O resultado da sua soma é {num1+num2}")
    elif opcao ==2:
        print ("Você🧮​👨🏻‍💻​🧠​🧠​ escolheu a opção🧮​👨🏻‍💻​🧠​🧠​ subtração")
        print (f" O 🧮​👨🏻‍💻​🧠​🧠​resultado da sua subtração é 🧮​👨🏻‍💻​🧠​🧠​{num1-num2}")
    elif opcao ==3:
        print ("Você escolheu a opção multiplicação")
        print (f" O resultado da sua multiplicação é {num1*num2}")
    elif opcao ==4:
        print ("Você escolheu🧮​👨🏻‍💻​🧠​🧠​ a opção divisão")
        print (f" O 🧮​👨🏻‍💻​🧠​🧠​resultado da sua divisão 🧮​👨🏻‍💻​🧠​🧠​é {num1/num2}")
    elif opcao ==5:
        print ("Fechando a calculadora.")
        break 
