def longest_valid_parentheses(s: str) -> int:
    # Initialize stack with -1 to serve as a base boundary for valid substrings
    stack = [-1]
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            # Store the index of the opening bracket
            stack.append(i)
        else:
            # Pop the last opening bracket index or boundary
            stack.pop()
            
            if not stack:
                # If stack is empty, this ')' is unmatched; push its index as a new boundary
                stack.append(i)
            else:
                # Calculate length by subtracting current index from the last element in stack
                current_length = i - stack[-1]
                if current_length > max_length:
                    max_length = current_length
                    
    return max_length
