rows=6
for i in range(1,rows+1):
    for j in range(1,2*rows):
        if i==rows or i+j==rows+1 or j-i==rows-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()