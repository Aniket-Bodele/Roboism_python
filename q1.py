lt=[]
n=int(input("Enter the number of elements for list\n"))
for i in range(0,n):
    ele=int(input("Enter the element\n"))
    lt.append(ele)

way=input("Enter the function to perform\n")
if(way=="asc"):
    lt.sort()
elif(way=="desc"):
    lt.reverse()
else:
    print("Enter the correct function")
for i in range(len(lt)):
    print (lt[i])