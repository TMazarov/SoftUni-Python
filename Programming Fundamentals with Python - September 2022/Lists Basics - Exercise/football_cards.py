team_a = list([f'A-{i}' for i in range(1, 12)])
team_b = list([f'B-{i}' for i in range(1, 12)])

players_kicked = input().split()

for player in players_kicked:

    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print("Game was terminated")
        break

else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
