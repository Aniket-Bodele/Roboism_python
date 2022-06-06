lst=[]
lst2=[]
n=int(input("Enter number of element"))
for i in range(0,n):
    ele=(input("Enter the input"))
    lst.append(ele)
for i in  range(0,n):
    lst2.append(ord(lst[i]))

min=lst2[0]

for i in range(0,n-1):
    for j in range(i+1,n):
        if(lst2[i]>lst2[j]):
            temp=lst[i]

            lst[i]=lst[j]
            lst[j]=temp
for i in range(0,n):
     print(lst[i])

