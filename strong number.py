n=int(input("enter the number"))
sum=0
temp=n
while temp >0:
    factor=1
    i=1
    reminder=temp%10
    while i<=reminder:
        factor=factor*i
        i=i+1
        print("\nfactor%d=%d" %(reminder,factor))
        sum=sum+factor
        temp=temp//10
    print("\n sun of factor of a given number%d=%d"%(n,sum))
    if sum==n:
        print("%d is strong number")
    else:
        print("%d is not strong number")
