def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Final price after applying {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: {final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values for price and discount.")
