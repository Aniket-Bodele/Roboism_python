lst=[]
lst2=[]
n=int (input("Enter the number of inputs\n"))
for i in range(0,n):
    ele=input("Enter the element")
    lst.append(ele)
j=0
k=0
while((j<=n-1)):
      lst2.append(lst[j])
      lst2.append(lst[j])
      j+=1

for i in range(len(lst2)):
    print(lst2[i],end='')