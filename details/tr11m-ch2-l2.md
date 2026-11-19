# Üstel ve logaritmik fonksiyonlar, bileşke

## Üstel fonksiyon

f(x) = aˣ, a > 0 ve a ≠ 1.

- (0, 1) noktasından geçer; x ekseni yatay asimptottur.
- a > 1: artan; 0 < a < 1: azalan.
- Görüntü kümesi (0, ∞). f(x) = 2ˣ + 3 için (3, ∞).
- 2ˣ⁺¹ = 32 → 2ˣ⁺¹ = 2⁵ → x = 4.

## Logaritma

**log_a b = c ⇔ aᶜ = b** (a > 0, a ≠ 1, b > 0)

- log₂ 8 = 3, log 1000 = 3 (taban 10)
- log_a 1 = 0, log_a a = 1

### Kurallar
- log(m·n) = log m + log n
- log(m/n) = log m − log n
- log mᵏ = k·log m
- log_a b = log_c b / log_c a (taban değiştirme)

**Örnekler**
- log₂ 5 + log₂(8/5) = log₂ 8 = 3
- log₃ 27 − log₃ 3 = log₃ 9 = 2
- log₂ 3 = a ise log₂ 12 = a + 2.

## Denklemler

- log₂ x = 5 → x = 32
- log₂(x + 1) = 3 → x + 1 = 8 → x = 7 (tanım koşulunu kontrol edin).

## Fonksiyonlarla dört işlem

(f ± g)(x) = f(x) ± g(x), (f·g)(x) = f(x)·g(x), (f/g)(x) = f(x)/g(x) (g(x) ≠ 0).

f(x) = 2x + 1, g(x) = x² için (f + g)(2) = 5 + 4 = 9.

## Bileşke

**(g ∘ f)(x) = g(f(x))**. Genelde f ∘ g ≠ g ∘ f.

- f(x) = 2x + 1, g(x) = x² için (g ∘ f)(2) = g(5) = 25.
- f(x) = x + 3, g(x) = 2x − 1 için (g ∘ f)(x) = 2(x + 3) − 1 = 2x + 5.

## İpuçları

- Logaritmada tanım koşulları (b > 0) kontrol edilmelidir.
- Üstel denklemlerde tabanlar eşitlenir.
- Bileşkede önce içteki fonksiyon uygulanır.
