#Pede o comprimento do terreno e converte em número inteiro
comprimento = int(input('Me diga o comprimento do terreno: '))
#Pede a largura do terreno e converte em número inteiro
largura = int(input('Me diga a largura do terreno: '))
#Pede o preço do m² e converte em número decimal
preco = float(input('E qual o preço do m² da sua região? '))
#Fórmula de área
area = comprimento * largura
#Fórmula do preço total
preco_total = preco * area
print ('O terreno possui', area, 'm² e custa R$', float(preco_total))