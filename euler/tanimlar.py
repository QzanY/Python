from math import *
import random
def isprime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def ispalin(n):
    strn=str(n)
    if strn == strn[::-1]:
        return True
    return False

def ispandig(n):
    assert len(n)<10
    rakamlar=[x for x in range(1,len(str(n))+1)]
    sayi=[]
    for i in str(n):
        sayi.append(int(i))
    if sorted(sayi)==rakamlar:
        return True
    return False

def carpanlar(n):
    carpan=list()
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            carpan.append(i)
            if n//i != i:
                carpan.append(n//i)
    return(carpan)
