idade_50 = 0
peso_60 = 0
olhos_azuis = 0
ruivas = 0
total_altura_baixa = 0
idade_altura_baixa = 0
for i in range(20):
    idade = 0
    idade = int(input('\nDigite sua idade: '))
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    olhos = input('Digite a cor dos olhos (A - Azul, P - Preto, V - Verde e C - Castanho): ')
    cabelo = input('Digite a cor do cabelo (P - Preto, C - Castanho, L - Louro e R - Ruivo): ')
    # validação dos olhos e cabelos
    if olhos not in ['A', 'a', 'P', 'p', 'V', 'v', 'C', 'c']:
      print('Cor dos olhos inválida!')
      continue
    if cabelo not in ['P', 'p', 'C', 'c', 'L', 'l', 'r', 'R']:
        print('Cor de cabelo inválida!')
        continue
        
    # contagem de pessoas maior que 50 e peso menor que 60
    if idade > 50 and peso < 60:
        idade_50 += 1

    # media das idades de pessoas com menos de 1.50
    if altura < 1.50:
        idade_altura_baixa += idade
        total_altura_baixa += 1

    # % de pessoas com olhos azuis
    if olhos == 'A' or olhos == 'a':
        olhos_azuis += 1

    # qntd de pessoas ruivas sem olhos azuis
    if (cabelo == 'R' or cabelo == 'r') and (olhos != 'A' and olhos != 'a'):
        ruivas += 1

print('\nResultados:')
if idade_50 > 0:
    print(f'A quantidade de pessoas com mais de 50 anos e peso inferior a 60 kg é: {idade_50}')
else: print('Nenhuma pessoa com mais de 50 anos e peso inferior a 60 kg foi cadastrada.')

if total_altura_baixa > 0:
    media_idade = idade_altura_baixa / total_altura_baixa
    print(f'A média das idades das pessoas com altura inferior a 1.50 é: {media_idade:.2f}')
else: print('Nenhuma pessoa com altura inferior a 1.50 foi cadastrada.')

if olhos_azuis > 0:
    print(f'A porcentagem de pessoas com olhos azuis é: {(olhos_azuis / 2) * 100:.2f}%')
else: print('Nenhuma pessoa com olhos azuis foi cadastrada.')

if ruivas > 0:
    print(f'A quantidade de pessoas ruivas sem olhos azuis é: {ruivas}')
else: print('Nenhuma pesssoa ruiva sem olhos azuis foi cadastrada.')

input('\nPressione Enter para fechar o programa...')
        
        
