balance = 500.0 
while True:
    print('\n--- ATM MENU ---')
    print('1. Check Balance')
    print('2. Withdraw Money')
    print('3. Exit')
    choice_inp = input('Choose an option (1-3): ')
    try:
        choice = int(choice_inp)
    except:
        print('Error: Please enter a valid number (1, 2, or 3).')
        continue 
    if choice == 1:
        print(f'Current Balance: ${balance:.2f}')    
    elif choice == 2:
        amount_inp = input('Enter amount to withdraw: ')
        try:
            amount = float(amount_inp)
            if amount > balance:
                print('Insufficient funds!')
            elif amount <= 0:
                print('Please enter a positive amount.')
            else:
                balance = balance - amount
                print(f'Withdrawal successful! New balance: ${balance:.2f}')
        except:
            print('Error: Please enter a numeric amount.')        
    elif choice == 3:
        print('Thank you for using the ATM. Goodbye!')
        break     
    else:
        print('Invalid choice. Please select 1, 2, or 3.')