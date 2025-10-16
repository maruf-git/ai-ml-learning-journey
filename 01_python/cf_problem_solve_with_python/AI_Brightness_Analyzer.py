brightness = [int(x) for x in input().split()]
sum=0
for val in brightness:
    sum+=val
level = sum/len(brightness)

if level<85:
    print("Dark Image")
elif level>=85 and level<=170:
    print("Normal Image")
else:
    print("Bright Image")