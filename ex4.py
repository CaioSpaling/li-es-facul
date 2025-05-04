print('='*40)
print('MAIOR E MENOR ALTURA')

cont=0

for a in range(1,16):
    cont+=1
    
    print('='*40)
    alt = int(input('Digite sua altura (cm): '))

    if cont == 1:
        maior = menor = alt
    if alt > maior:
        maior = alt 
    if alt < menor:
        menor = alt

print(f'A maior altura registrada foi {maior}cm!')
print(f'A menor altura registrada foi {menor}cm!')