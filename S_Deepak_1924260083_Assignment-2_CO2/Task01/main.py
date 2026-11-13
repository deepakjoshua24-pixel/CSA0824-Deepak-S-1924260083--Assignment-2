"""Q1: State electricity subsidy rules and boundary analysis."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Household:
    name: str
    units: int
    ration_card: bool
    age_over_80: bool


def separate_if_buggy(h):
    """Deliberately faulty: overlapping independent conditions can award two results."""
    decisions = []
    if h.units <= 100:
        decisions.append("full subsidy")
    # BUG: partial rule starts at zero instead of 101, so it overlaps the first rule.
    if h.units <= 200 and h.ration_card:
        decisions.append("partial subsidy")
    if h.units > 200 and not h.age_over_80:
        decisions.append("no subsidy")
    if h.units > 200 and h.age_over_80:
        decisions.append("senior exception")
    return decisions or ["no subsidy"]


def decide(h):
    """Correct mutually exclusive decision using if-elif-else."""
    if h.units <= 100:
        return "full subsidy"
    elif 101 <= h.units <= 200:
        return "partial subsidy" if h.ration_card else "no subsidy"
    else:  # units > 200
        return "senior exception" if h.age_over_80 else "no subsidy"


def decide_match(h):
    """Alternative match-case implementation (Python 3.10+)."""
    match h:
        case Household(units=u) if u <= 100:
            return "full subsidy"
        case Household(units=u, ration_card=True) if 101 <= u <= 200:
            return "partial subsidy"
        case Household(units=u) if 101 <= u <= 200:
            return "no subsidy"
        case Household(units=u, age_over_80=True) if u > 200:
            return "senior exception"
        case _:
            return "no subsidy"


households = [
    Household("H1", 100, False, False), Household("H2", 100, True, False),
    Household("H3", 101, True, False), Household("H4", 101, False, False),
    Household("H5", 200, True, False), Household("H6", 200, False, False),
    Household("H7", 201, False, False), Household("H8", 201, False, True),
]
print("name units ration_card age_over_80 | buggy separate-if | correct if-elif | match-case")
for h in households:
    print(f"{h.name:>4} {h.units:>5} {str(h.ration_card):>11} {str(h.age_over_80):>11} | "
          f"{', '.join(separate_if_buggy(h)):>24} | {decide(h):>16} | {decide_match(h)}")
print("\nComplexity: each fixed if/elif or match decision is O(1) time and O(1) extra space.")
print("A lookup searched linearly through k slabs is O(k) time and O(k) table space.")
