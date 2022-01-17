#!/usr/bin/env python
# coding: utf-8

# ### Super Dígito 🤔
# 
# O super dígito de um número inteiro *x* é obtido da seguinte forma:
# 
# - Se *x* é composto por apenas um dígito, então, esse dígito é o super dígito de x.
# - Do contrário, o super dígito de *x* é igual ao super dígito da soma dos dígitos de x.
# 
# Perceba que, enquanto não chegarmos a um número composto por apenas **um dígito**, ainda não encontramos o super dígito de *x*.
# 
# Por exemplificar, o super dígito de 9875 é:
# 
# ```python
# super_digit(9875) = 9 + 8 + 7 + 5 = 29
# super_digit(29)   = 2 + 9 = 11
# super_digit(11)   = 1 + 1 = 2
# super_digit(2)    = 2
# ```
# 
# Portanto, no exemplo acima, se *x* for igual a 9875, o seu super dígito é igual a 2, pois calculamos o super dígito da soma dos seus dígitos, até que o resultado fosse apenas um número de apenas **um dígito**.
# 
# Sabendo disso, o seu desafio é o seguinte:
# 
# - você irá receber dois números do usuário, *n* e *k*. A partir desses dois números, você formará um novo número *p*, que será a concatenação no número *n*, *k* vezes. Por exemplo, se *n = 9875* e *k = 4*, *p = 9875 9875 9875 9875*; ou seja *p* é 9875, 4 vezes.
# 
# - Sabendo o valor de *p*, **calcule o seu super dígito por meio de uma função recursiva**.
# 
# Exemplo de entrada ||| Exemplo de saída
# ------------------ ||| ----------------
# 148 3              ||| 3
# 9875 4             ||| 8
# 123 3              ||| 9

# In[ ]:


def super_dig(p):
    if p <= 9:
        return p
    else:
        p_lista = list(str(p))
        lista_numeros = [int(numero) for numero in p_lista]
        soma = 0
        for num in lista_numeros:
            soma += num
        return super_dig(soma)


# In[ ]:


n = int(input('Digite o numero n: '))
k = int(input('Digite as repeticoes k: '))


# In[ ]:


n = str(n)
p = int(n*k)


# In[ ]:


saida = super_dig(p)
print(saida)


# In[ ]:




