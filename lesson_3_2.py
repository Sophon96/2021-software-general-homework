################################################
# Create a program to accept words from a user, and add them to a dictionary. 
# At the end, use print(mydict) to print out the user's work to them

if __name__ == '__main__':
    a = dict()
    while (x := input("Enter a word, or leave blank to end: ")) != "":
        y = input("Enter the word's translation: ")
        a[x] = y

    print(a)
