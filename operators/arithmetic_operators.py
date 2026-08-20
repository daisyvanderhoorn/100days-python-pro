def arithmetic_operators():
    """
    PEMDAS <-> Left to Right

    1. Parentheses;         ()
    2. Exponents;           **
    3. Modulus (remainder)  %
    3. Multiplication;      *
    3. Divison;             /
    4. Addition;            +
    4. Subtraction;         -
    """
    a, b = 5, 2
    print("Arithmetic Operators")
    print(f"  {a} + {b}  = {a + b}")
    print(f"  {a} - {b}  = {a - b}")
    print(f"  {a} * {b}  = {a * b}")
    print(f"  {a} / {b}  = {type(a / b)}")
    print(f"  {a} // {b} = {type(a // b)}")
    print(f"  {a} % {b}  = {a % b}")
    print(f"  {a} ** {b} = {a ** b}")


if __name__ == "__main__":
    arithmetic_operators()
