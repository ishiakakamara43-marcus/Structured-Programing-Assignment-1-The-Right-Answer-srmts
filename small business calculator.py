# ============================================================
# PROG103 - PRINCIPLES OF STRUCTURED PROGRAMMING
# Assignment 1 - Individual Assignment
# Title   : Small Business Sales Calculator
# System  : Terminal-Based Python Application
# SDG     : SDG 8 - Decent Work and Economic Growth
# ============================================================

# ------------------- CONSTANTS ----------------------------
TAX_RATE = 0.15          # 15% tax rate
DISCOUNT_THRESHOLD = 5   # Minimum items to qualify for discount
DISCOUNT_RATE = 0.10     # 10% discount for bulk purchases


# ------------------- FUNCTIONS ----------------------------

def display_welcome():
    """Display the welcome banner for the application."""
    print("=" * 55)
    print("     SMALL BUSINESS SALES CALCULATOR")
    print("     Empowering Local Businesses - Sierra Leone")
    print("=" * 55)
    print("  SDG 8: Decent Work and Economic Growth")
    print("=" * 55)
    print()


def get_product_details():
    """
    Prompt the user to enter product name, price, and quantity.
    Returns a dictionary with product details.
    """
    print("\n--- Enter Product Details ---")

    name = input("Product Name       : ").strip()

    # Validate price input
    while True:
        try:
            price = float(input("Unit Price (NLe)   : "))
            if price <= 0:
                print("  [!] Price must be greater than 0. Try again.")
            else:
                break
        except ValueError:
            print("  [!] Invalid input. Please enter a number.")

    # Validate quantity input
    while True:
        try:
            quantity = int(input("Quantity Sold      : "))
            if quantity <= 0:
                print("  [!] Quantity must be at least 1. Try again.")
            else:
                break
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")

    return {"name": name, "price": price, "quantity": quantity}


def apply_discount(quantity, subtotal):
    """
    Apply a discount if quantity meets or exceeds DISCOUNT_THRESHOLD.
    Returns the discount amount.
    """
    if quantity >= DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_RATE
        return discount
    return 0.0


def calculate_totals(price, quantity):
    """
    Calculate subtotal, discount, tax, and final total for a product.
    Returns a dictionary with all calculated values.
    """
    subtotal = price * quantity
    discount = apply_discount(quantity, subtotal)
    discounted = subtotal - discount
    tax = discounted * TAX_RATE
    total = discounted + tax

    return {
        "subtotal": subtotal,
        "discount": discount,
        "discounted": discounted,
        "tax": tax,
        "total": total
    }


def display_receipt(product, totals):
    """
    Display a formatted receipt for a single product sale.
    """
    print("\n" + "-" * 45)
    print("             SALES RECEIPT")
    print("-" * 45)
    print(f"  Product        : {product['name']}")
    print(f"  Unit Price     : NLe {product['price']:>10.2f}")
    print(f"  Quantity       : {product['quantity']:>10}")
    print("-" * 45)
    print(f"  Subtotal       : NLe {totals['subtotal']:>10.2f}")

    if totals['discount'] > 0:
        print(f"  Discount (10%) : NLe {totals['discount']:>10.2f} -")

    print(f"  Tax (15%)      : NLe {totals['tax']:>10.2f} +")
    print("-" * 45)
    print(f"  TOTAL          : NLe {totals['total']:>10.2f}")
    print("-" * 45)

    if totals['discount'] > 0:
        print("  * Bulk discount applied (5+ items)")
    print()


def display_summary(records):
    """
    Display a summary of all sales transactions entered in the session.
    """
    print("\n" + "=" * 55)
    print("              SALES SUMMARY REPORT")
    print("=" * 55)
    print(f"  {'#':<4} {'Product':<18} {'Qty':<6} {'Total (NLe)':>12}")
    print("-" * 55)

    grand_total = 0.0
    for i, record in enumerate(records, start=1):
        print(f"  {i:<4} {record['name']:<18} {record['quantity']:<6} {record['total']:>12.2f}")
        grand_total += record["total"]

    print("=" * 55)
    print(f"  {'Grand Total':<28} NLe {grand_total:>10.2f}")
    print("=" * 55)

    # Performance classification
    print()
    if grand_total >= 1000:
        print("  [STATUS] Excellent sales performance today!")
    elif grand_total >= 500:
        print("  [STATUS] Good sales performance today.")
    else:
        print("  [STATUS] Below target. Consider promotions.")
    print()


def display_menu():
    """Display the main menu options."""
    print("\n  MENU OPTIONS:")
    print("  [1] Add a new sale")
    print("  [2] View sales summary")
    print("  [3] Exit")
    print()


# ------------------- MAIN PROGRAM -------------------------

def main():
    """Main function - entry point of the application."""

    display_welcome()

    records = []      # List to store all sales records
    running = True    # Control variable for the main loop

    while running:
        display_menu()
        choice = input("  Enter your choice (1/2/3): ").strip()

        if choice == "1":
            # --- Add a new sale ---
            product = get_product_details()
            totals = calculate_totals(product["price"], product["quantity"])
            display_receipt(product, totals)

            # Save record for summary
            records.append({
                "name": product["name"],
                "quantity": product["quantity"],
                "total": totals["total"]
            })
            print("  [✓] Sale recorded successfully.")

        elif choice == "2":
            # --- View sales summary ---
            if len(records) == 0:
                print("\n  [!] No sales recorded yet. Add a sale first.")
            else:
                display_summary(records)

        elif choice == "3":
            # --- Exit ---
            if len(records) > 0:
                display_summary(records)
            print("  Thank you for using the Sales Calculator.")
            print("  Supporting local business in Sierra Leone!\n")
            running = False

        else:
            print("\n  [!] Invalid choice. Please enter 1, 2, or 3.")


# ------------------- ENTRY POINT --------------------------
if __name__ == "__main__":
    main()