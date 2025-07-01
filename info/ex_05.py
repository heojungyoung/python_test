a, b = 1, 1
y = a + b
n = 10

for k in range(3, n +1):
    c = a + b
    y = y + c
    a = b
    b = c

print(y)

# 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34 + 55 = 143

