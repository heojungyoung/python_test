a = {  'apple', 'lemon', 'banana' }
a.update(  {'kiwi', 'banana'})
a.remove('lemon')
a.add('apple')
for i in a:
    print("과일명 : %s" % i)

# a = {'apple', 'lemon', 'banana'}

# a.update({'kiwi', 'banana'})   # 'banana'는 이미 있으므로 변화 없음
# a  ➜  {'apple', 'lemon', 'banana', 'kiwi'}

# a.remove('lemon')              # 'lemon' 삭제
# a  ➜  {'apple', 'banana', 'kiwi'}

# a.add('apple')                 # 이미 존재하므로 변화 없음
# a  ➜  {'apple', 'banana', 'kiwi'}
