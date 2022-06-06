s1=int(input("Enter the first number"))
s2=input("Enter the operation")
s3=int (input("Enter the second number"))

if(s2=="+"):
    s4=s1+s3
elif(s2=="-"):
    s4=s1+s3
elif(s2=="*"):
    s4=s1*s3
elif(s2=="/"):
    s4=s1/s3
else:
    print("Print the correct operation")

print("Your solution is:",s4)
