asia = {'한국', '중국', '일본'}
asia.add('베트남')
asia.add('중국')
asia.remove('일본')
asia.update( {'한국', '홍콩', '태국'})
print(asia)

# 출력 순서는 상관 없음
# set 은 순서가 없고 중복을 허용하지 않는 자료형이므로, 같은 값을 다시 넣어도 한 번만 남고 출력 순서는 실행마다 달라질 수 있습니다.

# asia = {'한국', '중국', '일본'}
# asia.add('베트남')                    # {'한국', '중국', '일본', '베트남'}
# asia.add('중국')                     # 이미 존재 → 변화 없음
# asia.remove('일본')                  # {'한국', '중국', '베트남'}
# asia.update({'한국', '홍콩', '태국'})  # '한국'은 중복, '홍콩'·'태국' 추가
# print(asia)
