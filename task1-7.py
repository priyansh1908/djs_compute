row=int(input("enter number of rows you want to print"))
char=ord("A")
for i in range(row):
    for j in range(i+1):
        if i%2==0:
            print(chr(char),end="")
        else:
            print(int(char)-64,end="")
        char=char+1
    print()    