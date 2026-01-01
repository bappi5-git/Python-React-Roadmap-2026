score = input('enter score')
try:
    sc = float(score)
except:
    print('error: not a number')
    quit()
if sc < 0.0 or sc > 1.0:
    print('Error: Score is out of range.')
elif sc >= 0.9:
    print('A')
elif sc >=0.8:
    print('B')
elif sc >= 0.7:
    print('C')
elif sc >= 0.6:
    print('D')
else:
    print('F')    

