r = 's'
total_sal = 0
total_filhos = 0
maior = 0
cont_sal_1000 = 0
total_pessoas = 0

while r == "s":
    print('='*40)
    sal = float(input('Digite seu salário: R$'))
    filhos = int(input('Digite o número de filhos que possui: '))
    print('='*40)
    
    if sal>maior:
        maior=sal
    if sal<=1000:
        cont_sal_1000+=1
    total_pessoas+=1
    total_sal+=sal
    total_filhos+=filhos
    
    r = str(input('Deseja continuar [s/n]? ')).lower().strip()[0]

perc_1000 = (cont_sal_1000/total_pessoas)*100
media_filhos = total_filhos/total_pessoas
media_sal = total_sal/total_pessoas

print('='*40)    
print(f'A média salarial da população é R${media_sal}!')
print(f'A média de filhos registrada por pessoa é {media_filhos:.0f} filhos!')
print(f'O maior salário registrado foi de R${maior}!')
print(f'O percentual de pessoas que recebe até R$1000 é {perc_1000}%!')
print('='*40)
