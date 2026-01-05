# Zagadnienie 5 – Faktoryzacja liczb

## Opis
Program rozkłada podaną liczbę całkowitą
na czynniki pierwsze metodą dzielenia próbnego.

Rozkład na czynniki pierwsze jest jednoznaczny
z dokładnością do kolejności.

## Efektywność
- skuteczna dla małych i średnich liczb
- nieefektywna dla bardzo dużych liczb

## Zastosowania
- kryptografia (RSA)
- bezpieczeństwo danych
- teoria liczb
---

## Przykładowe obliczenia

Dla liczby: **84**

Proces rozkładu:
- 84 = 2 × 42  
- 42 = 2 × 21  
- 21 = 3 × 7  
- 7 = 7

Ostateczny rozkład:  
**84 = 2 × 2 × 3 × 7**

## Wnioski

Algorytm dzielenia próbnego jest prosty i skuteczny dla niewielkich liczb,
jednak dla bardzo dużych liczb jego wydajność gwałtownie spada.
