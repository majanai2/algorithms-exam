import time

def sieve_eratosthenes(n):
    if n < 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i]]


# TESTY
N = 1_000_000

start = time.time()
primes = sieve_eratosthenes(N)
end = time.time()

print(f"Liczba liczb pierwszych do {N}: {len(primes)}")
print(f"Czas wykonania: {end - start:.4f} s")
print("Pierwsze 10 liczb pierwszych:", primes[:10])
print("Ostatnie 10 liczb pierwszych:", primes[-10:])
