a,b,c = [int(x) for x in input().split()]

min = a
max = a

# min
if b<min:
    min = b
if c<min:
    min = c

# max
if b>max:
    max = b
if c>max:
    max = c
    
    
print(min, max)