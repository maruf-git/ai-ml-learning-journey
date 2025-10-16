n = int(input())
count=0
for _ in range(n):
    vote = input()
    if vote=="YES":
        count+=1
if count >= n-count:
    print("ACCEPT")
else:
    print("REJECT")