"""Q3: Vehicle registration normalisation, validation, and receipt formatting."""

def normalise(text: str) -> str:
    return text.strip().replace(" ", "").replace("-", "").upper()


def is_valid(reg: str) -> bool:
    if len(reg) not in (9, 10):
        return False
    series_end = len(reg) - 4
    return (reg[0:2].isalpha() and reg[0:2].isupper()
            and reg[2:4].isdigit()
            and reg[4:series_end].isalpha() and reg[4:series_end].isupper()
            and reg[series_end:].isdigit())


def format_receipt(reg: str) -> str:
    if not is_valid(reg):
        raise ValueError("cannot format an invalid registration")
    series_end = len(reg) - 4
    return f"{reg[:2]} {reg[2:4]} {reg[4:series_end]} {reg[series_end:]}"


if __name__ == "__main__":
    samples = ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234", "TN 22 1234 AB",
               "mh 12 xy 9876", "DL-3-C-4567"]
    print(f"{'input':18} {'normalised':12} result")
    for raw in samples:
        reg = normalise(raw)
        status = "valid" if is_valid(reg) else "INVALID"
        print(f"{raw:18} {reg:12} {status}")
        if is_valid(reg):
            print(" " * 4 + "receipt:", format_receipt(reg))
    print("\nFor lengths 9 and 10, s[-4:] is the final four digits; s[4:-4] is the 1- or 2-letter series.")
    print("Strings are immutable: upper() returns a new string and leaves the original unchanged.")
    print("Complexity: normalise, validation, and formatting each take O(L) time; O(L) output space.")
