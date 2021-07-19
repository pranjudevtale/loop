rows = 5
# reverse loop
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

r=5
i=0
while i<r:
    num=i
    j=0
    while j<=i:
        print(num,end=" ")
        j=j+1
    print()
    i=i+1