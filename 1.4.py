x=float(input("enter the cost price of the scooter(Rs.):"))
y=float(input("enter the repair cost(Rs.):"))
z=float(input("enter the seeling price(Rs.):"))
#calculate total cost price
cost_price=x+y
#ensure selling price is greater than cost price
if z<=cost_price:
    print("No gain.selling price must be greater than total cost")
else:
    gain=z-cost_price
    gain_percent=(gain/cost_price)*100
#display result
    print(f"Total cost price=Rs.{cost_price}")
    print(f"Gain=Rs.{gain}")
    print(f"Gain Percent={gain_percent:.2f}%")



        
