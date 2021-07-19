# rows = 5
# # reverse loop
# for i in range(rows, 0, -1):
#     num = i
#     for j in range(0, i):
#         print(num, end=' ')
#     print("\r")


r=5
i=1
while i<=r:
    num=1
    j=1
    while j<=i:
        print(num*r,end=" ")
        j=j+1
    print( )
    i=i+1

