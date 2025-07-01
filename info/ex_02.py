a , c = 32, -3
b = a << 2
a >>= 3
c = c << 2
print(a, b ,c)

# 4 128 -12

# Compute b = a << 2

# Left-shift by 2 multiplies by 2²:
# 32 × 4=128

# So b = 128 (binary 0b10000000)

# Update a >>= 3

# Right-shift by 3 divides (floor) by 2³:
# 32 ÷ 8=4

# So a = 4 (binary 0b100)

# Compute c = c << 2

# Even for negatives, left-shift multiplies by 2²:
# −3×4=−12
# So c = -12
