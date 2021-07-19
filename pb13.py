# rows = 5
# last_num = 2 * rows
# even_num = last_num
# for i in range(1, rows + 1):
#     even_num = last_num
#     for j in range(i):
#         print(even_num, end=' ')
#         even_num -= 2
#     print("\r")


r=5
last_name=2*r
even_num=last_name
i=1
while i<=r:
    even_num=last_name
    j=1
    while j<=i:
        print(even_num,end=" ")
        even_num=2
        j=j+1
    print()
    i=i+1