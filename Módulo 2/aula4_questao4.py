#entrada
valor = int(input('Digite o valor: '))
#processamento

##Começar com a maior nota
notas_100 = valor // 100
##Atualizar quanto falta depois da nota
valor = valor % 100
print (notas_100, 'nota(s) de R$100,00')

notas_50 = valor // 50
##Atualizar quanto falta depois da nota
valor = valor % 50
print (notas_50, 'nota(s) de R$50,00')

notas_20 = valor // 20
##Atualizar quanto falta depois da nota
valor = valor % 20
print (notas_20, 'nota(s) de R$20,00')

notas_10 = valor // 10
##Atualizar quanto falta depois da nota
valor = valor % 10
print (notas_10, 'nota(s) de R$10,00')

notas_5 = valor // 5
##Atualizar quanto falta depois da nota
valor = valor % 5
print (notas_5, 'nota(s) de R$5,00')

notas_2 = valor // 2
##Atualizar quanto falta depois da nota
valor = valor % 2
print (notas_2, 'nota(s) de R$2,00')

notas_1 = valor // 1
##Atualizar quanto falta depois da nota
valor = valor % 1
print (notas_1, 'nota(s) de R$1,00')

#saída