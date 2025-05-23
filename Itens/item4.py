# Faturamento mensal por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcular o total
total_faturamento = sum(faturamento_estados.values())

# Calcular e exibir o percentual de cada estado
print("Percentual de representação por estado:")
for estado, valor in faturamento_estados.items():
    percentual = (valor / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")
