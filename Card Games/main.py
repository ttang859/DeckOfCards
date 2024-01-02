import os
from blackjack import *
from card_interface import *

def parse_file(file):
    player_list = []
    file_data = file.readlines()
    for line in file_data:
        colon = line.find(':')
        pid = int(line[:colon])
        bal = int(line[colon+1:])
        player_list.append(Player(pid,[],0,bal))
    return player_list

while True:
    load_game = input('Load previous game, Y/N?')
    if load_game.upper() == 'Y':
        save_file = open('Card Games/game_save.txt')
        players = parse_file(save_file)
        break
    elif load_game.upper() == 'N':
        players = init()
        dealer = Player(0, [],0,0) #dealer id is 0 and is at end of list of players
        players.append(dealer)
        break

play_bj(players)

save_file = open('Card Games/game_save.txt', 'w')
for player in players:
    save_file.write(str(player.get_pid()) + ':' + str(player.get_bal()) + ' \n')
save_file.close()

exit()