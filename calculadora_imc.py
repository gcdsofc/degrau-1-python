print("=== CALCULADORA DE IMC ===")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = round(peso / (altura ** 2), 2)

print(f"Seu IMC é: {imc}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 35:
    print("Classificação: Obesidade grau 1")
elif 35 <= imc < 40:
    print("Classificação: Obesidade grau 2")
else:
    print("Classificação: Obesidade grau 3")