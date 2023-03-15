"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
"""

def ebob_bulma(sayi1,sayi2):
    i = 1
    ebob = 1
    while(i <= sayi1 and i <= sayi2):
        if(not(sayi1 % i) and not(sayi2 % i)):
            ebob = i
        i += 1
    return ebob

sayi1 = int(input("Sayı1 :"))
sayi2 = int(input("Sayı2 :"))

print("EBOB :",ebob_bulma(sayi1,sayi2))
