valor_decimal = int(input('Digite um valor decimal: '))

print ('-'*37)
print('\tOpções de conversão: ')
print('-'*37)
print('1-  Decimal para Binário\n2-  Decimal para Octal\n3-  Decimal para Hexadecimal')
print('-'*37)
escolha = int(input('Digite a opção desejada: '))

if escolha < 1 or escolha > 3:
    print('\nOpção inválida!')
else:
    if escolha == 1:
        # O binário começa vazio
        binario = ''
        # Aqui o número assume o valor_decimal para nao modificar o original
        numero = valor_decimal
        if numero == 0:
            binario = '0'
        else:
            while numero > 0:
                # O resto vai ser adicionado ao 'binario' que começa vazio, dpois vai somando como string, montando assim o num binario
                resto = numero % 2
                binario = str(resto) + binario
                # Aqui começa o novo ciclo de divisao pelo numero que ficou divido pelo inicial, ex: 34 // 2 = 17 dpois ent 17 % 2 e assim por diante
                numero = numero // 2        
        print(f'BINÁRIO: {binario}')

    if escolha == 2:
        octal = ''
        numero_octal = valor_decimal
        if numero_octal == 0:
            octal = '0'
        else:
            while numero_octal > 0:
                resto = numero_octal % 8
                octal = str(resto) + octal
                numero_octal = numero_octal // 8
        print(f'OCTAL: {octal}')

    if escolha == 3:
        hexa = ''
        numero_hexa = valor_decimal
        if numero_hexa == 0:
            hexa = '0'
        else:
            while numero_hexa > 0:
                resto = numero_hexa % 16
                if resto == 10:
                    subs_1 = 'A'
                    hexa = str(subs_1) + hexa
                elif resto == 11:
                    subs_2 = 'B'
                    hexa = str(subs_2) + hexa
                elif resto == 12:
                    subs_3 = 'C'
                    hexa = str(subs_3) + hexa
                elif resto == 13:
                    subs_4 = 'D'
                    hexa = str(subs_4) + hexa
                elif resto == 14:
                    subs_5 = 'E'
                    hexa = str(subs_5) + hexa
                elif resto == 15:
                    subs_6 = 'F'
                    hexa = str(subs_6) + hexa
                else:
                    hexa = str(resto) + hexa
                numero_hexa = numero_hexa // 16
        print(f'HEXADECIMAL:{hexa}')

input('\nPressione Enter para fechar o programa...')
