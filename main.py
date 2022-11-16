from Game import Game





game = Game()
game.assign_players()
game.deal_cards()

print("")


while not game.player_has_won():
    game.play_round()
    game.print_stats()

    if game.player_should_be_eliminated():
        game.eliminate_players()

    print()

winner = game.get_winner()
print(f"Player: {winner.name} has won the game!")

adsf="asdf"




