# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = int(input('Extra payment start month: '))
extra_payment_end_month = int(input('Extra payment end month: '))
extra_payment = int(input('Extra payment: '))

while principal > 0:
    if extra_payment_start_month < extra_payment_end_month:
        payment = 2684.11 + extra_payment
        extra_payment_start_month += 1
    else:
        payment = 2684.11

    month += 1
    principal = round(principal * (1+rate/12) - payment, 2)
    total_paid = round(total_paid + payment, 2)
    if principal < 0:
        total_paid = round(total_paid + principal, 2)
        principal = 0
    print(f'{month:3} {total_paid:9} {principal:>0.2f}')

print('Total paid:', total_paid)
print('Months:', month)
