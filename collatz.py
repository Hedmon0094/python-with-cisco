# Read the initial number
c0 = int(input("Enter a natural number: "))

# Ensure the input is a valid natural number
if c0 <= 0:
    print("Please enter a non-negative and non-zero integer.")
else:
    steps = 0  # Initialize step counter

    # Execute Collatz's steps
    while c0 != 1:
        print(c0)
        if c0 % 2 == 0:
            c0 //= 2
        else:
            c0 = 3 * c0 + 1
        steps += 1

    # Print the final value of c0 and the number of steps
    print(c0)
    print("Number of steps:", steps)
