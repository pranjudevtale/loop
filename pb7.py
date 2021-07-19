side=int(input("enter the length"))
count=0
b=0
while count<side:
    a=side-count
    print(a*"",(count*"* ")*1)
    count+=1
while count>=0:
    print(b*"" ,(count*"* ")*1)
    count-=1
    b+=1