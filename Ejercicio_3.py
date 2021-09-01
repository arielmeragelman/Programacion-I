

def sumador(*args):
    total=0
    for valor in args:
        total=valor+total
    print("(1) - EL TOTAL ES:"+str(total))
    print("(2) - EL TOTAL ES:"+str(total))


sumador(2,-1,8)