print("""************************************
Kullanıcı Girişi
************************************
""")

sys_kullanici_adi = "mmustafa"
parola = "12345"

kullanici_adi = input("Kullanıcı adınız:")
kullanici_parola = input("Parolanız:")

if (kullanici_adi == sys_kullanici_adi and kullanici_parola != parola):
    print("Parola Hatalı...")
elif (kullanici_adi != sys_kullanici_adi and kullanici_parola == parola):
    print("Kullanıcı Adı Hatalı...")
elif (kullanici_adi != sys_kullanici_adi and kullanici_parola != parola):
    print("Kullanıcı Adı ve Parola Hatalı...")
else:
    print("Sisteme başarıyla giriş yapıldı...")
