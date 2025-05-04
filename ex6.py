print('='*20)
print('Tabuada!')

r = 's'

while r == 's':
    print('='*20)
    tab = int(input('Digite um número: '))
    print('='*20)
    
    for t in range(1,11):
        print(f'{tab} x {t} = {tab*t}')
    print('='*20)
    
    r = str(input('Deseja repetir [s/n]? '))
    print('='*20)