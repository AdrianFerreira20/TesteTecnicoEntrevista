def fibonacci(num):
    # Inicializa os primeiros números da sequência de Fibonacci
    fib_seq = [0, 1]

    # Gera a sequência até que o último número seja maior ou igual ao número informado
    while fib_seq[-1] < num:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    # Verifica se o número informado está na sequência
    if num in fib_seq:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."


# Exemplo de uso
numero = int(input("Informe um número: "))
resultado = fibonacci(numero)
print(resultado)
