import art
from replit import clear

# Step-1 : take the inputs and assign it to a dictionary and make the while loop for consistency.
print(art.logo)
users = [{
  "name":input("What is your name?: "),
  "bid":int((input("What is your bid?: $")))
}]
again = input("Are there any other bidders? Type 'yes or 'no'.\n")
while again == "yes":
  clear()
  new_user = {
  "name":input("What is your name?: "),
  "bid":int(input("What is your bid?: $"))
  }
  users.append(new_user)
  again = input("Are there any other bidders? Type 'yes or 'no'.\n")
# Step-2 : Select the winner with the biggest int value
bids = []
for dic in users :
  bids.append (dic["bid"])
winner_value = max(bids)
winner_name = ""
for dic in users:
  if dic["bid"] == winner_value:
    winner_name = dic["name"]
print(f"The winner is {winner_name} with a bid of {winner_value}")



