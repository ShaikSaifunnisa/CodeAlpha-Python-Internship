# ==========================================
# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker
# ==========================================

stock_prices = {
    "TCS": 4000,
    "INFY": 2000,
    "RELIANCE": 1500,
    "HDFCBANK": 1800,
    "ITC": 500
}

portfolio = {}
transactions = []


def show_stocks():
    print("\n========== AVAILABLE STOCKS ==========")

    for stock, price in stock_prices.items():
        print(f"{stock:<12} ₹{price:,.2f}")

    print("======================================")


def buy_stock():
    show_stocks()

    stock = input("\nEnter stock name to BUY: ").upper()

    if stock not in stock_prices:
        print("❌ Stock not found.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            return

    except ValueError:
        print("❌ Please enter a valid number.")
        return

    price = stock_prices[stock]
    investment = price * quantity

    if stock in portfolio:
        old_quantity = portfolio[stock]["quantity"]
        old_investment = portfolio[stock]["investment"]

        portfolio[stock]["quantity"] += quantity
        portfolio[stock]["investment"] += investment

    else:
        portfolio[stock] = {
            "quantity": quantity,
            "investment": investment
        }

    transactions.append({
        "type": "BUY",
        "stock": stock,
        "quantity": quantity,
        "price": price
    })

    print("\n✅ BUY successful!")
    print(f"Stock: {stock}")
    print(f"Quantity: {quantity}")
    print(f"Price per share: ₹{price:,.2f}")
    print(f"Investment: ₹{investment:,.2f}")


def sell_stock():
    if not portfolio:
        print("\n❌ Your portfolio is empty.")
        return

    show_portfolio()

    stock = input("\nEnter stock name to SELL: ").upper()

    if stock not in portfolio:
        print("❌ You do not own this stock.")
        return

    try:
        quantity = int(input("Enter quantity to sell: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            return

    except ValueError:
        print("❌ Please enter a valid number.")
        return

    owned_quantity = portfolio[stock]["quantity"]

    if quantity > owned_quantity:
        print(f"❌ You only own {owned_quantity} shares.")
        return

    current_price = stock_prices[stock]

    average_cost = (
        portfolio[stock]["investment"] / owned_quantity
    )

    sell_value = current_price * quantity
    cost_value = average_cost * quantity
    profit_loss = sell_value - cost_value

    portfolio[stock]["quantity"] -= quantity
    portfolio[stock]["investment"] -= cost_value

    if portfolio[stock]["quantity"] == 0:
        del portfolio[stock]

    transactions.append({
        "type": "SELL",
        "stock": stock,
        "quantity": quantity,
        "price": current_price
    })

    print("\n✅ SELL successful!")
    print(f"Stock: {stock}")
    print(f"Quantity sold: {quantity}")
    print(f"Sell value: ₹{sell_value:,.2f}")

    if profit_loss >= 0:
        print(f"Profit: ₹{profit_loss:,.2f}")
    else:
        print(f"Loss: ₹{abs(profit_loss):,.2f}")


def show_portfolio():
    print("\n========== MY PORTFOLIO ==========")

    if not portfolio:
        print("Your portfolio is empty.")
        print("=================================")
        return

    total_investment = 0
    total_current_value = 0

    for stock, data in portfolio.items():

        quantity = data["quantity"]
        investment = data["investment"]
        current_price = stock_prices[stock]

        current_value = quantity * current_price
        profit_loss = current_value - investment

        total_investment += investment
        total_current_value += current_value

        print(f"\nStock: {stock}")
        print(f"Quantity: {quantity}")
        print(f"Average cost: ₹{investment / quantity:,.2f}")
        print(f"Current price: ₹{current_price:,.2f}")
        print(f"Investment: ₹{investment:,.2f}")
        print(f"Current value: ₹{current_value:,.2f}")

        if profit_loss >= 0:
            print(f"Profit: ₹{profit_loss:,.2f}")
        else:
            print(f"Loss: ₹{abs(profit_loss):,.2f}")

    total_profit_loss = total_current_value - total_investment

    print("\n---------------------------------")
    print(f"Total investment: ₹{total_investment:,.2f}")
    print(f"Current value: ₹{total_current_value:,.2f}")

    if total_profit_loss >= 0:
        print(f"Total profit: ₹{total_profit_loss:,.2f}")
    else:
        print(f"Total loss: ₹{abs(total_profit_loss):,.2f}")

    print("=================================")


def show_transactions():
    print("\n========== TRANSACTION HISTORY ==========")

    if not transactions:
        print("No transactions yet.")
        print("========================================")
        return

    for number, transaction in enumerate(transactions, start=1):

        print(
            f"{number}. "
            f"{transaction['type']} | "
            f"{transaction['stock']} | "
            f"Quantity: {transaction['quantity']} | "
            f"Price: ₹{transaction['price']:,.2f}"
        )

    print("========================================")


def update_price():
    show_stocks()

    stock = input("\nEnter stock name to update: ").upper()

    if stock not in stock_prices:
        print("❌ Stock not found.")
        return

    try:
        new_price = float(input("Enter new price: ₹"))

        if new_price <= 0:
            print("❌ Price must be greater than 0.")
            return

    except ValueError:
        print("❌ Please enter a valid price.")
        return

    stock_prices[stock] = new_price

    print("\n✅ Stock price updated!")
    print(f"{stock} = ₹{new_price:,.2f}")


def main():

    while True:

        print("\n")
        print("==========================================")
        print("       STOCK PORTFOLIO TRACKER")
        print("==========================================")
        print("1. View available stocks")
        print("2. Buy stock")
        print("3. Sell stock")
        print("4. View my portfolio")
        print("5. View transaction history")
        print("6. Update stock price")
        print("7. Exit")
        print("==========================================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            show_stocks()

        elif choice == "2":
            buy_stock()

        elif choice == "3":
            sell_stock()

        elif choice == "4":
            show_portfolio()

        elif choice == "5":
            show_transactions()

        elif choice == "6":
            update_price()

        elif choice == "7":
            print("\nThank you for using Stock Portfolio Tracker! 📈")
            break

        else:
            print("❌ Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
