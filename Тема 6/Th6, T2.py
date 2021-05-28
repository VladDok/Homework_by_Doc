# Input data:

# stock = {
#    "banana": 6,
#    "apple": 0,
#    "orange": 32,
#    "pear": 15
#}
#prices = {
#    "banana": 4,
#   "apple": 2,
#    "orange": 1.5,
#    "pear": 3
#}
# Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total price of stock.

print('Hello! This program can help you to count your total prize for stock.\
For it you need to create dicts called stock and prices.\n')
  
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }
       
list_for_operation = []

for value in stock.values():
    list_for_operation.append(value)
    
i = 0     
for key in stock:
    list_for_operation[i] *= prices[key]
    i += 1
    
total_prize_for_stock = sum(list_for_operation)

print('Total sum:', total_prize_for_stock)

    