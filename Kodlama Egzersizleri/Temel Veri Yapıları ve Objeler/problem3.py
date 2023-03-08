"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini
gerektiğini hesaplayın.
"""

kmbasinayakma = float(input("Aracın kilometrede yaktığı miktar:"))
kmyol = int(input("Aracın km olarak yaptığı yol:"))

print("Tutar: {} tl".format(kmbasinayakma * kmyol))