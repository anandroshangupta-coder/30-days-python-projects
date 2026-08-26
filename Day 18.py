# ==========================================
# Day 18 - Inventory Management System
# 30 Days Python GitHub Project Challenge
# ==========================================

import json
import os


FILE_NAME = "inventory.json"


print("======================================")
print("      INVENTORY MANAGEMENT SYSTEM")
print("======================================")


# ==========================================
# Product Class
# ==========================================

class Product:

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    # Convert product to dictionary
    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    # Display product
    def display(self):
        total_value = self.price * self.quantity

        print(f"\nProduct ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Price      : ₹{self.price:.2f}")
        print(f"Quantity   : {self.quantity}")
        print(f"Stock Value: ₹{total_value:.2f}")


# ==========================================
# Inventory Class
# ==========================================

class Inventory:

    def __init__(self):
        self.products = {}
        self.load_inventory()

    # Save inventory to JSON file
    def save_inventory(self):

        data = {}

        for product_id, product in self.products.items():
            data[product_id] = product.to_dict()

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    # Load inventory from JSON file
    def load_inventory(self):

        if not os.path.exists(FILE_NAME):
            return

        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            for product_id, details in data.items():

                self.products[product_id] = Product(
                    details["product_id"],
                    details["name"],
                    details["price"],
                    details["quantity"]
                )

        except (json.JSONDecodeError, KeyError):
            print("⚠️ Could not load inventory file.")

    # Add product
    def add_product(self):

        product_id = input("\nEnter product ID: ")

        if product_id in self.products:
            print("❌ Product ID already exists.")
            return

        name = input("Enter product name: ")

        try:
            price = float(input("Enter product price: ₹"))
            quantity = int(input("Enter quantity: "))

            if price < 0 or quantity < 0:
                print("❌ Price and quantity cannot be negative.")
                return

            product = Product(
                product_id,
                name,
                price,
                quantity
            )

            self.products[product_id] = product

            self.save_inventory()

            print("✅ Product added successfully!")

        except ValueError:
            print("❌ Please enter valid price and quantity.")

    # View products
    def view_products(self):

        print("\n======================================")
        print("          ALL PRODUCTS")
        print("======================================")

        if not self.products:
            print("No products available.")
            return

        for product in self.products.values():
            product.display()

        print("\n======================================")

    # Search product
    def search_product(self):

        product_id = input("\nEnter product ID to search: ")

        if product_id in self.products:

            print("\n✅ Product found!")
            self.products[product_id].display()

        else:
            print("❌ Product not found.")

    # Update stock
    def update_stock(self):

        product_id = input("\nEnter product ID: ")

        if product_id not in self.products:
            print("❌ Product not found.")
            return

        try:
            quantity = int(input("Enter new quantity: "))

            if quantity < 0:
                print("❌ Quantity cannot be negative.")
                return

            self.products[product_id].quantity = quantity

            self.save_inventory()

            print("✅ Stock updated successfully!")

        except ValueError:
            print("❌ Please enter a valid quantity.")

    # Update price
    def update_price(self):

        product_id = input("\nEnter product ID: ")

        if product_id not in self.products:
            print("❌ Product not found.")
            return

        try:
            price = float(input("Enter new price: ₹"))

            if price < 0:
                print("❌ Price cannot be negative.")
                return

            self.products[product_id].price = price

            self.save_inventory()

            print("✅ Price updated successfully!")

        except ValueError:
            print("❌ Please enter a valid price.")

    # Delete product
    def delete_product(self):

        product_id = input("\nEnter product ID to delete: ")

        if product_id in self.products:

            deleted_product = self.products.pop(product_id)

            self.save_inventory()

            print(
                f"✅ '{deleted_product.name}' "
                "deleted successfully."
            )

        else:
            print("❌ Product not found.")

    # Inventory statistics
    def show_statistics(self):

        if not self.products:
            print("\n❌ No products available.")
            return

        total_products = len(self.products)
        total_quantity = sum(
            product.quantity
            for product in self.products.values()
        )

        total_value = sum(
            product.price * product.quantity
            for product in self.products.values()
        )

        print("\n======================================")
        print("        INVENTORY STATISTICS")
        print("======================================")
        print(f"Total Products : {total_products}")
        print(f"Total Quantity : {total_quantity}")
        print(f"Total Value    : ₹{total_value:.2f}")
        print("======================================")


# ==========================================
# Create Inventory
# ==========================================

inventory = Inventory()


# ==========================================
# Main Menu
# ==========================================

while True:

    print("\n======================================")
    print("          INVENTORY MENU")
    print("======================================")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Update Price")
    print("6. Delete Product")
    print("7. Inventory Statistics")
    print("8. Exit")
    print("======================================")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":

        inventory.add_product()

    elif choice == "2":

        inventory.view_products()

    elif choice == "3":

        inventory.search_product()

    elif choice == "4":

        inventory.update_stock()

    elif choice == "5":

        inventory.update_price()

    elif choice == "6":

        inventory.delete_product()

    elif choice == "7":

        inventory.show_statistics()

    elif choice == "8":

        print("\n======================================")
        print("       Thank You! Goodbye 👋")
        print("======================================")
        break

    else:

        print("❌ Invalid choice! Please select 1-8.")