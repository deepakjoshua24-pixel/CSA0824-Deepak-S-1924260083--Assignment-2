"""Q5: Mutable defaults, parameter styles, return values, and scope."""

def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


def price_with_tax(subtotal, rate=0.05):
    tax = subtotal * rate
    return subtotal + tax, tax


def scope_demo():
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1
    local_note = "local to this call"
    count = 10
    def increment_outer():
        nonlocal count
        count += 1
    increment_outer()
    return local_note, count

GLOBAL_COUNTER = 0

if __name__ == "__main__":
    print("buggy:", add_item_buggy("Tea"), add_item_buggy("Vada"))
    print("fixed:", add_item("Tea"), add_item("Vada"))
    print("three independent customers:", [add_item("Customer " + str(i)) for i in range(1, 4)])
    print("buggy stored default:", add_item_buggy.__defaults__)
    total, gst = price_with_tax(100, rate=0.05)
    print(f"total={total:.2f}, GST={gst:.2f}")
    print("scope:", scope_demo(), "global counter:", GLOBAL_COUNTER)
    print("Use positional arguments for clear order, keywords for clarity, defaults for optional values.")
    print("Complexity: appending one item is O(1) amortized time; each customer's list uses O(m) space for m items.")
