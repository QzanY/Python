#35

def perm(n):
    liste=[]
    for i in str(n):
        liste.append(i)
    lisste=[]
    for a in range(0,len(str(n))):
        liste.append(liste[0])
        liste.remove(liste[0])
        stri = ""
        for i in liste:
            stri+=i
        lisste.append(stri)
    return lisste
aranan=0
for i in range(1,1000000):
    kontrol=0
    for a in perm(i):
        if isprime(int(a))==1:
            kontrol+=1
    if kontrol==len(str(i)):
        aranan+=1
print(aranan)

#36

def ispalin(n):
    strn=str(n)
    l=len(strn)
    a=int(l/2)
    if strn[0 : a]==strn[::-1][0:a]:
        return True
    return False
palindromlar=[]
for i in range(1,1000000):
    if ispalin(i):
        if ispalin(int(str(bin(i))[2:])):
            palindromlar.append(i)
print(sum(palindromlar))

#37

def ltrunc(n):
    for i in range(0,len(str(n))):
        if n>9:
            if isprime(n):
                n=n//10
    if isprime(n):
        return True
    return False
def rtrunc(n):
    for i in range(0,len(str(n))):
        if n>9:
            if isprime(n):
                n=int(str(n)[1:])
    if isprime(n):
        return True
    return False
liste=[]
i=1
while True:
    if ltrunc(i)==1 and rtrunc(i)==1:
        liste.append(i)
    i+=1
    if len(liste)==15:
        break
liste.remove(2)
liste.remove(3)
liste.remove(5)
liste.remove(7)
print(sum(liste))

#38

def ispandig(n):
    rakamlar=[1,2,3,4,5,6,7,8,9]
    sayi=[]
    for i in str(n):
        sayi.append(int(i))
    if sorted(sayi)==rakamlar:
        return True
    return False
liste=[]
for i in range(1000,10000):
    a=i
    b=i*2
    ab=int(str(a)+str(b))
    if ispandig(ab):
        liste.append(ab)
for i in range(100,333):
    a=i
    b=i*2
    c=i*3
    abc=int(str(a)+str(b)+str(c))
    if ispandig(abc):
        liste.append(abc)
for i in range(10,100):
    a=i
    b=i*2
    c=i*3
    d=i*4
    abcd=int(str(a)+str(b)+str(c)+str(d))
    if ispandig(abcd):
        liste.append(abcd)
for i in range(1,10):
    a = i
    b = i * 2
    c = i * 3
    d = i * 4
    e = i * 5
    abcde = int(str(a) + str(b) + str(c) + str(d) + str(e))
    if ispandig(abcde):
        liste.append(abcde)
print(max(liste))

#39

cevreler={}
for b in range(1,500):
    for c in range(1,500-b):
        a=((b**2)+(c**2)) ** 0.5
        if a+b+c>1000:
            break
        if a==int(a):
            cevre=int(a)+b+c
            if cevre in cevreler:
                cevreler[cevre]+=1
            else:
                cevreler[cevre]=1
for n,v in cevreler.items():
    if v == max(cevreler.values()):
        print(n)
#40

n=1
sayi=""
while True:
    sayi+=str(n)
    if len(sayi)>1000000:
        break
    n+=1
print(int(sayi[0])*int(sayi[9])*int(sayi[99])*int(sayi[999])*int(sayi[9999])*int(sayi[99999])*int(sayi[999999]))

#41

def ispandig(n):
    assert len(n)<10
    rakamlar=[x for x in range(1,len(str(n))+1)]
    sayi=[]
    for i in str(n):
        sayi.append(int(i))
    if sorted(sayi)==rakamlar:
        return True
    return False
n=1

liste=[]
while n<10000000:
    if ispandig(n)==1 and isprime(n)==1:
        liste.append(n)
    n+=1
print(max(liste))

#42

