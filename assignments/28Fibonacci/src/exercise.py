
def main():
    #escribe tu código abajo de esta línea
    print("Indica el índice que se desea calcular de la serie de Fibonacchi.")
    ind=int(input())

    a=0   #primer número
    b=1   #segundo número

    c=1   #índice actual
    r=0   #resultado de la suma de los dos números
    
    while c<ind:
        r=a+b
        a=b
        b=r

        c=c+1
    print (str(r))
    pass

if __name__=='__main__':
    main()
