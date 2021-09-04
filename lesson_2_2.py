# Gregory wants to know how many toys they can buy at Toys'N'Us

# They prioritize buying the most expensive toys first (For ejm. If Gregory had $50 
# they'd end up buying 2 Jumbo Baby Yoda Plushies, 1 Beyblade, and 5 Sticky Hands with 
# a remainder of $0.30 left)

# Have the user input how much money Gregory has then print how many of each 
# toy they can afford, as well as how much money they'd have remaining

if __name__ == '__main__':
    budget = float(input("Budget: "))
    jbypc = budget // 20
    budget -= jbypc * 20
    bc = budget // 7.2
    budget -= bc * 7.2
    shc = budget // 0.5
    budget -= shc * 0.5
    print(f'Jumbo Baby Yoda Plushies: {jbypc}\nBeyblades: {bc}\nStick Hands: {shc}\nRemaining Money: {budget}')
