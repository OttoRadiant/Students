n=int(input("Enter the value"))
n1=n
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
    

if rev==n1:
    print("this is pallindrome")
else:
    print("not a pallindrome")
