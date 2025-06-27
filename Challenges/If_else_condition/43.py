# WAP to Cheak the discount on some fix amount.

amount = float(input(" Enter the amount on which discount is given:"))

if amount <= 1000:
    amount -= amount*10/100
    print("Discount will be 10%:",amount)
elif 1000 < amount <= 5000:
    amount -=  amount*20/100
    print("Discount will be 20%:",amount)
elif 5000 < amount <= 10000:
    amount -= amount*30/100
    print("Discount will be 30%:",amount)
elif 10000 < amount:
    amount -= amount*50/100
    print("Discount will be 50%:",amount)
else:
    print("There will be no any Discount")
