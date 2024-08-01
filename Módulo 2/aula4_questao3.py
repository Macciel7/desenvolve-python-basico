nome1 = input('Qual o nome do seu primeiro produto? ')
valor1 = float(input('Qual o valor do seu produto? '))
quantidade1 = int(input('Quantos desse produto você comprou? '))
valor1 = valor1 * quantidade1

nome2 = input('Qual o nome do seu segundo produto? ')
valor2 = float(input('Qual o valor do seu produto? '))
quantidade2 = int(input('Quantos desse produto você comprou? '))
valor2 = valor2 * quantidade2

nome3 = input('Qual o nome do seu terceiro produto? ')
valor3 = float(input('Qual o valor do seu produto? '))
quantidade3 = int(input('Quantos desse produto você comprou? '))
valor3 = valor3 * quantidade3

valor_total = valor1 + valor2 + valor3

print ('Total: R$', valor_total)