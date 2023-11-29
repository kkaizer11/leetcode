#código feio mas funciona
def reverse(x):
    if x < -2147483648 or x > 2147483647:
        return 0
    # Funcional mas faltam os casos extremos
    neg = False
    if x < 0:
        x *= -1 
        neg = True
    linha = str(x)[::-1]
    if neg == True:
        if (int(linha) *-1) < -2147483648:
            return 0
        return int('-' + linha)
    else:
        if int(linha) > 2147483647:
            return 0
        return int(linha)


# num  = 1534236469
# z = reverse(num)
# print(z)
