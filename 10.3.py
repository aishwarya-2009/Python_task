import matplotlib.pyplot as plt
categories = ["Electronics", "Fashion", "Groceries", "Books"]
sales = [350, 200, 150, 100]
plt.pie(sales, labels=categories, autopct="%1.1f%%", startangle=90, shadow=True)
plt.title("Sales Distribution by Category")
plt.show()
