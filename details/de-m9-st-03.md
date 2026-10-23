# Zählprinzip, Fakultät und Binomialkoeffizient

## Zählprinzip

Gibt es bei der ersten Entscheidung n₁ und bei der zweiten n₂ Möglichkeiten, so gibt es insgesamt **n₁ · n₂** Möglichkeiten. Das gilt auch für mehr als zwei Stufen.

**Beispiel:** Ein Zahlenschloss mit 3 Rädern (je 0 bis 9) hat 10 · 10 · 10 = 1000 Einstellungen.

## Fakultät

**n! = n · (n − 1) · … · 2 · 1**, außerdem gilt 0! = 1.

n! gibt an, auf wie viele Arten man n verschiedene Objekte anordnen kann.

**Beispiele:** 4! = 24 und 5! = 120.

## Geordnete Auswahl

Wählt man aus n Objekten k Objekte in einer bestimmten Reihenfolge aus (ohne Zurücklegen), gibt es n · (n − 1) · … · (n − k + 1) Möglichkeiten.

**Beispiel:** Podium mit 3 Plätzen bei 8 Läufern: 8 · 7 · 6 = 336.

## Ungeordnete Auswahl: Binomialkoeffizient

Die Anzahl der Möglichkeiten, aus n Objekten k ohne Beachtung der Reihenfolge auszuwählen, ist

**(n über k) = n! : (k! · (n − k)!)**

- (n über 0) = 1 und (n über 1) = n
- (n über k) = (n über n − k)

**Beispiele:** (5 über 2) = 10, (6 über 2) = 15, (25 über 5) = 53 130.

## Anordnungen mit gleichen Objekten

Bei n Objekten, von denen einige gleich sind, teilt man durch die Fakultäten der Gleichen.

**Beispiel:** Buchstaben von ANNA: 4! : (2! · 2!) = 6.
