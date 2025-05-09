i = 1
vista = 0
prazo = 0

while i <= 15:
    codigo = input('Digite o código da transação("V" para à vista e "P" a prazo )')
    valor = float(input('Digite o valor da transação: '))

    if codigo == "v" or codigo == "V":
        vista = vista + valor
    elif codigo == "p" or codigo == "P":
        prazo = prazo + valor
    else: print('Código inválido!')
i = i + 1
