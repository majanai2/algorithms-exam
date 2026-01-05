# Zagadnienie 4 – Algorytm Euklidesa (NWD)

## Opis
Program oblicza największy wspólny dzielnik wielu dodatnich liczb
całkowitych z wykorzystaniem iteracyjnego algorytmu Euklidesa.

## Zasada działania
NWD(a, b) = NWD(b, a mod b)

## Złożoność
- czasowa: O(log n)
- pamięciowa: O(1)

## Zastosowania
- kryptografia
- upraszczanie ułamków
- algorytmy matematyczne
---

## Przykładowe obliczenia

Dla danych wejściowych:  
48, 64, 80

Kolejne obliczenia:
- NWD(48, 64) = 16 (4 iteracje)
- NWD(16, 80) = 16 (3 iteracje)

Wynik końcowy:  
**NWD = 16**

Łączna liczba iteracji algorytmu:  
**7 iteracji**

## Wnioski

Algorytm Euklidesa działa bardzo szybko nawet dla większych liczb,
ponieważ liczba operacji rośnie logarytmicznie wraz z wielkością danych.
