# Süreklilik ve asimptotlar

## Süreklilik

f, x = a da sürekli ⇔ **lim(x→a) f(x) = f(a)**.

Üç koşul: f(a) tanımlı, limit var, ikisi eşit.

- Polinomlar tüm ℝ de süreklidir (f(x) = x² + 1, 2x + 1, sabit).
- Rasyonel fonksiyonlar tanım kümelerinin her noktasında süreklidir.
- f(x) = 1/x, x = 0 da tanımsız → süreksiz.

## Süreksizlik türleri

- **Kaldırılabilir süreksizlik:** Limit var ama f(a) tanımsız veya farklı. (x² − 4)/(x − 2): limit 4, f(2) tanımsız.
- **Sıçrama:** Sol ve sağ limit farklı.
- **Sonsuz süreksizlik:** Fonksiyon sınırsız büyür (düşey asimptot).

## Parametre bulma

Parçalı fonksiyonun sürekli olması için kritik noktada sol limit = sağ limit = fonksiyon değeri.

- f(x) = x + 2 (x ≤ 1), ax + 1 (x > 1): 3 = a + 1 → a = 2.
- f(x) = x² + ax (x < 1), 3 (x ≥ 1): 1 + a = 3 → a = 2.
- f(x) = (x² − 1)/(x − 1) (x ≠ 1), f(1) = k için k = 2.

## Asimptotlar

- **Düşey asimptot:** Paydayı sıfır yapan (payı sıfır yapmayan) x = a doğruları. f(x) = 1/(x − 2) için x = 2; 1/(x² − 1) için x = ±1.
- **Yatay asimptot:** lim(x→±∞) f(x) = c ise y = c.
  - f(x) = 1/x → y = 0
  - f(x) = (2x + 1)/(x − 3) → y = 2 ve düşey x = 3
  - (x² − 1)/(x² − 4) → y = 1

## Özet

| İfade | Davranış |
|---|---|
| Polinom | Her yerde sürekli |
| Rasyonel | Payda ≠ 0 yerlerde sürekli |
| Payda = 0 | Düşey asimptot veya kaldırılabilir süreksizlik |
| Derece(pay) ≤ derece(payda) | Yatay asimptot var |
