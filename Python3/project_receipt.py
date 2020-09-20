lovely_loveseat_description = "Levely Loveseat. Tufted blend on wood. 32 inches high x 40 inches wide x 30 inches dee. Red or white."
lovely_loveseat_price = 254.00
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black"
stylish_settee_price = 180.50
luxurious_lamp_description = "Luxurious Lamp. Glass and Iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15
sales_tax = .088
customer_one_total = lovely_loveseat_price
# customer_one_intemization = lovely_loveseat_description
customer_one_tax = customer_one_total * sales_tax
final_price = customer_one_tax + customer_one_total
print("Customer One Items:")
print(lovely_loveseat_description)
print("Customer One Total:")
print(lovely_loveseat_price)
print("Sales Tax")
print(customer_one_tax)
print("Total")
print(final_price)
