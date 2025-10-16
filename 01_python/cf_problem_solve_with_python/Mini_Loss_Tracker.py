n = int(input())
target = float(input())
s=0.0
for i in range(n):
    s+=float(input())
if(s/n<=target):
    print("PASS")
else:
    print("RETRY")