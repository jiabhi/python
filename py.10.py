#wap to calculate all the bill amount of an item given its quantity sold  ,values discount and tax in python

def calculate_bill_amount(quantity, unit_price, discount_percent, tax_rate):
    # Calculate the total price before discount
    total_price_before_discount = quantity * unit_price

    # Calculate the discount amount
    discount_amount = (discount_percent / 100) * total_price_before_discount

    # Calculate the total price after discount
    total_price_after_discount = total_price_before_discount - discount_amount

    # Calculate the tax amount
    tax_amount = (tax_rate / 100) * total_price_after_discount

    # Calculate the total bill amount
    total_bill_amount = total_price_after_discount + tax_amount

    return total_bill_amount

# Example usage
quantity_sold = 10
unit_price = 50.0
discount_percent = 10.0
tax_rate = 5.0

# Calculate the total bill amount for the item
bill_amount = calculate_bill_amount(quantity_sold, unit_price, discount_percent, tax_rate)

# Display the total bill amount with proper formatting
print(f"Total bill amount: ${bill_amount:.2f}")
