def circular_path(n, m):
    # Create the circular array
    array = list(range(1, n + 1))
    
    # Initialize variables
    path = []
    current_index = 0
    
    # Traverse the array with a step of m
    for _ in range(n):
        # Add the first element of the current interval to the path
        path.append(array[current_index])
        
        # Move forward by m-1 steps (since we are already on the first element)
        current_index = (current_index + m - 1) % n
    
    # Output the path
    print("Resulting path:", "".join(map(str, path)))

if __name__ == "__main__":
    while True:
        # Use input() to get values for n and m
        n = int(input("Enter the value of n: "))
        m = int(input("Enter the value of m: "))
        
        # Calculate and print the circular path
        circular_path(n, m)
        
        # Ask if the user wants to try again
        retry = input("Would you like to try again? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Exiting the program. Goodbye!")
            break
