def main():
    #escribe tu código abajo de esta línea
    print ("Choose the 'n' value: ")
    n=int(input())
    b=0
    i=1
    while i<n:
        
        b=i+1
        print (str(i),"#")
        print (str(b),"%")
        i=i+2
        continue
    if (n%2!=0):
        
        print (str(n),"#")
    
    
    
    
    
    pass

if __name__=='__main__':   
    main()
