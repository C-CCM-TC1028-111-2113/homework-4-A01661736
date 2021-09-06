
def main():
    #Escribe tu código debajo de esta línea
    height=int(input("Enter triangle height: "))

    n=1
    c=height

    base="*"
    i=" "   
    
    while ( (len (base))<=height):
        while n<=c:
            i=" "
            c=c-1
            i=i*(c)
            break
            
        print(str(i)+str(base))
        base=base+"*"
        
        continue
    pass


if __name__=='__main__':
    main()
