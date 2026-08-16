print("=" * 50)
print("        DAY 02 - SIMPLE BILL CALCULATOR")
print("=" * 50)

while True:
    print("\nEnter Customer Details")
    customer_name = input("Customer Name : ")

    print("\nEnter Product Details")
    product_name = input("Product Name  : ")
    price = float(input("Price (₹)     : "))
    quantity = int(input("Quantity      : "))

    # Calculations
    subtotal = price * quantity
    gst = subtotal * 0.18
    total = subtotal + gst

    # Print Bill
    print("\n" + "=" * 50)
    print("                 BILL RECEIPT")
    print("=" * 50)
    print(f"Customer Name : {customer_name}")
    print(f"Product Name  : {product_name}")
    print(f"Price         : ₹{price:.2f}")
    print(f"Quantity      : {quantity}")
    print("-" * 50)
    print(f"Subtotal      : ₹{subtotal:.2f}")
    print(f"GST (18%)     : ₹{gst:.2f}")
    print("-" * 50)
    print(f"TOTAL BILL    : ₹{total:.2f}")
    print("=" * 50)

    # Another Bill
    choice = input("\nDo you want to create another bill? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using the Bill Calculator!")
        print("Have a Great Day!")
        break