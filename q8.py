lst=[]
x=0
n=int(input("Please enter the number of elements in string\n"))
for i in range(0,n):
     ele=input("Enter the element\n")
     lst.append(ele)
for i in range (0,n):
    if(ord(lst[i])<65):

        x+=int(lst[i])
print(x)
