temperature = 37

if temperature > 37:
    print("You have a fever")
else:
    print("You are doing great in this cold weather")



bill = 1900

discount = 0.5

if bill > 2000:
    print("You have a 20% discount on your"+ " " + str(bill) + " " + "bill" + " " + "You will pay" + " " + str(bill - (bill * discount)))

else:
    print("You need to spend a little more than 2000 to get a discount")