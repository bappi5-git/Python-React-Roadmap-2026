largest = None
smallest = None
while True:
    num = input('Enter number: ')
    if num == 'done':
        break    
    try:
        ival = int(num)    
    except:
        print('Inavalid input')
        continue
        
    if largest is None:
        largest = ival
    elif ival > largest:
        largest = ival    
    if smallest is None:
        smallest = ival
    elif ival < smallest:
        smallest = ival
    

print('maximum is', largest)
print('minimum is', smallest)

