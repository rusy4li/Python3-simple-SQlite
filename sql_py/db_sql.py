######
### Python ile database işlemleri
## SQlite
# Rusy4li
##############

### Notes:
# Bu program sadece pythonda database sqlite işlemlerini basitleştirmek amacıyla kodlanmıştır!
# DB browser SQlite programını indirip bilgisayarınıza kurarak oluşturmuş olduğum database dosyasını program üzerinden inceleyebilirsiniz!
####


# Kütüphaneler
try:
    import time, os, sqlite3
except ImportError:
    print(">>> 'time' modül hatası!")
    input(" Devam etmek için herhangi bir tuşa basın lütfen >> ")
try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
except ImportError:
    print(">>> 'colorama' modül hatası!")
    input(" Devam etmek için herhangi bir tuşa basın lütfen >> ")
try:
    from ek import banner
except ImportError:
    print(">>> 'banner' modül hatası!")
    input(" Devam etmek için herhangi bir tuşa basın lütfen >> ")



# Kullanıcı girdisi vs.. almak için fonksiyon oluşturuyoruz
def run(sayi):
    if (sayi == 1):
        print(" [!] Oluşturmak istediğiniz database'nin dosya adı ne olsun?")
        database_name_input = input(" > ")
        database_name_function = database_name_input + '.sqlite'
        print()
        return database_name_function
    elif (sayi == 2):
        print(" [!] Oluşturmak istediğiniz database'nin Tablosu ne olsun?")
        print(" [info] faturalar, kredi, users")
        database_tablo_input = input(" > ")
        print()
        return database_tablo_input
    elif (sayi == 3):
        print(" [!] Oluşturmak istediğiniz database'nin Tablosuna gireceğiniz verilere kategori belirleyin")
        print(" [info] son_odeme_tarihi, miktar, users_password")
        database_category_input = input(" > ")
        print()
        return database_category_input
    elif (sayi == 4):
        print(" [!] Oluşturmak istediğiniz database'nin Tablosuna verileri girin")
        print(" [!] Gireceğiniz verinin türünü yazın [int],[str]")
        database_category_value_types_input = input(" > ")
        print(" [!] Lütfen girmek istediğiniz veriyi yazın")
        if (database_category_value_types_input == "int"):
            database_category_value = int(input(" > "))
        else:
            database_category_value = input(" > ")
        print()
        return database_category_value
        



print(Fore.RED)

# Ekranı temizleyelim
os.system("cls")

print(banner)

# Run(1)
# Database adını öğreniyoruz
database_name = run(1)

# Database dosya adı belirliyoruz
database = database_name

# Döngü tekrara uğramaması için database oluşturulmuşmu diye kontrol ediyoruz
database_repeat = os.path.exists(database)

# Database'i oluşturuyoruz/ Bağlıyoruz
db = sqlite3.connect(database)

# İmlec oluşturuyoruz
click = db.cursor()

# Run(2)
# Database tablo adı belirliyoruz
database_tablo = run(2)

# Run(3)
# Database Kategori belirliyoruz
database_category = run(3)

# Tablo ve Kategori oluşturuyoruz 
## If not exist yazmak öenmli yoksa döngü buga girer!
click.execute(f"""CREATE TABLE IF NOT EXISTS {database_tablo}
({database_category})""")

# Run(4)
# Database Tablolara veri giriyoruz
database_category_value = run(4)

# Eğer dosya oluşturulmadı ise Oluşturduğumuz database'nin tablosuna verilere ekliyoruz
if not database_repeat:
    click.execute(f"""INSERT INTO {database_tablo} VALUES("{database_category_value}")""")

    # Save Fonksiyonu
    db.commit()

# sr değişkenine klasördeki tüm dosyaların adlarını atıyoruz
sr = os.listdir()

# Klasörde database dosyası oluşmuşmu diye kontrol ediyoruz
# Database check
if (database in sr):

    # Tablodaki tüm verileri seç
    click.execute(f"""SELECT * FROM {database_tablo}""")

    # Verileri değişkene atıyoruz fetchall() fonksiyonu ile
    database_db = click.fetchall()
else:
    print(" Hata!")
    time.sleep(5)

# Verileri yazdırıyoruz
print(" {0} ".format(database_db))
print()
print(" [!] Eğer bu database'yi nasıl DB browserdan yöneteceğinizi bilmiyor iseniz internetden araştırınız!")
print(" [!] Gerekli birçok şey için setup.py dosyasındaki notları okuyunuz!")

