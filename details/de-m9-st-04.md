# Bedingte Wahrscheinlichkeit und Vierfeldertafel

## Bedingte Wahrscheinlichkeit

Die Wahrscheinlichkeit von A unter der Bedingung, dass B schon eingetreten ist, schreibt man P(A|B):

**P(A|B) = P(A ∩ B) : P(B)** (mit P(B) > 0)

## Vierfeldertafel

Eine Vierfeldertafel ordnet die Häufigkeiten zweier Merkmale.

**Beispiel:** In einer Klasse mit 30 Schülern sind 18 Mädchen und 12 Jungen. 10 Mädchen und 4 Jungen tragen eine Brille.

- Mädchen mit Brille: 10, Mädchen ohne Brille: 8 (zusammen 18)
- Jungen mit Brille: 4, Jungen ohne Brille: 8 (zusammen 12)
- Insgesamt mit Brille: 14, ohne Brille: 16 (zusammen 30)

P(Brille) = 14/30 = 7/15.
P(Brille | Mädchen) = 10/18 = 5/9.

## Unabhängigkeit und Additionssatz

- Zwei Ereignisse sind **unabhängig**, wenn **P(A ∩ B) = P(A) · P(B)** gilt.
- **Additionssatz:** P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

**Beispiel:** Bei P(A) = 0,5 und P(B) = 0,4 (unabhängig) ist P(A ∩ B) = 0,2 und P(A ∪ B) = 0,7.

## Anwendung: Medizinischer Test

Von 10 000 Personen sind 1 % krank (100 Personen). Der Test erkennt Kranke zu 99 %, zeigt aber bei 5 % der Gesunden fälschlich positiv an.

- Kranke mit positivem Test: 99
- Gesunde mit positivem Test: 5 % von 9900 = 495
- Alle positiven Tests: 594

P(krank | positiv) = 99/594 ≈ 17 %.

Ein positiver Test ist also bei seltenen Krankheiten oft ein Fehlalarm.
