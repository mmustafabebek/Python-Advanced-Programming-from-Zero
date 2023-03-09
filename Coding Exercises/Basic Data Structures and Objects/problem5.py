# Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

a = float(input("Birinci sayıyı giriniz:"))
b = float(input("İkinci sayıyı giriniz:"))

print("Değiştirilmeden Önce Değerler\na: {}\nb: {}\n".format(a,b))

a,b = b,a

print("Değiştirildikten Sonra Değerler\na: {}\nb: {}\n".format(a,b))