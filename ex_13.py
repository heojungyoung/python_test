class CharClass:
    a = ['Seoul', 'Kyeongi', 'Inchon', 'Daejeon', 'Daegu', 'Pusan'];

myVar = CharClass()
str01 = ' '
for i in myVar.a:
    str01 = str01 + i[0]
print(str01)    


# | 도시 이름     | i\[0] | str01 변화    |
# | --------- | ----- | ----------- |
# | "Seoul"   | S     | `" S"`      |
# | "Kyeongi" | K     | `" SK"`     |
# | "Inchon"  | I     | `" SKI"`    |
# | "Daejeon" | D     | `" SKID"`   |
# | "Daegu"   | D     | `" SKIDD"`  |
# | "Pusan"   | P     | `" SKIDDP"` |

# SKIDDP