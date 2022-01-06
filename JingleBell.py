dict_jingle = {
    'W': 1 ,
    'H': 1/2 ,
    'Q': 1/4 ,
    'E': 1/8,
    'S': 1/16,
    'T': 1/32,
    'X': 1/64
}

compass = input('Digite aqui os compassos a serem verificados: ').upper()

lista_compass = compass.strip('/').split('/')
incorretos = []


cont = 0
for i in lista_compass:
    comp = list(i)
    sum = 0
    for j in comp:
        sum += dict_jingle[j]
    if sum == 1:
        cont += 1
    else:
        incorretos.append(i)
print(f'Quantidade de corretos: {cont} \nIncorretos: {incorretos}')

