#ćwiczenia z rozdziału 15
def ile_pol(n):
    return n*n

def ile_kolorowych(n, kolor):
    if (kolor == "c"):
        return (n*n-1)//2+1
    elif (kolor == "b"):
        return n*n//2
    else:
        print("zły parametr")

def ile_wieza(n,x,y):
    return (n-1)*2
    
def testuj_szachownice(n):
    for n in range(2,n+1):
        print(n, ile_pol(n), ile_kolorowych(n, "b"), ile_kolorowych(n, "c"))

def ile_goniec(n,x,y):
    return min(x-1, n-y) + min(x-1, y-1) + min(n-x, y-1) + min(n-x, n-y)

def ile_hetman(n,x,y):
    return ile_goniec(n,x,y)+ile_wieza(n,x,y)

def zestawienie_hetman(x,y):
    for x in range(1,x+1):
        for y in range(1,y+1):
            print(ile_hetman(n,x,y)," ", end="")
        print("")

def ile_krol(n,x,y):
    if(x==1 or x==n):
        if(y==1 or y==n):
            return 3
        else:
            return 5
    elif(y==1 or y==n):
        return 5
    else:
        return 9

def ile_skoczek(n,x,y):
    liczbaPol = 0
    if(x+2<=n and x+2>0 and y+1<=n and y+1>0): liczbaPol+=1
    if(x+2<=n and x+2>0 and y-1<=n and y-1>0): liczbaPol+=1
    if(x-2<=n and x-2>0 and y+1<=n and y+1>0): liczbaPol+=1
    if(x-2<=n and x-2>0 and y-1<=n and y-1>0): liczbaPol+=1
    if(x+1<=n and x+1>0 and y+2<=n and y+2>0): liczbaPol+=1
    if(x+1<=n and x+1>0 and y-2<=n and y-2>0): liczbaPol+=1
    if(x-1<=n and x-1>0 and y+2<=n and y+2>0): liczbaPol+=1
    if(x-1<=n and x-1>0 and y-2<=n and y-2>0): liczbaPol+=1
    return liczbaPol

n = int(input("Podaj jeden wymiar szachownicy z zakresu <2,32>: "))
x = int(input("Podaj współrzędne X figury: "))
y = int(input("Podaj współrzędne Y figury: "))
if n>32 or n<2 or x>n or y>n:
    print("błąd danych")
else:
    print("Iość pól szachownicy: ", ile_pol(n))
    print("Ilość pól czarnych: ", ile_kolorowych(n, "c"))
    print("Ilość pól czarnych: ", ile_kolorowych(n, "b"))
    testuj_szachownice(n)
    print("Ile pól atakuje wieża", ile_wieza(n,2,2))
    print("Ile pól atakuje goniec", ile_goniec(n,x,y))
    print("Ile pól atakuje hetman", ile_hetman(n,x,y))
    zestawienie_hetman(n,n)
    print("Ile pól atakuje król", ile_krol(n,x,y))
    print("Ile pól atakuje skoczek", ile_skoczek(n,x,y))
