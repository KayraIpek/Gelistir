# menu_modulu.py
class MenuSistemi:

    @staticmethod
    def karsilama(program_adi):
        print(f"\n{program_adi} programına hoş geldiniz!\n")

    @staticmethod
    def menuOlustur(menu_map):
        # ... (menü oluşturma mantığı)
        numbered_options = {}
        for i, (description, func_obj) in enumerate(menu_map.items(), 1):
            print(f"{i}. {description}")
            numbered_options[str(i)] = func_obj

        cikis_numarasi = str(len(menu_map) + 1)
        print(f"{cikis_numarasi}. Çıkış")

        secim = input("Bir seçenek giriniz: ")

        if secim in numbered_options:
            return numbered_options[secim]
        elif secim == cikis_numarasi:
            return "EXIT"
        else:
            print("Geçersiz bir seçim yaptınız.")
            return None

    @staticmethod
    def menuyuCalistir(menu_map):
        while True:
            secim = MenuSistemi.menuOlustur(menu_map)

            if secim == "EXIT":
                print("Programdan çıkılıyor...")
                break
            elif secim:
                # Seçilen fonksiyonu çalıştır
                secim()
                print()
                print("----------MENU-----------")

# Artık 'karsilama' fonksiyonuna ihtiyacımız yok, onu MenuSistemi'ne taşıdık.
# if __name__ == "__main__": bloğu bu dosyadan tamamen kaldırılmıştır.