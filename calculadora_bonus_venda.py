nome = (input("Informe o seu nome: "))
salario_fixo = float (input("Informe o seu salario fixo: "))
vendas = int(input("Informe quantas vendas realizou:"))
comissao = salario_fixo* 0.15
salario_recebido = salario_fixo+comissao
if vendas >=20:
    print(f"Seu salario será {salario_recebido}, parabéns por bater a meta!​💲​🤑 ​")
else:
    print (f" Você não bateu a meta seu salario será {salario_fixo}! ​​😪​😓​ ")
    
