def faktoryzacja(n):
    czynniki = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            czynniki.append(d)
            n //= d
        d += 1

    if n > 1:
        czynniki.append(n)

    return czynniki

if __name__ == "__main__":
    liczba = 84
    print("Czynniki:", faktoryzacja(liczba))
