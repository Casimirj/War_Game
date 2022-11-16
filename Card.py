from Extra import GameData


class Card:
    def __init__(self, rank, suite):
        """
        Initializes the Card Object
        :param rank: The "Number" of a card
        :param suite: Figure it out you dumb fuck

        Face cards are ranked with a number above 10
            ex: Jack == 11, Queen == 12, etc
        """
        self.rank = rank
        self.suite = suite

    def get_nice_name(self):
        """
        Gets the human name for a card based on rank/suite

        "Two of Hearts", "Queen of Spades"
        :return: (String) the fancy name for the card
        """
        return f"{GameData.ranks[self.rank]} of {self.suite}"



    def beats(self, opposing_card):
        """
        Checks if card beats another card

        :param opposing_card: The card to be comparing against
        :return: True if card beats opposing card, False if card loses
        """
        return self.rank > opposing_card.rank


    def ties(self, opposing_card):
        """
        Checks if card ties to another card

        :param opposing_card: The card to be comparing against
        :return: True if card ties opposing card, False if card does not tie
        """
        return self.rank == opposing_card.rank





