def pertence_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

# Entrada do usuário
try:
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    
    if numero < 0:
        print("Números negativos não pertencem à sequência de Fibonacci.")
    elif pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
