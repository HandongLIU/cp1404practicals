# Handong LIU
Total = 0
Number_of_items = int(input("Number of items : "))
while Number_of_items < 0:
    print("Invalid Number of Items")
    Number_of_items = int(input("Number of items : "))
for i in range(Number_of_items):
    price = float(input("price of items: "))
    Total += price
    if Total > 100:
        Total *= 0.9

print("Total price for ",Number_of_items," item is $",Total,sep='')


