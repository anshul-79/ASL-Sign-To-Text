def table(num):
    tot=0
    while(num>0):
        tot+=num%10
        num=num//10
    return tot


n=int(input("Enter a number "))

print("result : ",table(n))