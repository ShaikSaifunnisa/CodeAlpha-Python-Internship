# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

stock_prices = {
    "TCS": 4000,
    "INFY": 2000,
    "RELIANCE": 1500,
    "HDFCBANK": 1800,
    "ITC": 500
}

total_investment = 0

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable stocks:")
for stock in stock_prices:
    print(stock, "- ₹", stock_prices[stock])

print("\nEnter 'done' when you finish.")

while True:
    stock = input("\nEnter stock name: ").strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print("Investment for", stock, ":", "₹", investment)

print("\n-----------------------------------")
print("Total Investment: ₹", total_investment)
print("-----------------------------------")
print("Thank you for using the Stock Portfolio Tracker!")
