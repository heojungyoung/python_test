a = "REMEMBER NOVEMBER"
b = a[0:3] + a[12:16]
c = "R AND %s" % "STR"
print(b+c)

# REMEMBER AND STR


# a = "REMEMBER NOVEMBER"

# a[0:3]  -> "REM"
# a[12:16] -> "EMBE"   # 12~15번째 글자. 16은 포함되지 않아요.
# b = a[0:3] + a[12:16]  # "REMEMBE"

# c = "R AND %s" % "STR" # "R AND STR"

