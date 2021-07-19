# rows = 5
# b = 0
# # reverse for loop from 5 to 0
# for i in range(rows, 0, -1):
#     b += 1
#     for j in range(1, i + 1):
#         print(b, end=' ')
#     print('\r')

r=5
b=0
i=1
while i<=5:
    b=b+1
    j=0
    while j<=5:
        print(r,"* ",end=" "*1)
        j=j+1
        r=r+1
    print( )
    i=i+1
