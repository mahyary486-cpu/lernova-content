# Mehrstufige Zufallsexperimente und Pfadregeln

## Baumdiagramm

Mehrstufige Zufallsexperimente (mehrmals würfeln, mehrmals Kugeln ziehen) stellt man in einem **Baumdiagramm** dar. Jeder Pfad entspricht einem Ergebnis. An die Äste schreibt man die Wahrscheinlichkeiten.

## Pfadregeln

- **Produktregel:** Die Wahrscheinlichkeit eines Pfades ist das Produkt der Wahrscheinlichkeiten entlang der Äste.
- **Summenregel:** Gehören mehrere Pfade zu einem Ereignis, addiert man ihre Wahrscheinlichkeiten.

## Mit und ohne Zurücklegen

- **Mit Zurücklegen:** In jeder Stufe bleiben die Wahrscheinlichkeiten gleich.
- **Ohne Zurücklegen:** Die Anzahl der Kugeln sinkt, die Wahrscheinlichkeiten ändern sich von Stufe zu Stufe.

## „Mindestens einmal“

Hier rechnet man am besten mit dem Gegenereignis:

**P(mindestens einmal) = 1 − P(nie)**

## Beispiele

**Beispiel 1:** Münze zweimal werfen.
P(zweimal Zahl) = 1/2 · 1/2 = 1/4.

**Beispiel 2:** Urne mit 4 roten und 6 blauen Kugeln, zweimal ohne Zurücklegen.
P(rot, rot) = 4/10 · 3/9 = 12/90 = 2/15.

**Beispiel 3:** Würfel zweimal werfen.
P(mindestens eine 6) = 1 − (5/6)² = 1 − 25/36 = 11/36.

**Beispiel 4:** Münze dreimal werfen, genau einmal Zahl.
Drei Pfade mit je 1/8, also P = 3/8.
