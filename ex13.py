import random

num_aleatorio = random.randint(1, 50)
tentativas = 0


print('Jogo de adivinhação!')
print('Você tem no máximo 7 tentativas para adivinhar o número, lembrando que vai de 1 ate 50')
while tentativas < 7:
    chute = int(input('Tente a sorte: '))
    if chute < 1 or chute > 50:
        print('** Valor inválido, somente números entre 1 e 50!')
        continue

    tentativas += 1

    if chute == num_aleatorio:
        print(f'Parabéns você acertou o número em {tentativas} tentativas!!')
        break
    elif chute < num_aleatorio:
        print('\nO número é maior que o digitado')
    else: print('\nO número é menor que o digitado')

if chute != num_aleatorio:
    print(f'\nVocê nao conseguiu acertar o número, que era {num_aleatorio}')

input('\nPressione Enter para fechar o programa...')
