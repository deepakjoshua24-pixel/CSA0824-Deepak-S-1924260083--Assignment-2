"""Q7: Redesign Q6 from repeated recursion to a two-value iterative method."""
from functools import lru_cache
import time

naive_calls = 0
@lru_cache(maxsize=None)
def memo(n):
    if n <= 1:
        return 1
    return memo(n - 1) + memo(n - 2)

def naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return naive(n - 1) + naive(n - 2)

def iterative(n):
    if n <= 1:
        return 1
    a = b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def timed(fn, n):
    start = time.perf_counter()
    value = fn(n)
    return value, time.perf_counter() - start

if __name__ == "__main__":
    n = 30
    naive_calls = 0
    original, t_original = timed(naive, n)
    memo.cache_clear()
    cached, t_cached = timed(memo, n)
    redesigned, t_iter = timed(iterative, n)
    assert original == cached == redesigned
    print(f"n={n}; equal_results={original == cached == redesigned}; naive_calls={naive_calls}")
    print(f"naive={t_original:.6f}s memo={t_cached:.6f}s iterative={t_iter:.6f}s")
    n_large = 1000
    large, t_large = timed(iterative, n_large)
    print(f"iterative n={n_large}; digits={len(str(large))}; time={t_large:.6f}s")
    print("Objective: preserve the result while reducing exponential repeated work and avoiding recursive stack growth.")
    print("Trade-off: iterative method keeps only two prior values; it cannot directly provide the full intermediate cache.")
