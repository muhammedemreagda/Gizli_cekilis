import random
import os

# Katılımcı isimleri
isimler = ["Mert", "Nisa", "Sude", "Tolga", "Emre", "Emirhan", "Sıla", "Zeynep", "Yavuz"]

def gizli_cekilis(isimler):
    if len(isimler) < 2:
        raise ValueError("Çekiliş yapmak için en az iki kişi olmalıdır.")
    
    # Orijinal listeyi kopyala ve karıştır
    alicilar = isimler.copy()
    random.shuffle(alicilar)
    
    # Eşleştirme döngüsü
    for i in range(len(isimler)):
        if isimler[i] == alicilar[i]:  # Kendi adını çektiyse
            # Pozisyon değişikliği yaparak sorunlu eşleşmeyi çöz
            swap_index = (i + 1) % len(isimler)
            alicilar[i], alicilar[swap_index] = alicilar[swap_index], alicilar[i]
    
    # Sonuçları eşleştirme olarak döndür
    hediyelesme = {isimler[i]: alicilar[i] for i in range(len(isimler))}
    return hediyelesme

# Çekilişi yap
sonuc = gizli_cekilis(isimler)

# Tüm isimlerin eşleşmesini tek tek göster
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
    print("Katılımcılar:", ", ".join(isimler))  # Kalan katılımcıları göster
    veren_kisi = input("\nHediyeleşeceğini öğrenmek istediğiniz ismi girin (çıkmak için '0'): ").strip()

    if veren_kisi == '0':  # Uygulamadan çık
        print("Uygulama kapatılıyor...")
        break
    elif veren_kisi in sonuc:
        print(f"\n{veren_kisi} -> {sonuc[veren_kisi]}")
        input("\nKonsolu temizlemek için Enter'a basın...")
    else:
        print("\nGirdiğiniz isim listede bulunmuyor. Tekrar deneyin!")
