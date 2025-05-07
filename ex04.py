grupos = []
for i in range(2):
    grupo = []
    print(f"Grupo {i + 1}")
    for n in range(4):
        valor = float(input(f"Digite o {n + 1}º valor: "))
        grupo.append(valor)
    grupos.append(grupo)

print("\nGrupos lidos:")
for i, grupo in enumerate(grupos, 1):
    print(f"Grupo {i}: {grupo}")

for grupo in grupos:
    for i in range(len(grupo)):
        for j in range(i + 1, len(grupo)):
            if grupo[i] > grupo[j]:
                grupo[i], grupo[j] = grupo[j], grupo[i]
print("\nGrupos em ordem crescente: ")
for i, grupo in enumerate(grupos, 1):
    print(f"Grupo {i}: {grupo}")
