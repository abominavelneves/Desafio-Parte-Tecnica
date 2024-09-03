def PertenceFibo(numero):
    array=[0,1]
    while array[-1]<numero:
        next=array[-1]+array[-2]
        if next==numero:
            print('pertence')
            array.append(next)
            break
        elif next>numero:
            print('nao pertence')
        array.append(next)
PertenceFibo(34)