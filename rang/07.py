"""def fibonacci(n):
    fib_sequence = [0, 1]  # Começamos com os dois primeiros números da sequência
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Adiciona o próximo número como a soma dos dois anteriores
    return fib_sequence

# Calcula os primeiros 8 números da sequência de Fibonacci
fib_numbers = fibonacci(10)
print("Os primeiros 8 números da sequência de Fibonacci são:", fib_numbers)"""

# Começamos com os dois primeiros números da sequência
fib_sequence = [0, 1]

# Calcula os próximos 6 números da sequência de Fibonacci
for _ in range(2, 8):
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

# Imprime os primeiros 8 números da sequência de Fibonacci
print("Os primeiros 8 números da sequência de Fibonacci são:", fib_sequence)