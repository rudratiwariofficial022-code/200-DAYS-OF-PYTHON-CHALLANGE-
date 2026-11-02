def countdown(number):
    # 1. Base Case: Stop when the number hits 0
    if number <= 0:
        print("Blast off! 🚀")
        return
    
    # 2. Action: Print the current number
    print(number)
    
    # 3. Recursive Case: Call the function again with a smaller number
    countdown(number - 1)

# Start the countdown from 3
countdown(3)
