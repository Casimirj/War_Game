from Deck import Deck


class Player:

    def __init__(self):
        self.deck = Deck() #this is the Deck object we created in Deck.py
        self.name = "I never set a name for my player!"


    def assign_deck(self, deck):
        self.deck = deck

    def assign_name(self, name):
        self.name = name

    def play_card(self):
        if not self.deck.is_empty():
            card_to_play = self.deck.draw_card()

            return card_to_play
        else:
            return False

    def receive_card(self, card):
        self.deck.add_card(card)

    def get_number_of_cards(self):
        return self.deck.get_deck_size()


