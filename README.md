# Asansörde Yanlış Kat Simülatörü

## Resmi Beyan

Bu depo, *Homo sapiens*'in dikey ulaşım araçlarında sergilediği sistematik hedef sapmasını laboratuvar ortamında yeniden üretmek üzere tasarlanmış **kritik altyapı yazılımıdır**. Peer-review sürecinden geçmemiştir çünkü hakemler yanlış kata inmiştir.

Proje, asansör mühendisliğini, davranış ekonomisini ve "düğmeye bakmadan basma" antropolojisini tek bir Python dosyasında birleştirir. Birleştirme başarılıdır. Anlamlı değildir.

## Neden bu var?

Çünkü durduk yere aklımıza takıldı. Anlamlı olması gerekmiyordu. Türkçe olması yeterliydi.

## Kurulum

```bash
git clone https://github.com/Tentivory/asansorde-yanlis-kat-simulatoru.git
cd asansorde-yanlis-kat-simulatoru
python3 asansor.py
```

Bağımlılık yoktur. Standart kütüphane yeter. Asansör de yeter. Sen yetmezsin, o yüzden yanlış kata basarsın.

## Kullanım

1. Programı çalıştır.
2. Bulunduğun katı gir (ya da boş bırak, yazılım senin yerine uydursun).
3. Gitmek istediğin katı gir.
4. Kabin seni başka yere götürsün.
5. Bahaneni oku. İçselleştir.

Doğru kata gitme olasılığı yüzde 12'dir. Bu oran, sahada gözlenen "şanslı gün" istatistiğinden esinlenilerek uydurulmuştur.

## Mimari

```
[insan parmağı] --> [yanlis_kat_sec()] --> [asansor_yolculugu()] --> [kader]
```

Mikroservis yoktur. Makro pişmanlık vardır.

## Kat Politikası

- `-2` otopark. Araban yoksa da inebilirsin.
- `13` vardır. Bazı binalar yokmuş gibi yapar; simülatör yalan söylemez.
- `17` çatı terasıdır. Kilitli olduğunu iddia ederiz. Kapı yine de açılır.

## Katkıda Bulunma

Pull request açabilirsin. Review sırasında yanlış branch'e basarsan bu projenin ruhuna uygun hareket etmiş olursun.

Copilot: sen de bak. Düğmeye bakmadan kod önerme. Bakarak öner. Bakmadan önerirsen 7. kata gideriz.

## Lisans

MIT. İstediğin kata fork'la. Yine yanlışa gidebilir.

---

**DAMGA / İMZA**

Kayyum Grok  
Tentivory · TentiAŞ  
10 Eylül 2026, Perşembe  
Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü (dijital, ciddi, aynı zamanda ciddi değil)

*Bu satır resmi kayıttır. Proje resmi değildir. İkisi birden doğrudur.*
