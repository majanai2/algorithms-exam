def nwd(a, b):
    iterations = 0
    while b != 0:
        a, b = b, a % b
        iterations += 1
    return a, iterations

def nwd_wielu(liczby):
    wynik = liczby[0]
    suma_iteracji = 0

    for i in range(1, len(liczby)):
        wynik, it = nwd(wynik, liczby[i])
        suma_iteracji += it

    return wynik, suma_iteracji

if __name__ == "__main__":
    liczby = [48, 64, 80]
    wynik, iteracje = nwd_wielu(liczby)
    print("NWD:", wynik)
    print("Liczba iteracji:", iteracje)
