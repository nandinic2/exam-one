# Client needs to know the final price of shopping after a black friday sale.

clothes = int(input('How many items of the same clothing did you buy?'))
# Asks the user how many items were bought.
cost = int(input('How did one item cost?'))
# The cost of the item of clothing.

def discount(int, val):
    sale = 0
    # Sets the sale to zero.
    if int <= 2:
        # If the user buys less than two items.
        sale = int * val * 0.05
        # Sale is the number of clothes multplied by how much they cost and the 5% discount.
        return int * val - sale
        # Returns amount that should be paid.
    elif 3 <= int <= 6:
        sale = int * val * 0.1
        # Sale is the number of clothes multiplied by how much they clost and the 10% discount.
        return int * val - sale
        # Returns amount that should be paid.
    elif 10 <= int <= 15:
        # If the user buys ten or more items or at least fifteen.
        sale = int * val * 0.15
        # Sale is the number of clothes multiplied by how much they clost and the 15% discount.
        return int * val - sale
        # Returns amount that should be paid.
    else:
        # If the user buys more than fifteen items.
        sale = int * val * 0.2
        # Sale is the number of clothes multiplied by how much they clost and the 20% discount.
        return int * val - sale

print(discount(clothes, cost))
