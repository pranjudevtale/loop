# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, rows + 1):
#         if j <= i:
#             print(i, end=' ')
#         else:
#             print(j, end=' ')
#     print()

rows = 8
rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()
square = i * j
    




