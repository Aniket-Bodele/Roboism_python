n=int(input("Number till which prime number has to be evaluated\n"))
i=1
while(i<=n) :
    count =0
    j=1
    while(j<=i):
        if(i%j==0):
            count+=1
        j=j+1
    if(count==2):
        print("\t",i)
    i=i+1