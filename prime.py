n=int(input("enter the number"))
i=2
f=0
while(i<n//2):
    if(n%i==0):
        f=1
        break
    i+=1
    if(f==1):
        print("not a prime no")
    else:
        print(n,"is a prime no")
