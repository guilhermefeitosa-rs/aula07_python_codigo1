# Aula 07 - Sets: Coletor de CPFs Únicos

cpfs_coletados = set()

while True:
    entrada = input("Digite um CPF (ou 'sair'): ").strip()

    if entrada.lower() == "sair":
        break

    try:
        if not entrada:
            raise ValueError("O CPF não pode estar vazio.")

        cpfs_coletados.add(entrada)
        print("CPF adicionado.")

    except ValueError as erro:
        print(f"Erro: {erro}")

print(f"Total de CPFs únicos coletados: {len(cpfs_coletados)}")
print("CPFs cadastrados:")

for cpf in cpfs_coletados:
    print(cpf)
