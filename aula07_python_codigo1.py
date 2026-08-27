# Aula 07 - Exceções com try/except/finally

try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
    print(f"Resultado: {resultado}")

except ValueError:
    print("Isso não é um número válido!")

except ZeroDivisionError:
    print("Não é possível dividir por zero!")

finally:
    print("Execução finalizada.")
