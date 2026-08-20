"""
Python Percentages Reference
==============================
Covers:
    percentage_of_a_number()
    value_from_percentage()
    percentage_increase_decrease()
    percentage_change()
    decimal_percentage_conversion()
    formatting_as_percentage_string()
    rounding_percentages()
    modulus_vs_percent_pitfall()

Run this file directly to see every example executed:
    python python_percentages_reference.py
"""



def percentage_of_a_number():
    """
    Percentage of a number
    -------------------------
    Formula: (part / whole) * 100

    Example: what percentage is 30 out of 200?
    """
    part = 30
    whole = 200
    percentage = (part / whole) * 100
    print("Percentage of a number")
    print(f"  {part} is {percentage}% of {whole}")


def value_from_percentage():
    """
    Getting a value FROM a percentage
    -------------------------------------
    Formula: (percentage / 100) * whole

    Example: what is 15% of 200? (classic tip-calculator style problem)
    """
    percent = 15
    whole = 200
    value = (percent / 100) * whole
    print("\nValue from a percentage")
    print(f"  {percent}% of {whole} = {value}")


def percentage_increase_decrease():
    """
    Applying a percentage increase or decrease
    -----------------------------------------------
    Increase: new_value = value * (1 + percent / 100)
    Decrease: new_value = value * (1 - percent / 100)

    Example: a $50 item with a 20% discount, and a $50 item with 8% tax added.
    """
    price = 50
    discount_percent = 20
    tax_percent = 8

    discounted_price = price * (1 - discount_percent / 100)
    price_with_tax = price * (1 + tax_percent / 100)

    print("\nPercentage increase / decrease")
    print(f"  ${price} with {discount_percent}% discount -> ${discounted_price}")
    print(f"  ${price} with {tax_percent}% tax added     -> ${price_with_tax}")


def percentage_change():
    """
    Percentage change between two values
    -----------------------------------------
    Formula: ((new_value - old_value) / old_value) * 100

    A positive result means an increase, negative means a decrease.
    Example: a stock price moving from $80 to $92.
    """
    old_value = 80
    new_value = 92
    change = ((new_value - old_value) / old_value) * 100
    print("\nPercentage change")
    print(f"  From {old_value} to {new_value} is a {change}% change")


def decimal_percentage_conversion():
    """
    Converting between decimal and percentage form
    ----------------------------------------------------
    decimal -> percentage : multiply by 100
    percentage -> decimal : divide by 100

    Decimal form (e.g. 0.25) is what you use in calculations;
    percentage form (e.g. 25%) is what you show to a user.
    """
    decimal_value = 0.25
    percentage_value = 25

    print("\nDecimal <-> percentage conversion")
    print(f"  {decimal_value} as a percentage -> {decimal_value * 100}%")
    print(f"  {percentage_value}% as a decimal -> {percentage_value / 100}")


def formatting_as_percentage_string():
    """
    Formatting a number AS a percentage string
    ------------------------------------------------
    Python's f-string '%' format spec takes a DECIMAL (0.0-1.0) and both
    multiplies it by 100 and adds the % sign for you.

    :.0%  -> no decimal places
    :.1%  -> 1 decimal place
    :.2%  -> 2 decimal places

    Common mistake: passing an already-multiplied number (like 25 instead
    of 0.25) gives a wrong result (2500%), since the format spec multiplies
    by 100 itself.
    """
    ratio = 0.4567
    print("\nFormatting as a percentage string")
    print(f"  {ratio:.0%}")
    print(f"  {ratio:.1%}")
    print(f"  {ratio:.2%}")


def rounding_percentages():
    """
    Rounding a percentage value
    --------------------------------
    Use the built-in round(value, digits) once you have a plain number
    (not the f-string %-format, which rounds automatically).
    """
    percentage = 66.66666
    print("\nRounding percentages")
    print(f"  round({percentage}, 0) -> {round(percentage, 0)}")
    print(f"  round({percentage}, 1) -> {round(percentage, 1)}")
    print(f"  round({percentage}, 2) -> {round(percentage, 2)}")


def modulus_vs_percent_pitfall():
    """
    Common pitfall: % is the MODULUS operator, not a percent sign
    -------------------------------------------------------------------
    In Python code, % between two numbers means "remainder of division",
    not "percent". To display an actual percent sign, use the f-string
    ':.0%' format shown above, or build the string manually.
    """
    print("\nModulus vs. percent pitfall")
    print(f"  7 % 2 = {7 % 2}   <- this is remainder, NOT '7 percent of 2'")
    print(f"  To show 45 as '45%': f'{{45}}%' -> {45}%")


if __name__ == "__main__":
    percentage_of_a_number()
    value_from_percentage()
    percentage_increase_decrease()
    percentage_change()
    decimal_percentage_conversion()
    formatting_as_percentage_string()
    rounding_percentages()
    modulus_vs_percent_pitfall()
