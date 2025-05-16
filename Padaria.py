opcao=0
frances=0
integral=0
doceliso=0
docefarofa=0
paodeforma=0
quantidade= int
valortotal=0
valordocefarofa=0
valordoceliso=0
valorfrances=0
valorintegral=0
valorpaodeforma=0
while opcao!=6:
    print("------PADARIA DO PORTUGOL------")
    print("[1] PÃO FRANCÊS. ")
    print("[2] PÃO INTEGRAL. ")
    print("[3] PÃO DOCE LISO. ")
    print("[4] PÃO DOCE FAROFA. ")
    print("[5] PÃO DE FORMA. ")
    print("[6] PARA FINALIZAR A COMPRA. ")
    print("---------------------------------------- ")
    opcao = int(input("ESCOLHA SUA OPÇÃO:"))
    if opcao ==1:
        quantidade=int(input("Digite a quantidade de Pão francês que você quer:"))
        frances=frances+quantidade
        valorfrances=frances+(quantidade*1.04) 
    elif opcao==2:
        quantidade=int(input("Digite a quantidade de Pão integral que você quer: "))
        integral=integral+quantidade
        valorintegral=integral+(quantidade*1.04)
    elif opcao==3:
        quantidade=int(input("Digite a quantidade de Pão doce liso que você quer:"))
        doceliso=doceliso+quantidade
        valordoceliso=doceliso+(quantidade*1.08)
    elif opcao== 4: 
        quantidade=int(input("Digite a quantidade de Pão doce farofa que você quer:"))
        docefarofa=docefarofa+quantidade
        valordocefarofa=docefarofa+(quantidade*1.11)
    elif opcao== 5:
        quantidade=int(input("Digite a quantidade de Pão de Forma que você quer: "))
        paodeforma=paodeforma+quantidade
        valorpaodeforma=paodeforma+(quantidade*0.95)
    elif opcao==6:
        valortotal=(valorfrances+valorintegral+valordoceliso+valordocefarofa+valorpaodeforma)
        break
print("resumo da compra: ")
if frances>0:
    print("Pão Francês - Quantidade: ", frances,"|valor:R$ ", valorfrances)
if integral>0:
        print("Pão Integral - Quantidade: ", integral,"|valor:R$ ", valorintegral)
if doceliso>0:
        print("Pão Doce Liso - Quantidade: ", doceliso,"|valor:R$ ", valordoceliso)
if docefarofa>0:
        print("Pão Doce Farofa - Quantidade: ", docefarofa,"|valor:R$ ", valordocefarofa)
if paodeforma>0:
        print("Pão De Forma - Quantidade: ", paodeforma,"|valor:R$ ", valorpaodeforma)
else:
        print("Valor total da compra: R$ ", valortotal)