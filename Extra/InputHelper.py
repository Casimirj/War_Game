
def safe_get_number_input(text):
    while True:  # don't look at this, its bad code
        try:
            num_players = int(input(text))
            print(" ")
            return num_players
        except ValueError as ex:
            print("You need to enter a valid integer, try again")
