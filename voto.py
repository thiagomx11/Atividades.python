ano_atual=2025
ano_nascimento=int(input("digite seu ano de nascimento:"))
idade=ano_atual-ano_nascimento
print(f"voce tem{idade} anos.")
if idade<16:
    print(" voce nao pode votar!")
elif idade<18 or idade>70:
    print("seu voto e obrigatorio.")
else:
    print("Seu voto é obrigatorio.")