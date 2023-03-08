from ast import Str
from datetime import date, datetime
from struct import pack
from unicodedata import digit
from random import *
#käivitamisel täidetakse kaks nimekirja: taotlejad[], punktid[]
def patsiendid(i:list,v:list):
    """
    funktsioon mis lisab järjendusele nimesid ja teise järjendusele paneb random
    """
    n=int(input("Mitu inimest?"))
    for j in range(n):
        nimi=input("sisesta nimi")
        vitamiini=randint(10,100)
        i.append(nimi)
        v.append(vitamiini)
    return i,v
def suur_vaike(i:list,v:list):
    """
    leiab numbrid, mis on <30
    """
    number=30
    for m in v:
        if m < number:
            ind=v.index(m)
            print(f"{m}, {i[ind]}")
def keskmine(i:list,v:list):
    """
    kõik plussib, jagab kogus
    """
    kesk_d=sum(v)/len(v)
    print(f"on keskmine d vitamiini näitleja {kesk_d}")
    return i,v
def suurim_d_vitamiin(i:list,v:list):
    """
    teeb max vitamiini arvu ja leiab palk indeksid ja nimi indeksid
    """
    palk=max(v)
    ind=v.index(palk)
    nimi=i[ind]
    return palk,nimi
def search_patients_by_name(nimed, d_vitamiini_sisaldus):
    """
    ==nimi järjendusega
    """
    
    nimi = input("sissesta nimi ")
    for i in range(len(nimed)):
        if nimed[i].lower() == nimi.lower():
            print("leidud pacient:", nimed[i], d_vitamiini_sisaldus[i])
def redact(i:list,v:list):
    """
    paneb esimesele tähele järjenduses i ja teeb seda suur täht,pärast seda lisab igale nimise esimene suur täht
    """
    ind=i.index[0]
    i[0].isupper()+i[1:]
    return i
