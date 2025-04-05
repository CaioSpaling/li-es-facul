from time import sleep
print('\033[;33m=-\033[m'*20)
nome = str(input('Olá usuário! Qual o seu nome? '.center(40)))
print('\033[;33m=-\033[m'*20)
print(f'Olá {nome}! Vamos trocar uma ideia sobre academia!'.center(40))
respcosta = input('Dentre esses exercícios para costas a seguir, qual o seu preferido? \na) Pull Down \nb) Pull Over \nc) Supino Inclinado \nd) Cruxifixo Inverso \n').lower()
if respcosta == ("a") and ("b"):
    print('Ótima escolha! É um ótimo exercício para esse agrupamento muscular!')
elif respcosta == ("d"):
    print('Bom exercício para posterior de ombro, mas pensando em costas no geral, existem melhores!')
elif respcosta == ("c"):
    print('???...')
    sleep(2)
    print('Amigão, até fiquei perdido, Supino é pra peito...')
else:
    print('Resposta Inválida!')
sleep(2)
print('\033[;33m=-\033[m'*20)
respeito = str(input('Qual o seu exercício preferido para peito? \na) Supino Reto \nb) Leg Press \nc) Cross Over na polia alta \nd) Crucifixo \n')).lower()
if respeito == ("a") and ("d"):
    print('Ótima escolha! São ótimos exercícios para o peitoral!')
elif respeito == ("c"):
    print('Uou! Bom exercício para a parte inferior do peitoral!')
elif respeito == ("b"):
    print('???...')
    sleep(2)
    print('Amigão, ta tudo bem? "leg" em inglês é perna...')
else:
    print('Resposta Inválida!')
print('\033[;33m=-\033[m'*20)
print('\033[;31mOBRIGADO\033[m').center(40)
print('\033[;33m=-\033[m'*20)