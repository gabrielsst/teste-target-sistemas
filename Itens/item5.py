def inverter_string(s):
    invertida = ""
    for caractere in s:
        invertida = caractere + invertida
    return invertida

# Entrada do usuário
texto = input("Digite uma string para inverter: ")

# Resultado
texto_invertido = inverter_string(texto)
print(f"String invertida: {texto_invertido}")
