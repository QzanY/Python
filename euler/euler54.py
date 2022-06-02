from math import *
from time import time
from sympy import *
from itertools import *
bas=time()

def puan(el1,el2):
    puanlar=[]
    maxozeller=[]
    for el in [el1,el2]:
        maxozel1=0
        maxozel2=0
        puann=0
        kartlar=el.split()
        degerle=list((kartlar[i][0]) for i in range(0,5))
        degerler=[]
        simgeler=set(kartlar[i][1] for i in range(0,5))
        for bn in range(0,5):
            if "T" in degerle:
                degerle.remove("T")
                degerle.append("10")
            if "J" in degerle:
                degerle.remove("J")
                degerle.append("11")
            if "Q" in degerle:
                degerle.remove("Q")
                degerle.append("12")
            if "K" in degerle:
                degerle.remove("K")
                degerle.append("13")
            if "A" in degerle:
                degerle.remove("A")
                degerle.append("14")
        for m in degerle:
            degerler.append(int(m))
        degerler=sorted(degerler)
        def ma(el):
            return max(degerler)
        if len(simgeler)==1 and [10,11,12,13,14]==degerler:
            puann=10
        else:
            a=0
            for u in range(0,4):
                if degerler[u+1]-degerler[u]==1:
                    a+=1
            if len(simgeler)==1 and a==4:
                puann=9
            elif len(simgeler)==1 and degerler==[2,3,4,5,14]:
                puann=9
            else:
                maxx=0
                aranan=0
                for i in degerler:
                    if degerler.count(i)>maxx:
                        maxx=degerler.count(i)
                        aranan=i
                maxozel1=aranan
                if maxx==4:
                    puann=8
                else:
                    ss=set()
                    sss=0
                    ssss=0
                    for i in degerler:
                        ss.add(degerler.count(i))
                        if degerler.count(i)==3:
                            sss=i
                        elif degerler.count(i)==2:
                            ssss=i
                    ss=sorted(ss)
                    maxozel1=sss
                    maxozel2=ssss

                    if ss== {2, 3}:
                        puann=7
                    else:
                        if len(simgeler)==1:
                            puann=6
                        else:
                            aa = 0
                            for i in range(0, 4):
                                if degerler[i + 1] - degerler[i] == 1:
                                    aa += 1
                            if aa == 4:
                                puann = 5
                            elif degerler==[2,3,4,5,14]:
                                puann=5
                            else:
                                sp = set()
                                for i in degerler:
                                    sp.add(degerler.count(i))
                                maxxx = 0
                                aranann = 0
                                for i in degerler:
                                    if degerler.count(i) > maxxx:
                                        maxxx = degerler.count(i)
                                        aranann = i
                                maxozel1=aranann
                                if 3 in sp and 2 not in sp:
                                    puann=4
                                else:
                                    spp = list()
                                    for i in degerler:
                                        spp.append(degerler.count(i))
                                    lisp=set()
                                    for j in degerler:
                                        if degerler.count(j)==2:
                                            lisp.add(j)
                                    if len(lisp)>0:
                                        maxozel1=max(lisp)
                                        maxozel2=min(lisp)

                                    if spp.count(2)==4:
                                        puann=3
                                    else:
                                        spq = list()
                                        for i in degerler:
                                            spq.append(degerler.count(i))
                                        spq=sorted(spq)
                                        lisk=0
                                        for l in degerler:
                                            if degerler.count(l) == 2:
                                                lisk=l
                                        maxozel1=lisk

                                        if spq==[1,1,1,2,2]:
                                            puann=2
                                        else:
                                            puann=max(degerler)/10
                    
        puanlar.append(puann)
        maxozeller.append(maxozel1)
        maxozeller.append(maxozel2)
    if puanlar[0]>puanlar[1]:
        return 1
    if puanlar[0]< puanlar[1]:
        return 0
    if puanlar[0]==puanlar[1]:
        if puanlar[0]==8 and puanlar[1]==8:
            if maxozeller[0]>maxozeller[2]:
                return 1
            elif maxozeller[0]<maxozeller[2]:
                return 0
            else:
                if maxozeller[0]>maxozeller[2]:
                    return 1
                elif maxozeller[0]<maxozeller[2]:
                    return 0
                else:
                    if maxozeller[1]>maxozeller[3]:
                        return 1
                    elif maxozeller[1]<maxozeller[3]:
                        return 0
                    else:
                        if maxozeller[0]>maxozeller[2]:
                            return 1
                        elif maxozeller[0]<maxozeller[2]:
                            return 0
                        else:
                            if maxozeller[0]>maxozeller[2]:
                                return 1
                            elif maxozeller[0]<maxozeller[2]:
                                return 0
                            else:
                                if maxozeller[1]>maxozeller[3]:
                                    return 1
                                elif maxozeller[1]<maxozeller[3]:
                                    return 0
                                else:
                                    if maxozeller[0]>maxozeller[2]:
                                        return 1
                                    elif maxozeller[0]<maxozeller[2]:
                                        return 0
                                    else:
                                        if ma(el1)>ma(el2):
                                            return 1
                                        else:
                                            return 0
        if puanlar[0]==7 and puanlar[1]==7:
            if maxozeller[0]>maxozeller[2]:
                    return 1
            elif maxozeller[0]<maxozeller[2]:
                return 0
            else:
                if maxozeller[1]>maxozeller[3]:
                    return 1
                elif maxozeller[1]<maxozeller[3]:
                    return 0
                else:
                    if maxozeller[0]>maxozeller[2]:
                        return 1
                    elif maxozeller[0]<maxozeller[2]:
                        return 0
                    else:
                        if maxozeller[0]>maxozeller[2]:
                            return 1
                        elif maxozeller[0]<maxozeller[2]:
                            return 0
                        else:
                            if maxozeller[1]>maxozeller[3]:
                                return 1
                            elif maxozeller[1]<maxozeller[3]:
                                return 0
                            else:
                                if maxozeller[0]>maxozeller[2]:
                                    return 1
                                elif maxozeller[0]<maxozeller[2]:
                                    return 0
                                else:
                                    if ma(el1)>ma(el2):
                                        return 1
                                    else:
                                        return 0
        if puanlar[0] == 4 and puanlar[1] == 4:
            if maxozeller[0]>maxozeller[2]:
                return 1
            elif maxozeller[0]<maxozeller[2]:
                return 0
            else:
                if maxozeller[0]>maxozeller[2]:
                    return 1
                elif maxozeller[0]<maxozeller[2]:
                    return 0
                else:
                    if maxozeller[1]>maxozeller[3]:
                        return 1
                    elif maxozeller[1]<maxozeller[3]:
                        return 0
                    else:
                        if maxozeller[0]>maxozeller[2]:
                            return 1
                        elif maxozeller[0]<maxozeller[2]:
                            return 0
                        else:
                            if ma(el1)>ma(el2):
                                return 1
                            else:
                                return 0
        if puanlar[0] == 3 and puanlar[1] == 3:
            if maxozeller[0]>maxozeller[2]:
                return 1
            elif maxozeller[0]<maxozeller[2]:
                return 0
            else:
                if maxozeller[1]>maxozeller[3]:
                    return 1
                elif maxozeller[1]<maxozeller[3]:
                    return 0
                else:
                    if maxozeller[0]>maxozeller[2]:
                        return 1
                    elif maxozeller[0]<maxozeller[2]:
                        return 0
                    else:
                        if ma(el1)>ma(el2):
                            return 1
                        else:
                            return 0
        if puanlar[0] == 2 and puanlar[1] == 2:
            if maxozeller[0]>maxozeller[2]:
                return 1
            elif maxozeller[0]<maxozeller[2]:
                return 0
            else:
                if ma(el1)>ma(el2):
                    return 1
                else:
                    return 0
        

with open("euler54.txt") as eul:
    liste=eul.readlines()
    lis=[]
    for el in liste:
        lis.append(el[0:29])
    counter=0
    for oyun in lis:
        oy1=oyun[0:14]
        oy2=oyun[15:29]
        if puan(oy1,oy2)==1:
            counter+=1
    print(counter-1)
sona=time()
print(sona-bas)
