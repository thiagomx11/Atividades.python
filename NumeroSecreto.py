import random
numero_secreto=random.randint(1,10)
tentativa=0
contagem_tentativas=0
numero=0
print ("BEM VINDO AO JOGO DA ADIVINHAÇÃO! ")
print ("Tente adivinhar o número secreto entre 1 e 10.")
while   tentativa != numero_secreto:
    numero=int(input("Digite sua tentativa: "))
    contagem_tentativas= contagem_tentativas+1
    if numero==numero_secreto :
        print("Parabéns!Você acertou.")
        print(f"Você precisou de: {contagem_tentativas} tentativas")
        break
    elif numero < numero_secreto:
        print("o número secreto é maior!")
    else:
        print("o número secreto é menor!")
