"""Q4: Compare string-building strategies using repeatable local timings."""
import statistics
import time


def build_plus(items):
    result = ""
    for item in items:
        result += item + ";"
    return result


def build_join(items):
    return ";".join(items) + (";" if items else "")


def build_fstring(items):
    parts = [f"{item};" for item in items]
    return "".join(parts)


def measure(fn, items, repeats=3):
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = fn(items)
        times.append(time.perf_counter() - start)
    return result, times, statistics.mean(times)


if __name__ == "__main__":
    for size in (1_000, 10_000, 200_000):
        items = [f"Item{i}:Rs{i % 50}" for i in range(size)]
        outputs = [measure(f, items) for f in (build_plus, build_join, build_fstring)]
        same = outputs[0][0] == outputs[1][0] == outputs[2][0]
        print(f"n={size:,} same_text={same} length={len(outputs[0][0]):,}")
        for label, (_, times, avg) in zip(("+=", "join", "f-string + join"), outputs):
            print(f"  {label:16} runs={[round(t, 6) for t in times]} mean={avg:.6f}s")
    print("Complexity: join-based versions are O(total output length); repeated += may copy growing prefixes.")
    print("Record these measurements again on your own computer; timing depends on machine and Python build.")
