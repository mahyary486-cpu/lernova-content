# Sayma stratejileri: permütasyon ve kombinasyon

## Temel sayma kuralları

- **Toplama kuralı (veya):** A işi m, B işi n yolla yapılıyorsa ve işler birlikte yapılamıyorsa A veya B işi m + n yolla yapılır.
- **Çarpma kuralı (ve):** A işi m, ardından B işi n yolla yapılıyorsa iş m·n yolla yapılır.

**Örnek:** 3 gömlek ve 4 pantolonla 3·4 = 12 kombin yapılır.

## Faktöriyel

n! = n·(n − 1)·…·2·1 ve 0! = 1. Örneğin 5! = 120.

## Permütasyon (sıralama)

n elemanın r tanesinin sıralanması: **P(n, r) = n!/(n − r)!** 

- P(5, 2) = 5·4 = 20
- n elemanın tamamının sıralanması n! dir.
- **Tekrarlı permütasyon:** n elemanın içinde a tanesi aynı ise n!/a! dir. ANKARA için 6!/3! = 120.
- **Yan yana koşulu:** Yan yana olanlar bir blok sayılır, blok içi de sıralanır. A ile B yan yana olacak şekilde 5 harf: 4!·2! = 48.

## Kombinasyon (seçme)

Sıranın önemli olmadığı seçim: **C(n, r) = n!/(r!(n − r)!)**

- C(5, 2) = 10 ve C(6, 3) = 20
- C(n, r) = C(n, n − r)
- 7 kişiden 3 kişilik komitede belirli iki kişi bulunacaksa C(5, 1) = 5.

## Rakamlarla sayı yazma

Sıfırın başa gelemediğini unutmayın. 0, 1, 2, 3, 4 rakamlarıyla (tekrarsız) üç basamaklı sayı: 4·4·3 = 48.

## Hangisini seçmeliyim?

| Soru ipucu | Yöntem |
|---|---|
| Sıra önemli (sıralama, şifre, yarış derecesi) | Permütasyon |
| Sıra önemsiz (komite, takım, el) | Kombinasyon |
| Her aşamada ayrı seçim | Çarpma kuralı |
