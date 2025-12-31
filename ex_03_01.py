hrs = input('enter hours')
rate = input('enter rate')
h = float(hrs)
r = float(rate)
if h >40:
    regular_pay = 40 * r
    overtime_hours = h - 40
    overtime_rate = r * 1.5
    overtime_pay = overtime_hours * overtime_rate
    pay = regular_pay + overtime_pay
else:
    pay = h * r
print('Pay:', pay)

