# Account balence

balance = 10000
class AcoountBalanceException(Exception):
    pass
def withdrow(amt):
    global balance
    if balance - amt < 5000:
        raise AcoountBalanceException('Amount cannot be less than 5000.')
    else:
        balance = balance - amt
        print(balance)
amt = int(input('Amount to be withdrow:'))
try:
    withdrow(amt)
except AcoountBalanceException as e:
    print(e)
