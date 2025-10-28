from menu_modulu import MenuSistemi

def ustveri(lisansadi):
    eserAdi = input("Eser Adı: ")
    eserSahibi = input("Eser Sahibi: ")
    eserTarihi = input("Eser Tarihi (YYYY): ")
    if lisansadi=="CC0 1.0":
      print(f"{eserAdi} by {eserSahibi} is marked CC0 1.0 ")
    else:
      print(f"{eserAdi} © {eserTarihi} by {eserSahibi} is licensed under {lisansadi}")

def zeropd():
    print("CC0 Sıfır (Zero): Kamu Malı tahsisi olarak kullanılır. Kullanımda olan son sürümü 1.0’dır. Resmi olarak Türkçe çevirisi yayınlanmıştır. Bu lisans kapsamında telif hakkı sınırlaması yoktur, kaynak atıf vermeden ticari amaç da dahil olmak üzere kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri("CC0 1.0")
    
def ccby():
    print("CC BY Atıf (Attribution): CC’nin en özgür lisansıdır. Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç da dahil olmak üzere kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri("CC BY 4.0")
    

def ccbysa():
    print("CC BY-SA Atıf-AynıLisanslaPaylaş (Attribution-ShareAlike): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek ve aynı lisansı devam ettirmek kaydıyla ticari amaç da dahil olmak üzere kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir")
    ustveri("CC BY-SA 4.0")

   

def ccbynd():
    print("CC BY-ND Atıf-Türetilemez (Attribution-NonDerivative): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç da dahil olmak üzere kopyalanabilir, dağıtılabilir ve yeniden kullanılabilir ancak üzerinde hiçbir değişiklik yapılamaz.")
    ustveri("CC BY-ND 4.0")
     

def ccbync():
    print("CC BY-NC Atıf-GayriTicari (Attribution-NonCommercial): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç haricinde kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri("CC BY-NC 4.0")
     

def ccbyncsa():
    print("CC BY-NC-SA Atıf-GayriTicari-AynıLisanslaPaylaş (Attribution-NonCommercial-ShareAlike): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek ve aynı lisansı devam ettirmek kaydıyla ticari amaç haricinde kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri("CC BY-NC-SA 4.0")
     

def ccbyncnd():
    print("CC BY-NC-ND Atıf-GayriTicari-Türetilemez (Attribution-NonCommercial-NonDerivative): CC’nin en az özgürlük sağlayan lisansıdır. Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç haricinde kopyalanabilir, dağıtılabilir ve yeniden kullanılabilir, ancak üzerinde hiçbir değişiklik yapılamaz.")
    ustveri("CC BY-NC-ND 4.0")
     

menu = MenuSistemi()
menu.karsilama("CC Lisans Seç")

# Menü öğelerini ve karşılık gelen fonksiyonları bir sözlükte tanımlayın
# Anahtar: Menüde görünecek açıklama, Değer: Çağrılacak fonksiyon nesnesi
menu_items = {
    "Kamu Malı / Public Domain": zeropd,
    "CC BY": ccby,
    "CC BY-SA": ccbysa,
    "CC BY-ND": ccbynd,
    "CC BY-NC": ccbync,
    "CC BY-NC-SA": ccbyncsa,
    "CC BY-NC-ND": ccbyncnd
}

menu.menuyuCalistir(menu_items)