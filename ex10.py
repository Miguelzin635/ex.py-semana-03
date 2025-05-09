preco_final = float(input('Digite o preço do carro: R$'))

print('\n' + '-' * 100)
print('À vista\t\t\t\tquantidade de parcelas\t\t\tPreço final ')
print('-' * 100)

# Cálculo do preço à vista
valor_vista = preco_final - (preco_final * 0.20)
print(f'R$ {valor_vista:.2f}\t\t\t\t{"-":<37}{"-"}')

for i in range(1, 11):
    parcelas = i * 6
    acrescimo = i * 3
    print(f'\t\t\t\t\t{parcelas:<10}\t\t\tR$ {preco_final + (preco_final * acrescimo / 100):.2f}')
print('-' * 100)

input('\nPressione Enter para sair do programa...')
