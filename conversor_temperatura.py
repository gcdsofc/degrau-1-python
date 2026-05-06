print("=== CONVERSOR DE TEMPERATURA ===")

while True:
    print("")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Fahrenheit para Kelvin")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = round((celsius * 9/5) + 32, 2)
        print("Resultado:", resultado, "°F")

    elif opcao == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = round((fahrenheit - 32) * 5/9, 2)
        print("Resultado:", resultado, "°C")

    elif opcao == 3:
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = round(celsius + 273.15, 2)
        print("Resultado:", resultado, "°K")

    elif opcao == 4:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = round((fahrenheit - 32) * 5/9 + 273.15, 2)
        print("Resultado:", resultado, "°K")

    elif opcao == 5:
        print("Encerrando...")
        break