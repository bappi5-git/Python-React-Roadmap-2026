def computepay(hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_rate = rate * 1.5
        overtime_pay = overtime_hours * overtime_rate
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay

hours_input = input('Enter hours')
rate_input = input('Enter rate')
hrs = float(hours_input)
rate = float(rate_input)

p = computepay(hrs, rate)
print('pay:', p)

