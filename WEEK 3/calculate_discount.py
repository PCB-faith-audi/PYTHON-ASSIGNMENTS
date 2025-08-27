def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# Prompt user for input
try:
    price = float(input("Enter the price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price after discount
    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. original price: {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")

