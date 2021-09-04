# A student has taken 3 tests in a class, and wants to know their current grade 
# (which is only calculated by these tests). 

# Ask the user to input all three of the test scores for the student, one by one. 

# The program should then calculate the average test score (average is adding all three 
# test scores together then dividing by 3), and then print the student's letter grade 
# (as well as the average score as a number).


if __name__ == '__main__':
    import decimal
    import sys
    import statistics

    endings = ['st', 'nd', 'rd']
    scores = []
    for i in range(3):
        try:
            scores.append(decimal.Decimal(input(f"Please input your {i+1}{endings[i]} score: ")))
        except decimal.InvalidOperation:
            print("The score must be a valid Decimal!", file=sys.stderr)
            exit(1)

    avg = statistics.mean(scores)
    lgs = {decimal.Decimal(65): 'F',
           decimal.Decimal(66): 'D',
           decimal.Decimal(69): 'D+',
           decimal.Decimal(72): 'C-',
           decimal.Decimal(76): 'C',
           decimal.Decimal(79): 'C+',
           decimal.Decimal(82): 'B-',
           decimal.Decimal(86): 'B',
           decimal.Decimal(89): 'B+',
           decimal.Decimal(92): 'A-',
           decimal.Decimal(96): 'A',
           decimal.Decimal(100): 'A+'}
    for k in lgs:
        if avg < k:
            break
    print(f"Your average score is {avg}, which is a {lgs[k]}")
