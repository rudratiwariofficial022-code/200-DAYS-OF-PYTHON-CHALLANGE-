num1 , num2 = map(int,input().split())

ans = 0
pos = 1 
carry = 0

while num1 > 0 or num2 >0:
    ld1 = num1 % 10
    ld2 = num2 % 10 
    total = ld1 + ld2 + carry 
    carry = total //10
    ans = ans +(total % 10) * pos 
    pos *= 10 
    num1 //= 10
    num2 //= 10
if carry == 1:
    ans = ans +carry * pos 
print(ans) 