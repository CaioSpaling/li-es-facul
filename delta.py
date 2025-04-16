from datetime import date
from datetime import datetime
from time import sleep
print('='*47)
print("\033[;32mDELTA SUPERMERCADOS\033[m".center(54))
print('='*47)
print('Estamos com uma promoção nos supermercados Delta!')
sleep(2)
dta = datetime.today()
dm_f = str(datetime.strftime(dta, "%d/%m"))
ano_f = int(datetime.strftime(dta, "%Y"))
valor = float(input('Digite o valor da sua compra: '))
if valor>=100:
    clube = str(input('Você é membro do clube Delta? ')).lower()
    nasc = input('Digite sua data de nascimento (dd/mm/aaaa): ')
    nasc_f = datetime.strptime(nasc, "%d/%m/%Y") #datetime.strptime(obj, format) para transformar uma string para formato data
    dm_cons_f = datetime.strftime(nasc_f, "%d/%m") #datetime.strftime(obj_f, format) para usar para comparar, printar etc.
    ano_cons_f = int(datetime.strftime(nasc_f, "%Y"))
    if clube == "sim" and dm_cons_f == dm_f:
        print(f'Você pagará {valor - 15}')
    elif clube == "sim" and dm_cons_f != dm_f or ano_cons_f - ano_f >= 60:
        print(f'Você pagará R${valor-10}')
    else:
        print(f'Você pagará R${valor}!')
else:
    print(f'Você pagará {valor}!')
print('='*47)
print('\033[;32mOBRIGADO POR COMPRAR NO DELTA!\033[m'.center(54))
print('\033[;32mVOLTE SEMPRE!\033[m'.center(54))
print('='*47)


    