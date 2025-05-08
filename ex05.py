nomes = []
bonus = []
for i in range(3):
    nome = str(input('\nInforme o nome: '))
    compra = float(input('Informe o valor de suas compras no ano passado: '))
    if compra < 1000:
        bonus_conta = compra * 0.10   
    else: 
        bonus_conta = compra * 0.15
    nomes.append(nome)
    bonus.append(bonus_conta)
print('\nLista dos clientes com bônus:')
for i in range(len(nomes)):
    print(f'O cliente {nomes[i]} ganhou um bônus de {bonus[i]:.2f}')


input('Pressione Enter para fechar o programa...')
