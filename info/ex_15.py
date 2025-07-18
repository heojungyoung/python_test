x = 'xyz321'
y = 'opq654'

a = ['abc123', 'def456', 'ghi789' ]
a.append(x)
a.append(y)
a.remove('def456')
print(a[1][-3:], a[2][:-3], sep=',')
for i in range(3,6):
    print(i, end = ' ')
 
# 789,xyz
# 3 4 5

# ['abc123', 'ghi789', 'xyz321', 'opq654']
#   0         1         2         3

# a[1][-3:]
# 'ghi789' 의 마지막 3글자 → '789'

# a[2][:-3]
# 'xyz321' 의 뒤 3글자를 뺀 앞부분 → 'xyz'
# a[2][-6:-3]으로 해도 동일한 결과