r = 's'
total = 0
cont = 0

print('-'*40)
print(f'{" CONFERINDO VALORES ":=^40}')
print('-'*40)

while r == 's':
    cont+=1
    num = float(input('Digite valores: '))

    if cont == 1:
        maior=menor=num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    total+=num
    r = str(input('Deseja continuar [s/n]? ')).strip().lower()[0]
    print('~'*40)
media = total/cont

print('='*40)
print(f'O maior valor registrado foi {maior}!')
print(f'O menor valor registrado foi {menor}!')
print(f'A média dos valores registrados foi {media}!')
print('='*40)