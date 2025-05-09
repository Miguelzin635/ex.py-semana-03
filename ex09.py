idade_10_20 = 0
peso_inferior_40 = 0
mais_50 = 0
total_altura = 0

for i in range(25):
    print(f'\nPessoa {i + 1}')
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    if idade > 50:
        mais_50 += 1
    if 10 <= idade <= 20:
        idade_10_20 += 1     
        total_altura += altura
    if peso < 40:
        peso_inferior_40 += 1

if mais_50 > 0 or idade_10_20 > 0 or peso_inferior_40 > 0:
    print(f'\nA quantidade de pessoas com mais de 50 anos é: {mais_50}')  
    if idade_10_20 > 0:
        print(f'A média das alturas das pessoas com idade entre 10 e 20 anos é: {total_altura / idade_10_20:.2f}')
    else: 
        print('Nenhuma pessoa com idade entre 10 e 20 anos foi cadastrada.')
    print(f'A percentagem de pessoas com peso inferior a 40 kg entre todas as pessoas analisadas é: {(peso_inferior_40 / 3) * 100:.2f}%')
else: 
    print('Nenhuma condição foi atendida.')

input('\nPressione Enter para fechar o programa...')

