# rows = 10
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(i * j, end=' ')
#     print()


i=0
while i<=10:
    j=0
    while j<=i:
        print(i*j,end="  ")
        j=j+1
    print()
    i=i+1