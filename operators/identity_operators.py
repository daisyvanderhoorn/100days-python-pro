def identity_operators():
    """
    Identity Operators
    --------------------
    is      True if both variables reference the SAME object
    is not  True if they do NOT reference the same object
    Note: 'is' checks identity (same object in memory),
    while '==' checks equality (same value). Not the same thing!
    """
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = list_a
    print("\nIdentity Operators")
    print(f"  list_a == list_b -> {list_a == list_b}  (same values)")
    print(f"  list_a is list_b -> {list_a is list_b}  (different objects)")
    print(f"  list_a is list_c -> {list_a is list_c}  (same object)")


if __name__ == "__main__":
    identity_operators()
