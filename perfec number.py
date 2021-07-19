n=int(input("enter the number"))
i=1
sum=0
while (i<n):
    if (n%i==0):
        sum=sum+i
    i=i+1
if (sum==n):
    print(n,"is perfact number",n)
else:
    print(n,"is not perfact number",n)