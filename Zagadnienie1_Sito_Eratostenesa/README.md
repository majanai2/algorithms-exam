# Zagadnienie 1 – Sito Eratostenesa

Program generuje liczby pierwsze do zadanego zakresu
z wykorzystaniem algorytmu sita Eratostenesa.

**Złożoność:**
- czas: O(n log log n)
- pamięć: O(n)
---

## Przykładowe obliczenia

Zakres: **1 – 30**

Kolejne wykreślenia:
- usuwamy wielokrotności 2: 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30
- usuwamy wielokrotności 3: 9, 15, 21, 27
- usuwamy wielokrotności 5: 25

Pozostałe liczby pierwsze:
**2, 3, 5, 7, 11, 13, 17, 19, 23, 29**

## Test wydajności

Zakres do 1 000 000:
- czas wykonania: < 0.2 s
- pamięć: około 8 MB

## Wnioski

Sito Eratostenesa jest bardzo szybkim algorytmem generowania liczb pierwszych,
szczególnie dla dużych zakresów.
