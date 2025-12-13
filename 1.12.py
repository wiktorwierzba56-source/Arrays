categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# find the index of the highest expense
max_index = expenses.index(max(expenses))

# print result
print("Most expensive category:", categories[max_index])
print("Amount:", expenses[max_index])
