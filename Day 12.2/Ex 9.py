def grocery_discount(price, discount):
    final_price = price - (price * discount / 100)
    return final_price

price = float(input("Enter the price: "))
discount = float(input("Enter the discount percentage: "))

final = grocery_discount(price, discount)
print(f"The final price after {discount}% discount is: ₹{round(final, 2)}")
