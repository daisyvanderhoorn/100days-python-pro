def membership_operators():
    """
    Membership Operators
    -----------------------
    in      True if a value exists in a sequence
    not in  True if a value does NOT exist in a sequence
    """
    fruits = ["apple", "banana", "cherry"]
    print("\nMembership Operators")
    print(f"  'banana' in {fruits} -> {'banana' in fruits}")
    print(f"  'mango' not in {fruits} -> {'mango' not in fruits}")


if __name__ == "__main__":
    membership_operators()