liste=[]   # Kelimeler buraya eklenecek
trignum=[x*(x+1)//2 for x in range(1,30)]

harfl=string.ascii_uppercase
sozluk={}
for i in harfl:
    sozluk[i]=harfl.index(i)+1
aranan=0
for kelime in liste:
    value=0
    for harf in kelime:
        value+=sozluk[harf]
    if value in trignum:
        aranan+=1
print(aranan)

#43

def ispandig(n):
    rakamlar=[0,1,2,3,4,5,6,7,8,9]
    sayi=[]
    for i in str(n):
        sayi.append(int(i))
    if sorted(sayi)==rakamlar:
        return True
    return False
digits="0123456789"
numbers=permutations(digits)
numberlist=[int("".join(number)) for number in numbers if number[0]!="0"]
pdig=[]
for i in numberlist:
    a=str(i)
    if int(a[3])%2==0:
        if int(a[2:5])%3==0:
            if int(a[5])%5==0:
                if int(a[4:7])%7==0:
                    if int(a[5:8])%11==0:
                        if int(a[6:9]) % 13 == 0:
                            if int(a[7:10]) % 17 == 0:
                                if ispandig(i):
                                    pdig.append(i)
print(sum(pdig))

#44

def pentnum(n):
    return n*(3*n-1)//2
def ispn(x):
    return ((1 + (1 + 24 * x) ** (1/2))/6).is_integer()

for i in range(1,5000):
    num1=pentnum(i)
    for j in range(i-1,0,-1):
        num2=pentnum(j)
        if ispn((num1+num2))==1 and ispn(num1-num2)==1:
            print(num1-num2)
            break

#45

def ispn(x):
    return ((1 + (1 + 24 * x) ** (1/2))/6).is_integer()
def ishx(x):
    return ((((8*x+1)**0.5)+1)/4).is_integer()
def trignum(n):
    return n*(n+1)//2
def istrig(x):
    return ((((8*x+1)**0.5)-1)//2).is_integer()
liste=[]
for i in range(1,100000):
    t=trignum(i)
    if ispn(t)==1 and ishx(t)==1:
        liste.append(t)
print(liste)

#46

number=9
while True:
    if isprime(number) or number%2==0:
        number+=1
        continue
    kontrol=False
    n=1
    while number-(2*(n**2))>0:
        if isprime(number-(2*(n**2))):
            kontrol=True
            break
        else:
            n+=1
    if not kontrol:
        print(number)
        break
    number+=1

#47

def acarpan(n):
    carpanlar=set()
    i=2
    while i<n**0.5:
        if n%i==0:
            carpanlar.add(i)
            n=n//i
            i-=1
        i+=1
    return(len(carpanlar)+1)
a=2*3*5*7
while True:
    kontrol=True
    for i in range(4):
        if acarpan(a+i)!=4:
            kontrol=False
            break
    if kontrol:
        print(a)
        break
    a+=1

#48

s=0
for i in range(1,1001):
    s+=i**i
print(s%10**10)

#49 - 0.41382312774658203

primes=[]
for i in range(1000,10000):
    if isprime(i):
        primes.append(i)
asalpermler=[]
for sayi in primes:
    permler=list(permutations(str(sayi),4))
    for a in permler:
        a="".join(a)
        if int(a) in asalpermler:
            continue
        else:
            if a.startswith("0")==0:
                if isprime(int(a)):
                    asalpermler.append(int(a))
ucluler={}
for i in asalpermler:
    liste=[]
    for rakam in str(i):
        liste.append(rakam)
    liste=sorted(liste)
    sayi=int("".join(liste))
    if sayi not in list(ucluler.keys()):
        ucluler[sayi]=[i]
    else:
        ucluler[sayi].append((i))
gruplar=list(ucluler.values())
agruplar=[]
for grup in gruplar:
    if len(grup)>2:
        agruplar.append(grup)
for grup in agruplar:
    grup=sorted(grup)
    arananlar=set()
    for a in grup:
        for b in grup:
            if a!=b:
                if a-b==3330:
                    arananlar.add(a)
                    arananlar.add(b)
    if len(arananlar)==3:
        print(arananlar)

#50 - 0.7735745906829834

bass=1
primes=[]
while sum(primes)<1000000:
    if isprime(bass):
        primes.append(bass)
    bass+=1
sayilar=[]
for i in range(0,len(primes)):
    tekrar=0
    sayi=0
    liste=[]
    aranan=0
    for j in range(i,len(primes)):
        if sayi<1000000:
            sayi+=primes[j]
            tekrar+=1
            if isprime(sayi):
                liste.append([sayi,tekrar])
    maxx=0
    for a in liste:
        if a[1]>maxx:
            maxx=a[1]
            aranan=a[0]
    sayilar.append([aranan,maxx])
en=0
sayi=0
for b in sayilar:
    if b[1]>en:
        en=b[1]
        sayi=b[0]
print(sayi)

#51 - 0.8747873306274414

def trak(n):
    lis=[]
    for i in str(n):
        if int(i) not in lis:
            if str(n).count(i)>1:
                lis.append(int(i))
    return lis
def aile(n):
    liste=[]
    a=str(n)
    for trakam in trak(n):
        liss=[]
        for i in range(0,10):
            b=str(n).replace(str(trakam),str(i))
            liss.append(int(b))
        liste.append(liss)
    return liste
asallar=list(sieve.primerange(100000,1000000))
aaa=[]
for sayi in asallar:
    for a in aile(sayi):
        miktar=0
        for deneme in a:
            if isprime(deneme):
                miktar+=1
        if miktar==8:
            aaa.append(sayi)
            break
    if len(aaa)==2:
        break
print(aaa)

#52

def rakamlar(n):
    liste=[]
    for i in str(n):
        if int(i) not in liste:
            liste.append(int(i))
    return sorted(liste)

sayi=100000
while True:
    if rakamlar(sayi)==rakamlar(2*sayi):
        if rakamlar(sayi)==rakamlar(3*sayi):
            if rakamlar(sayi)==rakamlar(4*sayi):
                if rakamlar(sayi) == rakamlar(5 * sayi):
                    if rakamlar(sayi)==rakamlar(6*sayi):
                        print(sayi)
                        break
    sayi+=1

#53

count=0
for n in range(1,101):
    for r in range(1,n):
        a=factorial(n)/(factorial(r)*factorial(n-r))
        if a>1000000:
            count+=1
print(count)

#54 - 0.20396113395690918

# euler 54 coz.py

#55 - 0.12497115135192871

def revtop(n):
    a=int(str(n)[::-1])
    return a+n
def ispalin(n):
    strn=str(n)
    l=len(strn)
    a=int(l/2)
    if strn[0 : a]==strn[::-1][0:a]:
        return True
    return False
aranan=0
for sayi in range(1,10000):
    tekrar=0
    a=sayi
    while True:
        tekrar+=1
        a=revtop(a)
        if ispalin(a):
            break
        if tekrar>50:
            aranan+=1
            break
print(aranan)

#56 - 0.3124043941497803

max=0
for a in range(1,100):
    for b in range(1,100):
        top=0
        for i in str(a**b):
            top+=int(i)
        if top>max:
            max=top
print(max)

#57 - 0.0


a=3
b=2
kont=0
for i in range(999):
    a,b=a+2*b,a+b
    if len(str(a))>len(str(b)):
        kont+=1
print(kont)

#58 - 0.4530489444732666


k=1
liste=[1]
count=0
while True:
    k+=1
    lis=[]
    lis.append(((2*k-1)**2))
    lis.append(((2 * k - 1) ** 2)-2*(k-1))
    lis.append(((2 * k - 1) ** 2) - 4 * (k-1))
    lis.append(((2 * k - 1) ** 2) - 6 * (k-1))
    for i in lis:
        if isprime(i):
            count+=1
    for i in lis:
        liste.append(i)
    if count/len(liste)<0.1:
        print(2*k-1)
        break

#59 - 0.01503443717956543

liste=[] #Sayılar buraya yazılacak
def iseng(a,b):
    x=a^b
    if x>=32 and x<=122:
        return True
    else:
        return False
olasilar1=list()
for key in range(97,123):
    kont=True
    for i in range(0,len(liste),3):
        if not iseng(liste[i],key):
            kont=False
            break
    if kont==True:
        olasilar1.append(key)
print(olasilar1)
olasilar2=[]
for key in range(97,123):
    kont=True
    for i in range(1,len(liste),3):
        if not iseng(liste[i],key):
            kont=False
            break
    if kont==True:
        olasilar2.append(key)
print(olasilar2)
olasilar3=[]
for key in range(97,123):
    kont=True
    for i in range(2,len(liste),3):
        if not iseng(liste[i],key):
            kont=False
            break
    if kont==True:
        olasilar3.append(key)
print(olasilar3)
sonuclar=[]
for key1 in olasilar1:
    for key2 in olasilar2:
        for key3 in olasilar3:
            sonuc = ""
            for i in range(0,len(liste)):
                if i%3==0:
                    sonuc+=chr((liste[i]^key1))
                if i%3==1:
                    sonuc += chr((liste[i] ^ key2))
                if i%3==2:
                    sonuc += chr((liste[i] ^ key3))
            sonuclar.append(sonuc)
cevap=sonuclar[4]
toplam=0
for harf in cevap:
    toplam+=ord(harf)
print(toplam)

#60


#62 - 5.565

number = 100
cubes = []
aranan = []
while True:
    cube = number**3
    liste = sorted(list(str(cube)))
    cubes.append(liste)
    if cubes.count(liste)==5:
        aranan = liste
        break
    number += 1
print((cubes.index(aranan)+100)**3)

#63 - 30.000866413116455

bas=time()
i=1
counter=0
while True:
    j=1
    while True:
        a = i ** j
        if len(str(a))==j:
            counter+=1
            print(counter)
            j+=1
        else:
            break
    bb=time()
    if bb-bas>30:
        break
    i+=1

#67 - 0.65

with open("C:/Users/ozany/OneDrive/Masaüstü/Python/Project Euler/p067_triangle.txt","r") as file:
    liste = file.readlines()
    trig = []
    for line in liste:
        lin = line.split()
        linn = []
        for i in lin:
            linn.append(int(i))
        trig.append(linn)
    print(trig)
    for i in reversed(range(0,len(trig)-1)):
        for j in range(len(trig[i])):
            trig[i][j] += max(trig[i+1][j],trig[i+1][j+1])
    print(trig[0])

#71 - 0.509

kesirler = set()
q = 1000000
r = 0
s = 1
while q>2:
    p = (3*q-1)//7
    if r*q<p*s:
        r = p
        s = q
    q += -1
print(r,s)

#81 - 0.0

def minpath(grid,x,y,memo):
    if x == 0 and y == 0 :
        return grid[x][y]

    if (x,y) in memo:
        return memo[(x,y)]
    

    if x == 0:
        return minpath(grid,x,y-1,memo) + grid[x][y]
    
    if y == 0:
        return minpath(grid,x-1,y,memo) + grid[x][y]

    else:
        memo[(x,y)] = min(minpath(grid,x-1,y,memo),minpath(grid,x,y-1,memo)) + grid[x][y]
    return memo[(x,y)]

with open("p081_matrix.txt","r") as file:
    lines = file.readlines()
    grid = []
    for line in lines:
        rline = []
        sline = line.split(",")
        for num in sline:
            rline.append(int(num))
        grid.append(rline)
    print(minpath(grid,79,79,{}))


#85 - 0.728386640548706

mindeger = 1000000
aranan1=0
aranan2 =0
for i in range(1,1000):
    for j in range(1,1000):
        a = i*(i-1)/2
        b = j*(j-1)/2
        s = a*b
        if abs(s-2000000)<mindeger:
            mindeger = abs(s-2000000)
            aranan1 = i
            aranan2 = j
print((aranan1-1)*(aranan2-1))

#92 - 162.1910469532013

counter=0
for sayi in range(1,10**7):
    sayilar=[89,145,42,20,4,16,37,58]
    sayilar1=[1,44,32,13,10]
    liste=[]
    n=sayi
    while True:
        a=0
        for rakam in str(n):
            a+=int(rakam)**2
        liste.append(a)
        n=a
        if a in sayilar:
            liste.append(89)
            break
        if a in sayilar1:
            break
    if 89 in liste:
        counter+=1
print(counter)

#99 - 0.002034425735473633

with open("p099_base_exp.txt","r") as file:
    sayilarrr = file.readlines()
    sayilarr = []
    for sayii in sayilarrr:
        sayilarr.append(sayii.split("\n")[0])
    sayilar = []
    for sayi in sayilarr:
        s = sayi.split(",")
        k = [int(s[0]),int(s[1])]
        sayilar.append(k)
    maxd = 0
    index = 0
    aranan = 0
    s=[]
    for sayi in sayilar:
        index +=1
        num = sayi[1]*log(sayi[0])
        if num>maxd:
            maxd = num
            aranan = index
    print(aranan)
#205

liste1 = []
for a1 in range(1,5):
    for a2 in range(1,5):
        for a3 in range(1,5):
            for a4 in range(1,5):
                for a5 in range(1,5):
                    for a6 in range(1,5):
                        for a7 in range(1,5):
                            for a8 in range(1,5):
                                for a9 in range(1,5):
                                    liste1.append(a1+a2+a3+a4+a5+a6+a7+a8+a9)

liste2 = []
for b1 in range(1,7):
    for b2 in range(1,7):
        for b3 in range(1,7):
            for b4 in range(1,7):
                for b5 in range(1,7):
                    for b6 in range(1,7):
                        liste2.append(b1+b2+b3+b4+b5+b6)


counter = 0

numdict1 = dict()
for num in liste1:
    if num not in numdict1:
        numdict1[num] = 1
    else:
        numdict1[num] += 1

numdict2 = dict()
for num in liste2:
    if num not in numdict2:
        numdict2[num] = 1
    else:
        numdict2[num] += 1

for num1,index1 in numdict1.items():
    for num2,index2 in numdict2.items():
        if num1 > num2:
            counter += index1*index2

print(round(counter/((4**9)*(6**6)),7))

#214 - 1352.2676949501038

from sympy import primerange,primefactors

primes = primerange(1,40000000)
def totient(n):
    factors = primefactors(n)
    m = n
    for p in factors:
        m = m * (p-1)/p
    return(int(m))

summ = 0
for prime in primes:
    chain = 0
    temp = prime
    while temp != 1:
        temp= totient(temp)
        chain+=1
    if chain + 1 == 25:
        summ += prime
print(summ)

#357 - 34.9300448068

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2 * i, len(result), i):
                result[j] = False
    return result

liste = list_primality(100000001)
print("asallar ayarlandı")
total = 0
for i in range(2,100000001,4):
    kontrol=True
    if liste[i+1]==False:
        kontrol = False
    if kontrol:
        for j in range(1, int(math.sqrt(i))+1):
            if i % j == 0 and liste[j+i//j]== False:
                kontrol = False
                break
    if kontrol:
        total +=i

print(total)

#684 - Too much time

def s(n):
    str_num = ""
    remain = n
    while remain>9:
        str_num += "9"
        remain -= 9     
    num = str(remain) + str_num
    return int(num)


def fib(n):
    return int(((((1+(5**0.5))/2)**(n))-(((1-(5**0.5))/2)**(n)))/(5**0.5))%100000007


def S(k):
    if k<10:
        return int(k*(k+1)/2)
    else:
        q = k//9
        r = k%9
        return int(45+54*(((10**q-1)/9)-1)-9*(q-1)+(10**q)*(((r+1)*(r+2)/2)-1)-r)%1000000007

total = 0
for i in range(2,91):
    total += S(fib(i))%1000000007
print(total%1000000007)

#751 - 1.3077259063720703

def b(n,Q):
    if n==1:
        return Q
    else:
        return floor(b(n-1,Q))*(b(n-1,Q)-floor(b(n-1,Q))+1)

def a(n,Q):
    return floor(b(n,Q))

def concatenator(n,Q):
    num = ""
    num += str(a(1,Q))
    num += "."
    for i in range(2,n+1):
        num += str(a(i,Q))
    return(num)
    
print(concatenator(15,2.223561019313554106173177))

