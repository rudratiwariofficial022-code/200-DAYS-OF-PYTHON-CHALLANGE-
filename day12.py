ef countdown(n):
    # 1. Base Case: stop when n reaches 0
    if n <= 0:
        print("Blastoff!")
        return
    
    # 2. Action
    print(n)
    
    # 3. Recursive Case: function calls itself with a modified argument
    countdown(n - 1)

# Start the function
countdown(5)
