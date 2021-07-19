# rows = 9
# for i in range(1, rows):
#     for j in range(-1 + i, -1, -1):
#         print(format(2 ** j, "4d"), end=' ')
#     print("")


r=9
i=1
while i<=r:
    j=0
    while j<=i:
        print(format(2**j,"4d"),end="  ")
        j=j+1
    print(" ")
    i=i+1