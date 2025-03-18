# init a flag to control loop
running = True

# loop as long flag true 
while running:
    # user input remove whitesp and chang lower
    user_input = input('enter number 1-10 or "q" to quit: ').strip().lower()
    
    # check if user want quit
    if user_input == 'q':
        running = False
        break
    
    # check in is valid digit
    if not user_input.isdigit():
        print('Not digit')
        continue
    
    # convert digit to int
    number = int(user_input)
    
    # check if num is 5 
    if number == 5:
        print('You entered 5, exiting')
        running = False
        break
    
    # check if num is outside range -- next iteration 
    if number < 1 or number > 10:
        print('Not in range')
        continue
    
    