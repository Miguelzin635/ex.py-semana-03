fe_1 = fe_2 = fe_3 = fe_4 = fe_5 = 0
for i in range(6):
    pessoa = i + 1
    idade = int(input('Digite sua idade: '))   
    if idade <= 15:
        fe_1 = fe_1 + 1
        x = (100 * fe_1) / 6
    elif 16 <= idade <=30:
        fe_2 = fe_2 + 1
    elif 31 <= idade <= 45:
        fe_3 = fe_3 + 1
    elif 46 <= idade <= 60:
        fe_4 = fe_4 + 1
    else:
        fe_5 = fe_5 + 1
        y = (100 * fe_5) / 6

print('FAIXA ETÁRIA\t\tIDADE\t\t\tQUANTIDADE')
print('-' * 60)
print('1ª\t\t\taté 15 anos\t\t', fe_1)
print('2ª\t\t\tde 16 a 30 anos\t\t', fe_2)
print('3ª\t\t\tde 31 a 45 anos\t\t', fe_3)
print('4ª\t\t\tde 46 a 60 anos\t\t', fe_4)
print('5ª\t\t\tAcima de 61 anos\t', fe_5)
print('-' * 60)
print(f' porcentagem de pessoas da 1° faixa etária é de: {x:.2f}%')
print(f' porcentagem de pessoas da 5° faixa etária é de: {y:.2f}%')

input('\nPressione Enter para fechar o programa...')
