minn = 9 

def solve(num):
    global minn
    if num ==0:
        return 
    ld = num % 10 
    if ld < minn:
        minn = ld 
    solve(num//10)
solve(num)
print(minn)