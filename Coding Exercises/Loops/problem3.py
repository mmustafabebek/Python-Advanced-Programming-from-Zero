"""
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

*İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.*
"""

for i in range(1,11):
    print("*******************************************")
    for k in range(1,11):
        print("{} x {} = {}".format(i,k,i*k))
