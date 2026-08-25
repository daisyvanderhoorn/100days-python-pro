height = 1.65
weight = 84

height_squared = height ** 2

# Weight / Height²
bmi = weight / (height ** 2)

print(bmi)

# Flooring
print(int(bmi))

# Rounding up/down
print(round(bmi))

# Round down to X decimals
print(round(bmi, 2))


print(f"{bmi:.2f}")
