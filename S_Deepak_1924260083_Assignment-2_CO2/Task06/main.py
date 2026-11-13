"""Q6: Naive recursion, memoisation, and iterative stair counts."""
from functools import lru_cache
import sys
import time

calls = 0

def ways_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_iterative(n):
    if n <= 1:
        return 1
    previous, current = 1, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current


if __name__ == "__main__":
    print("hand-check values:", {n: ways_iterative(n) for n in range(1, 7)})
    print("naive and memo call counts:")
    for n in (10, 20, 25, 30):
        calls = 0
        start = time.perf_counter(); naive_value = ways_naive(n); naive_time = time.perf_counter() - start
        naive_calls = calls
        calls = 0; ways_memo.cache_clear()
        start = time.perf_counter(); memo_value = ways_memo(n); memo_time = time.perf_counter() - start
        memo_calls = calls
        print(f"n={n:2} value={naive_value} agree={naive_value == memo_value} "
              f"naive_calls={naive_calls} naive_s={naive_time:.6f} "
              f"memo_calls={memo_calls} memo_s={memo_time:.6f}")
    ways_memo.cache_clear()
    try:
        print("memo n=1000:", ways_memo(1000))
    except RecursionError as exc:
        print(f"memo n=1000 raised {type(exc).__name__}; recursion limit={sys.getrecursionlimit()}")
    start = time.perf_counter(); value = ways_iterative(1000); elapsed = time.perf_counter() - start
    print(f"iterative n=1000 digits={len(str(value))} time={elapsed:.6f}s")
    print("Complexity: naive O(phi^n) time; memo O(n) time and O(n) cache/stack; iterative O(n) time, O(1) extra space.")
