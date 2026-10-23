
number = 15

if number >= 0:
    
    print("The number is positive.")
    
    # Nested if-else starts here
    if number % 2 == 0:
        print("It is also an even number.")
    else:
        print("It is also an odd number.")
        
else:
    # This block executes if the number is negative
    print("The number is negative.")
