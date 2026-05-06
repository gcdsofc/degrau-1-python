print("=== VERIFICADOR DE CPF ===")

cpf = input("Digite o CPF (com ou sem pontuação): ")

cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")
cpf = cpf.replace(" ", "")

if len(cpf) != 11:
    print("CPF inválido! O CPF deve ter 11 dígitos.")
elif not cpf.isdigit():
    print("CPF inválido! O CPF deve conter apenas números.")
elif cpf == cpf[0] * 11:
    print("CPF inválido! CPF com todos os dígitos iguais não é válido.")
else:
    print("CPF válido!")