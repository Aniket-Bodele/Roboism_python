def password (s) :
    k=len(s)
    j=""
    i=0
    while(i<(k-4)):
       j=( j+"*" )
       i= (i+1)
    while(i<k) :
       j=( j+s[i])
       i= (i+1)
    return j

p=input("Enter the password\n")

k=password(p)
print(k)