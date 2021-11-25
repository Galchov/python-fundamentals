team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards_input = input().split()

is_terminated = False

for card in cards_input:
    card_info = card.split('-')

    team_name = card_info[0]
    player_number = int(card_info[1])

    if team_name == "A" and player_number in team_a:
        team_a.remove(player_number)
    elif team_name == "B" and player_number in team_b:
        team_b.remove(player_number)

    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if is_terminated:
    print("Game was terminated")


# team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# cards = input().split()
#
# referee = ""
# game_terminated = False
#
# for card in cards:
#     referee = card.split("-")
#
#     if referee[0] == "A":
#         if int(referee[1]) in team_a:
#             team_a.remove(int(referee[1]))
#     elif referee[0] == "B":
#         if int(referee[1]) in team_b:
#             team_b.remove(int(referee[1]))
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         game_terminated = True
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
#
# if game_terminated:
#     print("Game was terminated")