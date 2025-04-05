from time import sleep
print('\033[;33m=-\033[m'*20)
nome = str(input('Olá usuário! Qual o seu nome? '.center(40)).title())
print('\033[;33m=-\033[m'*20)
print(f'Olá {nome}! Vamos trocar uma ideia sobre academia!'.center(40))
respcosta = input('Dentre esses exercícios para costas a seguir, qual o seu preferido? \n\033[;36ma)\033[m Pull Down \n\033[;36mb)\033[m Pull Over \n\033[;36mc)\033[m Supino Inclinado \n\033[;36md)\033[m Cruxifixo Inverso \n').lower()
if respcosta == "a" or respcosta == "b":
    print('\033[;34mÓtima escolha!\033[m É um ótimo exercício para esse agrupamento muscular!')
elif respcosta == "d":
    print('Bom exercício para posterior de ombro, mas pensando em costas no geral, \033[;32mexistem melhores!\033[m')
elif respcosta == "c":
    print('\033[;35m???...\033[m')
    sleep(2)
    print('Amigão, até fiquei perdido, \033[;31mSupino é pra peito...\033[m')
else:
    print('\033[;31mResposta Inválida!\033[m')
sleep(2)
print('\033[;33m=-\033[m'*20)
respeito = str(input('Qual o seu exercício preferido para peito? \n\033[;36ma)\033[m Supino Reto \n\033[;36mb)\033[m Leg Press \n\033[;36mc)\033[m Cross Over na polia alta \n\033[;36md)\033[m Crucifixo \n')).lower()
if respeito == "a" or respeito == "d":
    print('\033[;34mÓtima escolha!\033[m É um ótimo exercício para o peitoral!')
elif respeito == "c":
    print('\033[;35mUou!\033[m Bom exercício para a parte inferior do peitoral!')
elif respeito == "b":
    print('\033[;35m???...\033[m')
    sleep(2)
    print('Amigão, ta tudo bem? \033[;31m"LEG" em inglês é perna...\033[m')
else:
    print('\033[;31mResposta Inválida!\033[m')
print('\033[;33m=-\033[m'*20)
if respcosta == "a" or respcosta == "b" and respeito == "a" or respeito == "d":
    print('\033[;32mOBRIGADO PELAS RESPOSTAS!\033[m'.center(54))
else:
    print('\033[;31mVOCÊ É HORRÍVEL!\033[m'.center(54))
print('\033[;33m=-\033[m'*20)
