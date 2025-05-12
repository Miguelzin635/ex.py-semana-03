print('PROGRAMA FATORIAL')
num = int(input('Digite um número para calcular seu fatorial : '))

fat = 1

# O i vai receber do 1 ate o número digitado pelo usuário
for i in range (1, num + 1):

    # O fat começa do 1 e como o "i" vai ate o número digitado, vai ser fat = 1 * i=1, fat = 1 dpois * i=2, fat = 2, dpois * i=3, fat = 6...
    fat = fat * i

print(f'O resultado do seu fatorial é {fat}.')

input('Pressione Enter para fechar o programa...')
