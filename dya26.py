N= int(input())
def palindrome(N):
    original = N
    reverse = 0

    while N >0:
        digit = N % 10 
        reverse = reverse * 10 + digit 
        N = N // 10 

    if original == reverse:
        print("Yes")
    else:
        print("No")
palindrome(N)