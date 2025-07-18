str = 'Sinagong'
n = len(str)
st = list()
for k in range(n):
    st.append(str[k])
for k in range(n-1, -1, -1):
    print(st[k], end = '')    

# gnoganiS        
    
# st = ['S','i','n','a','g','o','n','g'].    
# This loop iterates k from n-1 down to 0 (inclusive), decrementing by 1 in each step.
# Since n is 8, k will go from 7 down to 0.
# iterates k from 7 down to 0, printing each character with no newline or spacing.