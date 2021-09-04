# Set the variable in_list to whatever value you want. Let's use 
# [ 5, 2, 3, 1, 4, 6, 8, 7 ] as an example.

# Use for loops, while loops, and whatever else we've learned to 
# set the variable x to the length of in_list - but you may NOT use len! 
# Try to mimic the behavior of len.

if __name__ == '__main__':
    in_list = [5, 2, 3, 1, 4, 6, 8, 7]
    x = 0
    for i in in_list:
        x += 1
    print(x)
