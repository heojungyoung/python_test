def func(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[-i-1] = lst[-i-1] , lst[i]
lst = [1,2,3,4,5,6]
func(lst)
print(sum(lst[::2]) - sum(lst[1::2]))

# 3

# Original list: [1, 2, 3, 4, 5, 6]

# i = 0: swap 1 ↔ 6  → [6, 2, 3, 4, 5, 1]
# i = 1: swap 2 ↔ 5  → [6, 5, 3, 4, 2, 1]
# i = 2: swap 3 ↔ 4  → [6, 5, 4, 3, 2, 1]
 
# even-index elements (0,2,4): 6 + 4 + 2 = 12
# odd-index  elements (1,3,5): 5 + 3 + 1 =  9
# result = 12 - 9 = 3
