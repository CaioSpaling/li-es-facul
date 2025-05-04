print('='*60)
print('Esses são todos os números ímpares entre 100 e 200!')
print('='*60)

cont = 0

for i in range(101,200, 2):
    cont+=1
    print(f' {i} |', end='')
    if cont % 10 == 0:
        print('\n')
print('='*60)