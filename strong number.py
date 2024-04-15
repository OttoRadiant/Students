n=int(input("Enter the value"))
s=0
num=n
while(n>0):
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact= fact*i
    s= s+fact
    n= n//10
if(s==num):
    print("it is a strong number")
else:
    print("Not a strong number")
    
    
