genero = input('Qual o seu gênero? (M ou F): ')
idade = int(input('Qual a sua idade?: '))
servico = int(input('E o seu tempo de serviço? (Em anos): '))

if genero == 'M':
    if idade >= 65 or servico >= 30 or idade >= 65 and servico >= 25:
        print ('Você já pode se aposentar')
    else:
        print('Você ainda não pode se aposentar')

elif genero == 'F':
    if idade >= 60 or servico >= 30 or idade >= 60 and servico >= 25:
        print ('Você já pode se aposentar')
    else:
        print('Você ainda não pode se aposentar')