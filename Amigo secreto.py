#!/usr/bin/env python
# coding: utf-8

# ### Amigo Secreto ⛄
# 
# Na família Natalícia já é tradição a realização do amigo secreto (ou amigo oculto) na véspera de natal. Todos os anos a família inteira se reune para a troca de presentes. É um momento de muita diversão e descontração.
# 
# Neste ano, a caçula Jocelina resolveu deixar o momento ainda mais divertido: ela propôs que todos os participantes colocassem em uma lista 3 sugestões para presentes. A partir dessa lista ela pensou em montar um programa que, colocado um nome **N** e um presente **P**, o programa retorna se a pessoa acertou ou não no presente para seu amigo secreto.
# 
# Só que Joce não sabe muito de programação, e acabou precisando de ajuda para montar esse programa. Você, sendo tomado(a) pelo espírito natalino, aceitou o desafio!
# 
# #### Entrada
# 
# ```
# 5
# iara mochila estojo lapis
# adelar sapato camisa carteira
# jessica agenda bolsa brincos
# jocelina xicara meias perfume
# elaine sandalia sapatilha camiseta
# jessica carteira
# jessica agenda
# iara sandalia
# elaine mochila
# iara mochila
# adelar carteira
# ```
# 
# #### Saída
# ```
# Tente Novamente!
# Uhul! Seu amigo secreto vai adorar o/
# Tente Novamente!
# Tente Novamente!
# Uhul! Seu amigo secreto vai adorar o/
# Uhul! Seu amigo secreto vai adorar o/
# ```

# In[ ]:


numero_pessoas = int(input('Digite a quantidade de participantes: '))


# In[ ]:


sugestoes = {}

n = 1
while n <= numero_pessoas:
    entrada = input(f'Digite o nome do participante {n} e as sugestoes de presente: ').split(' ')
    sugestoes[entrada[0]] = [ entrada[1], entrada[2], entrada[3] ]
    n += 1


# In[ ]:


presentear = input('Digite o nome do seu amigo secreto e o presente que comprou: ').split(' ')


# In[ ]:


if presentear[1] in sugestoes[presentear[0]]:
    print('Uhul! Seu amigo secreto vai adorar o/')
else:
    print('Tente Novamente!')


# In[ ]:




