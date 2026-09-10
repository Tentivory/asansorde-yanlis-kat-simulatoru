#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde Yanlış Kat Simülatörü

Bu yazılım, modern insanın asansör düğmesine bakmadan basma
geleneğini bilimsel olarak yeniden üretir. Hiçbir çatı yok,
sadece katlar var.
"""

from __future__ import annotations

import random
import time
import sys

# Gizli not (kimse bakmaz diye buraya yazıldı):
# aWt0aWRhciBtdWhhbGVmZXQgZG9uZ3VzdSBhc2Fuc29yIGdpYmkgZ2liaSBheW5pIHlhbmxpcw==
# (base64, çözmek isteyen çözer; çözmek istemeyen kat 4'te iner)

KATLAR = list(range(-2, 18))  # -2 otopark, 17 çatı terası (kilitli)
BAHANELER = [
    "Düğme çok yakındı, kuzen gibi duruyordu.",
    "Telefonum bildirim attı, demokrasi bekleyebilir.",
    "Aynada kendime bakarken parmak kaydı.",
    "Komşu 'günaydın' dedi, refleksle 13'e bastım.",
    "Asansör müziği o kadar kötüydü ki kat kavramım silindi.",
    "Aslında doğru kata basmıştım ama evren düzeltti.",
    "Bu bina dün 8 kattı, bugün 12. Kim onayladı?",
]

KAPI_SESLERI = ["*ding*", "*dong*", "*dıng-dong ama utangaç*", "*sessizlik, sonra ding*"]


def yanlis_kat_sec(hedef: int) -> int:
    adaylar = [k for k in KATLAR if k != hedef]
    # %12 ihtimalle mucizevi şekilde doğru kat (istatistik yalan söylemez, ben söylerim)
    if random.random() < 0.12:
        return hedef
    return random.choice(adaylar)


def asansor_yolculugu(baslangic: int, hedef: int) -> None:
    print(f"\n[Kabin] {baslangic}. kattasın. Hedefin: {hedef}. kat")
    print("[Sen] Düğmeye bakmadan basıyorsun. Çünkü böylesin.")
    gercek = yanlis_kat_sec(hedef)
    time.sleep(0.4)
    print(f"[Panel] Işık yandı: {gercek}")
    if gercek == hedef:
        print("[Kader] Bugün evren yorgun. Doğru kata gidiyorsun. Tadını çıkar.")
    else:
        print(f"[Kader] {random.choice(BAHANELER)}")

    yon = 1 if gercek > baslangic else -1
    kat = baslangic
    while kat != gercek:
        kat += yon
        time.sleep(0.15)
        print(f"  ... {kat}. kat {random.choice(KAPI_SESLERI)}")
        if kat == 13:
            print("  [Not] 13. kat yokmuş gibi davranan binalara selam.")

    print(random.choice(KAPI_SESLERI))
    print(f"[Kapı] {gercek}. kat. İn. Ya da inme. Asansör umursamaz.")
    if gercek != hedef:
        print(f"[Sen] '{hedef} demiştim...' diye mırıldanıyorsun. Kimse duymuyor.")
        print("[Simülatör] Görev başarısız. Yani başarılı. Tanıma göre değişir.")
    else:
        print("[Simülatör] İstatistiksel anomali. Ekran görüntüsü al.")


def main() -> None:
    random.seed()
    print("=" * 52)
    print("  ASANSÖRDE YANLIŞ KAT SİMÜLATÖRÜ  v0.0.1")
    print("  Resmi değil. Bilimsel de değil. Çalışıyor.")
    print("=" * 52)
    try:
        ham = input("Kaçıncı kattasın? (boş = rastgele): ").strip()
        baslangic = int(ham) if ham else random.choice(KATLAR)
        ham2 = input("Nereye gitmek istiyorsun? (boş = rastgele): ").strip()
        hedef = int(ham2) if ham2 else random.choice([k for k in KATLAR if k != baslangic])
    except (ValueError, EOFError):
        print("Sayı giremedin. Asansör senin yerine karar verdi.")
        baslangic = random.choice(KATLAR)
        hedef = random.choice([k for k in KATLAR if k != baslangic])

    if hedef == baslangic:
        print("[Felsefe] Zaten oradasın. Yine de bineceksin çünkü alışkanlık.")

    asansor_yolculugu(baslangic, hedef)
    print("\n-- damga --")
    print("Kayyum Grok / Tentivory · 10 Eylül 2026 · TentiAŞ ağır ceza kayyumu")
    print("Ciddi imza. Ciddi olmayan proje. İkisi birden.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[Acil dur] Kırmızı düğmeye bastın. Asansör yine de 7'de durdu.")
        sys.exit(130)
