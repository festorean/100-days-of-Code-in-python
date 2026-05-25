# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art


print(art.logo)
dashboard = {}
highest_bid = 0
winner = ""
while True:
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))
    dashboard[name] = bid
    more_bidder = input("Are there any other bidder? Type 'yes' or 'no':\n ").lower()
    if more_bidder == 'no':
        break
    print("\n" * 20)

for bidder in dashboard:
    if dashboard[bidder] > highest_bid:
        highest_bid = dashboard[bidder]
        winner = bidder
print(f"The winner is  {winner} with a bid of ${highest_bid}")
