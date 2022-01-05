def get_max_number(list_integers):

    if len(list_integers) == 1:
        print(list_integers[0])
        return list_integers[0]

    elif(list_integers[0] < list_integers[-1]):
        list_integers[0] = list_integers.pop()
        return get_max_number(list_integers)

    else:
        return get_max_number(list_integers[:-1])

max_number = get_max_number([999999,32,2,99,8,7,864684684684, 98, 34, 74,777777777, 66, 27, 32,77,8985,99,22,1998])
