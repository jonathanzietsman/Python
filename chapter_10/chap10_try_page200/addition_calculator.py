while True:
    try:
        a = int(input('Number 1: '))
        b = int(input('Number 2: '))
        print(a + b)
        continue_prompt = input("Do you want to add more numbers? (yes/no): ").strip().lower()
        if continue_prompt != 'yes':
            print("Goodbye!")
            break
    except ValueError:
        print('Error: Please enter valid numbers.')

