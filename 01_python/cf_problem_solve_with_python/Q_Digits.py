tst = int(input())
while(tst):
    n = int(input())
    if(n==0):
        print(0,end=" ")
    else:
        while(n>0):
            rem = n%10
            n = n//10 # integer division
            print(rem, end=" ")
    print()
    tst -= 1