def assignment_operators():
    """
    Assignment Operators
    ----------------------
    =    x = 5        plain assignment
    +=   x = x + 5     add and assign
    -=   x = x - 5     subtract and assign
    *=   x = x * 5     multiply and assign
    /=   x = x / 5     divide and assign
    //=  x = x // 5    floor divide and assign
    %=   x = x % 5     modulus and assign
    **=  x = x ** 5    exponent and assign
    &=, |=, ^=, >>=, <<=   bitwise versions (see bitwise_operators)
    """
    x = 10
    print("\nAssignment Operators (starting x = 10)")
    x += 5
    print(f"  x += 5   -> {x}")
    x -= 3
    print(f"  x -= 3   -> {x}")
    x *= 2
    print(f"  x *= 2   -> {x}")
    x /= 4
    print(f"  x /= 4   -> {x}")
    x //= 2
    print(f"  x //= 2  -> {x}")
    x %= 2
    print(f"  x %= 2   -> {x}")
    x **= 3
    print(f"  x **= 3  -> {x}")

if __name__ == "__main__":
    assignment_operators()

# Example += operator
score = 0

# User scored a point
score += 1
print(score)
