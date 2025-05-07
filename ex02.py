n = int(input("Digite um número inteiro e positivo: "))
n1 = 1
for n in range(2, n + 1):
    n1 = n1 + (1 / n)
print(f"{n1:.2f}")
