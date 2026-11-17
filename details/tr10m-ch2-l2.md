# Olasılık ve koşullu olasılık

## Temel kavramlar

- **Deney:** Sonucu önceden bilinmeyen işlem (zar atma).
- **Örnek uzay (E):** Tüm olası sonuçlar kümesi.
- **Olay:** Örnek uzayın alt kümesi.
- **Olasılık:** P(A) = s(A)/s(E), 0 ≤ P(A) ≤ 1

Kesin olayın olasılığı 1, imkânsız olayın olasılığı 0 dır.

**Örnekler**
- İki madeni parada örnek uzay 4 elemanlıdır; üç madeni parada 8.
- Bir zar atıldığında 6 gelme olasılığı 1/6.
- İki zar toplamının 7 olma olasılığı 6/36 = 1/6.

## Olaylar arası işlemler

- **Tümleyen:** P(A′) = 1 − P(A)
- **Ayrık olaylar:** P(A ∪ B) = P(A) + P(B)
- **Genel birleşim:** P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

## Bağımsız olaylar

Birinin sonucu diğerini etkilemiyorsa olaylar bağımsızdır: **P(A ∩ B) = P(A)·P(B)**.
Torbadan **iadeli** çekilişler bağımsızdır: (3/5)·(3/5) = 9/25.
**İadesiz** çekilişlerde ikinci olasılık değişir: (4/10)·(3/9) = 2/15.

## Koşullu olasılık

B olayının gerçekleştiği biliniyorsa A olayının olasılığı:

**P(A ∣ B) = P(A ∩ B) / P(B)**

**Örnek:** Zar atılıyor, sayının çift olduğu biliniyor. 4'ten büyük olma olasılığı: çift sayılar {2, 4, 6}, istenen {6} → 1/3.

## Deneysel olasılık

Deneysel olasılık = olayın gerçekleşme sayısı / toplam deneme sayısı. Madeni para 100 kez atılıp 48 yazı geldiyse deneysel olasılık 0,48 dir. Deneme sayısı arttıkça deneysel olasılık kuramsal olasılığa yaklaşır.
