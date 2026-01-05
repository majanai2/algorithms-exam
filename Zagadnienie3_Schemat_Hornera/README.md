# Zagadnienie 3 – Schemat Hornera

## Opis
Implementacja schematu Hornera do efektywnego
obliczania wartości wielomianu w zadanym punkcie.

Metoda pozwala ograniczyć liczbę operacji arytmetycznych
w porównaniu do klasycznego obliczania wielomianu.

## Zalety
- wysoka wydajność
- prostota implementacji
- stabilność numeryczna

## Złożoność
- czasowa: O(n)
- pamięciowa: O(1)
---

## Przykładowe obliczenia

Dla wielomianu:  
**2x³ − 3x² + 4x − 5**

Dla x = 3:

Horner:
- 2 → 2·3 − 3 = 3
- 3 → 3·3 + 4 = 13
- 13 → 13·3 − 5 = 34

Wynik: **34**

## Porównanie

Metoda klasyczna: 6 mnożeń  
Schemat Hornera: 3 mnożenia

## Wnioski

Schemat Hornera znacznie redukuje liczbę operacji,
co poprawia wydajność i dokładność obliczeń.
