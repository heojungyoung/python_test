def cnt(str, p):
    result = 0;
    for i in range(len(str)):
        sub=str[i:i+len(p)]
        if sub ==p:
            result += 1
    return result        
str = "abdcabcabca"
p1 = "ca"
p2 = "ab"
print(f'ab{cnt(str, p1)} ca{cnt(str, p2)}')  


# cnt는 주어진 패턴 p가 문자열 안에 겹쳐서(overlapping) 몇 번 나타나는지 세는 함수입니다.


#| 위치   | 두 글자 | "ca"? | "ab"? |
#| ---- | ---- | ----- | ----- |
#| 0-1  | ab   |       | ✔️    |
#| 1-2  | bd   |       |       |
#| 2-3  | dc   |       |       |
#| 3-4  | ca   | ✔️    |       |
#| 4-5  | ab   |       | ✔️    |
#| 5-6  | bc   |       |       |
#| 6-7  | ca   | ✔️    |       |
#| 7-8  | ab   |       | ✔️    |
#| 8-9  | bc   |       |       |
#| 9-10 | ca   | ✔️    |       |


# ab3 ca3