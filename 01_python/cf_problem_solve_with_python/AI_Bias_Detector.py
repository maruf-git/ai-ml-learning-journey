output = input().split()
n = len(output)
a_count=0
b_count=0
for res in output:
    if(res=='A'):
        a_count+=1
    else:
        b_count+=1

a_percent = a_count*100/n
# print(a_percent,b_count)
if(a_percent>70 or a_percent<30):
    print("Biased Model")
else:
    print("Fair Model")