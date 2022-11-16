
from Deck import Deck
from Player import Player
from Card import Card

import Extra.InputHelper as InputHelper


class Game:


    def __init__(self):
        self.players = []
        self.round_number = 0


    def assign_players(self):
        all_players = []

        num_players = InputHelper.safe_get_number_input("Please enter the number of players to play with: ")

        for i in range(1, num_players+1):
            player_name = input(f"Please enter a name for Player {i}: ")

            new_player = Player()
            new_player.assign_name(player_name)

            all_players.append(new_player)

        self.players = all_players

    def deal_cards(self):
        game_deck = Deck()
        game_deck.get_game_deck()
        game_deck.shuffle(10)

        while not game_deck.is_empty(): # while deck is not empty*
            for player in self.players: # players draw 1 at a time
                dealt_card = game_deck.draw_card()
                player.receive_card(dealt_card)



    def player_has_won(self):
        return len(self.players) == 1


    def get_winner(self):
        return self.players[0]

    def player_should_be_eliminated(self):
        for player in self.players:
            if player.deck.is_empty():
                return True
        return False


    def eliminate_players(self):
        while self.player_should_be_eliminated():
            for player in self.players:
                if player.deck.is_empty():
                    print(f"{player.name} has been eliminated!")
                    self.players.remove(player)

    def play_round(self):
        self.round_number += 1
        print(f"Round {self.round_number}!")

        highest_play = None
        highest_player = None
        tie_for_highest = False
        tied_player = None

        cards_in_round = []  # These cards get added to the winners deck after the round

        # Determine who won the round
        for player in self.players:
            played_card = player.play_card()  # this removes the card from the players deck
            cards_in_round.append(played_card)

            played_card_nice_name = played_card.get_nice_name()
            print(f"{player.name} plays the card: {played_card_nice_name}")

            if highest_play is None:        # first time through loop,
                highest_play = played_card  # we have nothing to compare against
                highest_player = player     # so we just say the 1st player is the "highest" lmao
            else:
                if played_card.beats(highest_play):
                    highest_play = played_card
                    highest_player = player
                    tie_for_highest = False
                    tied_player = None
                elif played_card.ties(highest_play):
                    tie_for_highest = True # you're probably asking "what if multiple players tie?"
                    tied_player = player # and the answer is not to think things like that

        # screw it!
        # player 1 always wins in case of a tie!

        # if tie_for_highest:
            # extra_round_cards = self.play_tie_round(highest_player, tied_player)

        print(f"{highest_player.name} wins the round")

        # Add the spoils of victory to the winners deck
        for card in cards_in_round:
            highest_player.receive_card(card)



    def print_stats(self):
        for player in self.players:
            print(f"{player.name} has {len(player.deck.cards_in_deck)} cards")





