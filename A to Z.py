num=int(input("enter the number "))
k=65
i=1
while i<num:
    j=1
    while j<i+1:
        a=chr(k)
        print(" ",a,end="")
        j=j+1
        k=k+1
    print(" ")
    i=i+1

# size = 7
# asciiNumber = 65
# m = (2 * size) - 2
# for i in range(0, size):
#     for j in range(0, m):
#         print(end=" ")
#     m = m - 1
#     for j in range(0, i + 1):
#         character = chr(asciiNumber)
#         print(character, end=' ')
#         asciiNumber += 1
#     print(" ")
