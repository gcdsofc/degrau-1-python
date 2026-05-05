print("=== CALCULADORA ===")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input("Escolha uma opção: "))

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == 1:
    resultado = numero1 + numero2
    print("Resultado:", resultado)
elif opcao == 2:
    resultado = numero1 - numero2
    print("Resultado:", resultado)
elif opcao == 3:
    resultado = numero1 * numero2
    print("Resultado:", resultado)
elif opcao == 4:
    if numero2 == 0:
        print("Erro: não é possível dividir por zero!")
    else:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
else:
    print("Opção inválida!")