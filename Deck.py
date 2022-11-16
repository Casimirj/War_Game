import random

from Extra import GameData
from Card import Card


class Deck:
    def __init__(self, input_cards=None):
        """
        Initializes the Deck Object

        :param input_cards: (Optional) You may specify the cards this deck starts with
        """

        if input_cards is None:
            self.cards_in_deck = []

        # Player deck, starts with SOME cards (input into function)
        else:
            self.cards_in_deck = input_cards

    def get_game_deck(self):
        """
        Creates a deck with ALL the Cards
        """
        # building the deck starting with an empty list of cards
        self.cards_in_deck = []

        # loops through all the suites in the deck
        for suite in GameData.suites:
            # loops through all card numbers (ranks) for a suite, and adds it to the deck
            for rank in GameData.ranks:
                new_card = Card(rank, suite)
                self.cards_in_deck.append(new_card)


    def shuffle(self, num_times_to_shuffle=5):
        """
        This is complicated, don't worry about it
        Shuffles the deck, resets "cards_in_deck" to the shuffled deck

        :param num_times_to_shuffle: Amount of passes to make randomizing the cards
                                    (Defaults to 5 shuffles)
        """

        for shuffle in range(0, num_times_to_shuffle):
            shuffled_deck = []

            deck_size = len(self.cards_in_deck)
            cards_left = deck_size
            for i in range(0, deck_size):
                random_card_position = random.randint(0, cards_left - 1)
                # using "pop" removes the card from the list (so we don't add the same card 2 times)
                random_card = self.cards_in_deck.pop(random_card_position)
    # 5: "Five",      # You could probably generate the names for numbers 2-10
    # 6: "Six",       # But because there is some nuance I wanted to define it simply
    # 7: "Seven",     # ex of nuance: 1 doesn't exist, cards above 10 have weird names, ect
    # 8: "Eight",
    # 9: "Nine",
    # 10: "Ten",
    # 11: "Jack",
    # 12: "Queen",
    # 13: "King",
    # 14: "Ace",
    # 15: "Joker"
                shuffled_deck.append(random_card)
                cards_left = cards_left - 1

            self.cards_in_deck = shuffled_deck

    def is_empty(self):
        """
        Checks if a deck is empty
        :return: "True" if deck is empty, "False" if deck has cards
        """
        num_cards_in_deck = len(self.cards_in_deck)
        return num_cards_in_deck == 0

    def draw_card(self):
        """
        Gets the top card from the deck

        :return: The first element in the list of cards, False if no cards exist in the deck
        """
        if not self.is_empty():
            card_to_play = self.cards_in_deck.pop(0)  # Pop removes card from list
            return card_to_play
        else:
            return False

    def add_card(self, card):
        """
        Adds a card to a deck

        :param card: Card to be added to the deck
        """
        self.cards_in_deck.append(card)

    def print_deck(self):
        """
        Prints the contents of a deck to the console
        """
        for card in self.cards_in_deck:
            print(card.get_nice_name())

    def get_deck_size(self):
        return len(self.cards_in_deck)
