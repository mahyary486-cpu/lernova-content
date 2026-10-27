# Kenngrößen und Rechnen mit der Binomialverteilung

## Kenngrößen

Für X ~ B(n; p) gilt:

- **E(X) = n · p**
- **V(X) = n · p · (1 − p)**
- **σ = √(n · p · (1 − p))**

## Beispiele

- n = 10, p = 0,5: E = 5
- n = 100, p = 0,3: V = 21, σ ≈ 4,58
- n = 50, p = 0,6: μ = 30, σ ≈ 3,46
- 10-mal würfeln, Anzahl der Sechsen: E ≈ 1,67

Vervierfacht man n, **verdoppelt** sich σ.

## Kumulierte Wahrscheinlichkeiten

- P(X ≤ k): höchstens k Treffer, man addiert P(X = 0) bis P(X = k)
- P(X > k) = 1 − P(X ≤ k)
- P(X ≥ 1) = 1 − P(X = 0) = 1 − (1 − p)ⁿ

## Mindestens-Aufgaben

Wie oft muss man würfeln, damit mit mindestens 90 % Wahrscheinlichkeit mindestens eine 6 fällt?
1 − (5/6)ⁿ ≥ 0,9 gilt ab n = 13.

Bei p = 0,1 und mindestens 99 % Wahrscheinlichkeit für mindestens einen Treffer: n = 44.

**KMK-Leitidee:** Daten und Zufall
