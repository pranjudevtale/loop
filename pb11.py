# num = 4
# counter = 0
# for x in range(0, num):
#     for y in range(0, x + 1):
#         print(counter, end=" ")
#         counter = 2 ** (x + 1)
#     print()

# rows = 7
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print(i * j, end='  ')
#     print()


r=7
i=1
while i<=r:
    j=1
    while j<=8:
        print(i * j,end='  ')
        j=j+1
    print()
    i=i+1
