def print_fibonacci(length):
    fibonacci_sequence = []  # Initialize an empty list
    
    # If the length is 0, return an empty list
    if length == 0:
        pass  # No need to calculate Fibonacci sequence
    
    # If the length is 1, only the first number (0) should be included
    elif length == 1:
        fibonacci_sequence.append(0)
    
    # For lengths greater than 1, generate the Fibonacci sequence
    else:
        fibonacci_sequence = [0, 1]  # Start with the first two Fibonacci numbers
    
        # Generate Fibonacci sequence until the desired length
        while len(fibonacci_sequence) < length:
            next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_fibonacci)
    
    print(fibonacci_sequence)
