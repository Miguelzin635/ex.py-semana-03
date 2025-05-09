i = 1
vista = 0
prazo = 0

while i <= 3:
    codigo = input('Digite o código da transação("V" para à vista e "P" a prazo ): ')
    valor = float(input('Digite o valor da transação: '))

    if codigo == "v" or codigo == "V":
        vista = vista + valor
    elif codigo == "p" or codigo == "P":
        prazo = prazo + valor
    else: print('Código inválido!')
    i = i + 1

print(f'\nO valor total das compras à vista é: {vista:.2f}')
print(f'O valor total das compras a prazo é: {prazo:.2f}')
print(f'O valor t otal das compras efetuadas é: {vista + prazo:.2f}')
print(f'O valor da primeira prestação, sendo que essas serão pagas em três vezes: {prazo / 3:.2f}')

input('Pressione Enter para sair do programa...')
