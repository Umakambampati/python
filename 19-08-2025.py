n=int(input("enter a number"))
temp=n
l=len(str(n))
sum=0
while temp>0:
    rem=temp%10
    sum+=rem**l
    temp=temp//10
if sum==n:
    print("armstrong")
else:
    print("not armstrong")


    

