# Create a program in which the user creates 
# a specific FRC team and store the following variables:
#     Team Number (named team_number)
#     Team Name (named team_name)
#     Location (named location)
#     Rookie Year (named rookie_year)
#     Is Active (named is_active)
# Be sure to store each variable as the correct type!

if __name__ == '__main__':
    team_number = int(input("Team number (int): "))
    team_name = input("Team name (str): ")
    location = input("Location (str): ")
    rookie_year = int(input("Rookie year (int): "))
    is_active = bool(int(input("Is active (bool 0, 1): ")))

    for i in ['team_number', 'team_name', 'location', 'rookie_year', 'is_active']:
        print(f'{i}: {eval(i)}')
