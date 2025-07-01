a = [ [1, 1, 0, 1, 0] ,
        [1,0,1,0]   ]
tot, totsu = 0,0
for i in a:
    for j in i:
        tot += j
    totsu = totsu + len(i)
print(totsu , tot)

# 9 5

# a = [ [1, 1, 0, 1, 0],   # 5 elements, sum = 1+1+0+1+0 = 3
#      [1, 0, 1, 0] ]     # 4 elements, sum = 1+0+1+0 = 2

# tot, totsu = 0, 0

# for sub in a:
#    for val in sub:
#        tot += val         # accumulate sum of values
#    totsu += len(sub)      # add number of elements in this sub-list

# After both loops:
# totsu = 5 + 4 = 9
# tot   = 3 + 2 = 5

# print(totsu, tot)  # outputs: 9 5
