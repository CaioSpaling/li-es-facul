print('Aqui estão todos os números ímpares de 1 a 500 que são divisiveis por 3!')
total = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        total+=i
        print(f'| {i} |', end='')
print(' cabô!\n', end='')
print('='*40)
print(f'A soma de todos esses valores é {total}')
print('='*40)