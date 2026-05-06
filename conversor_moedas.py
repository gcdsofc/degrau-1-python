print("--CONVERSOR DE MOEDAS--")

while True:
    print()
    print("1 - Real para Dólar")    
    print("2 - Real para Euro")
    print("3 - Real para Libra")
    print("4 - Sair")
    print()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1: 
      print()
      real = float(input("Digite o valor em Real: "))
      resultado = round(real * 0.18, 2)
      print (f"Resultado: {resultado} Dólares")

    elif opcao == 2: 
      print()
      real = float(input("Digite o valor em Real: "))
      resultado = round(real * 0.16, 2)
      print (f"Resultado: {resultado} Euros")

    elif opcao == 3: 
      print()
      real = float(input("Digite o valor em Real: "))
      resultado = round(real * 0.14, 2)
      print (f"Resultado: {resultado} Libras")
             
    elif opcao == 4:
      print()
      print("Encerrando...")
      break
    else:
      print()
      print("Opção inválida!")