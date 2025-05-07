s = 1
for i in range(92, 1478):
    cont = 0
    for n in range(1, i + 1):
        if i % n == 0:
            cont = cont + 1
    if cont == 2:
        print(i)
        s = s * i
print(s)

input("Presione Enter para sair")
