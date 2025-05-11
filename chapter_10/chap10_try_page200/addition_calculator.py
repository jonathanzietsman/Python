# Main program loop - continues until user chooses to exit
while True:
    try:
        # Get two numbers from the user and convert them to integers
        a = int(input('Number 1: '))
        b = int(input('Number 2: '))
        
        # Display the sum of the two numbers
        print(a + b)
        
        # Ask if user wants to continue with more calculations
        # strip() removes whitespace, lower() makes the input case-insensitive
        continue_prompt = input("Do you want to add more numbers? (yes/no): ").strip().lower()
        
        # If user doesn't type 'yes', exit the program
        if continue_prompt != 'yes':
            print("Goodbye!")
            break
            
    except ValueError:
        # Handle the error if user enters non-numeric input
        print('Error: Please enter valid numbers.')

