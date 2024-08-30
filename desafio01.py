def is_fibonacci(n):
    # Função para verificar se um número é um quadrado perfeito
    def is_perfect_square(x):
        s = int(x**0.5)
        return s * s == x

    # Verifica se 'n' é um número de Fibonacci
    # Um número é Fibonacci se e somente se um dos seguintes for um quadrado perfeito:
    # 5*n*n + 4 ou 5*n*n - 4
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Solicita ao usuário o número de entrada
numero = int(input("Qual número você deseja testar? "))

# Verifica se o número pertence à sequência de Fibonacci
if is_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
