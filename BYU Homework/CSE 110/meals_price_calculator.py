child_meal = float(input("what is the price of child's meal?: "))
adult_meal = float(input("what is the price of adult meal?: "))
num_of_children = int(input("how many children are there?: "))
num_of_adult = int(input("how many adult are there?: "))
tax_rate = float(input("what is the sales tax rate?: "))

sub_total = num_of_children * child_meal + num_of_adult * adult_meal
sales_tax = sub_total * tax_rate /100
total = sub_total + sales_tax
payment_amount = float(input("what's the payment amount?: "))
change = payment_amount - total

print((f"Subtotal is: {sub_total}"))
print((f"Sales tax is: {sales_tax}"))
print((f"Total is: {total}"))
print((f"Change is: {change}"))