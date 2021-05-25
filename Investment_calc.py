investment_amt = float(input('What is your investment amount: '))
interest_rate = float(input('Enter expected interest: '))
years = int(input('Years for interest: '))

interest_rate = interest_rate

for i in range(years):
    investment_amt = investment_amt + (investment_amt * interest_rate)

print('Your earnings are ${:.2f} after {} years.'.format(investment_amt, years))

