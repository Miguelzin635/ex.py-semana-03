i = 1
valor_inicial = int(input('Digite um valor de entrada (Positivo: )'))
degraus = int(input('Digite o número de degraus desejado: '))

if valor_inicial and degraus < 0:
    print('Erro: Apenas números positivos')

for i in range(1, degraus+1):        
    for j in range(i):
        print(valor_inicial, end=" ")
        valor_inicial += 1

    print()

input('Pressione Enter para fechar o programa...')
