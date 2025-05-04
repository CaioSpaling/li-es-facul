contg_negt = 0
for n in range(1, 8):
    val = float(input('Digite um valor: '))
    if val < 0:
        contg_negt+=1
print(f'Você digitou {contg_negt} valores negativos!')        