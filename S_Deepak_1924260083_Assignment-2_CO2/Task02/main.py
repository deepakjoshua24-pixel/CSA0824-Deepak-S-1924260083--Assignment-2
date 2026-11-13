"""Q2: OTP attempt loops. All prompts are simulated for reproducibility."""
from collections.abc import Iterable

OTP = "482915"


def while_version(entries: Iterable[str], security_answer_ok=False, debug=False):
    it = iter(entries)
    wrong = 0
    limit = 5 if security_answer_ok else 3
    while wrong < limit:
        try:
            entered = next(it)
        except StopIteration:
            break
        if not entered.strip():
            print("blank entry: ignored; attempt count unchanged")
            continue
        if debug:
            pass  # Deliberate no-op: pass is appropriate when a branch is intentionally empty.
        if entered == OTP:
            print(f"correct OTP after {wrong} wrong attempt(s)")
            break
        wrong += 1
        print(f"wrong OTP: {wrong}/{limit}")
    else:
        print("account locked for 30 minutes")
        return "locked"
    if wrong == limit:
        print("account locked for 30 minutes")
        return "locked"
    return "verified" if entered == OTP else "not verified"


def for_version(entries: Iterable[str], security_answer_ok=False):
    """Count nonblank wrong entries, not blank submissions, with a for loop."""
    it = iter(entries)
    limit = 5 if security_answer_ok else 3
    wrong = 0
    for _slot in range(limit):
        # Keep asking for this slot until it is nonblank or the input stream ends.
        while True:
            try:
                entered = next(it)
            except StopIteration:
                print("input stream ended")
                return "incomplete"
            if entered.strip():
                break
            print("blank entry: ignored; attempt count unchanged")
        if entered == OTP:
            print(f"correct OTP after {wrong} wrong attempt(s)")
            return "verified"
        wrong += 1
        print(f"wrong OTP: {wrong}/{limit}")
    else:
        print("account locked for 30 minutes")
        return "locked"


def recursive_version(entries, limit=3, wrong=0, index=0):
    """Recursive alternative with O(a) time and O(a) stack space."""
    if wrong >= limit:
        return "locked"
    if index >= len(entries):
        return "incomplete"
    entered = entries[index]
    if not entered.strip():
        return recursive_version(entries, limit, wrong, index + 1)
    if entered == OTP:
        return "verified"
    return recursive_version(entries, limit, wrong + 1, index + 1)


if __name__ == "__main__":
    print("while example:")
    print("result:", while_version(["", "111111", "222222", OTP], debug=True))
    print("\nfor example:")
    print("result:", for_version(["", "111111", "222222", "333333"]))
    print("\nsecurity-answer extension:")
    print("result:", while_version(["111111", "222222", "333333", "444444", OTP], True))
    print("recursive example:", recursive_version(["", "111111", OTP]))
    print("Complexity: O(a) time; loops use O(1) auxiliary space; recursion uses O(a) stack.")
