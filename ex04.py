grupos = []
for i in range(5):
    print(f"Grupo {i + 1}")
    valor_total = []
    for n in range(4):
        valor = float(input(f"Digite o {n + 1}º valor: "))
        valor_total.append(valor)
    grupos.append(valor_total)

print("\nGrupos lidos:")
for i, valor_total in enumerate(grupos, 1):
    print(f"Grupo {i}: {valor_total}")

print("\nGrupos em ordem crescente: ")
for valor_total in grupos:
    for l in range(len(valor_total)):
        for j in range(l + 1, len(valor_total)):
            if valor_total[l] > valor_total[j]:
                valor_total[l], valor_total[j] = valor_total[j], valor_total[l]
for i, valor_total in enumerate(grupos, 1):
    print(f"Grupo {i}: {valor_total}")

print("\nGrupos em ordem decrescente: ")
for valor_total in grupos:
    for l in range(len(valor_total)):
        for j in range(l + 1, len(valor_total)):
            if valor_total[l] < valor_total[j]:
                valor_total[l], valor_total[j] = valor_total[j], valor_total[l]
for i, valor_total in enumerate(grupos, 1):
    print(f"Grupo {i}: {valor_total}")
        
input('\nPressione Enter para fechar o programa...')
