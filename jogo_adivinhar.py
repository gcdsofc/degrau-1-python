import random

print("=== JOGO DE ADIVINHAR O NÚMERO ===")
print("Estou pensando em um número entre 1 e 100...")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Digite seu chute: "))
    tentativas += 1

    if chute < numero_secreto:
        print("Muito baixo! Tente um número maior.")
    elif chute > numero_secreto:
        print("Muito alto! Tente um número menor.")
    else:
        print("Parabéns! Você acertou em", tentativas, "tentativas!")
        break