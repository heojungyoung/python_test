a = 100
result = 0
for i in range(1,3):
    result = a >> i
    result = result + 1
print(result)    


# i	a >> i (비트 우측 이동)	+ 1	result 값
# 1	100 >> 1 → 50	51	51
# 2	100 >> 2 → 25	26	26 (앞에 갚은 덮어 씌어짐)