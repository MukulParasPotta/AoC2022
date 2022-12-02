token_to_rps_map = {'A':'R','B':'P','C':'S','X':'R','Y':'P','Z':'S'}
rps_to_score_map = {'R':1,'P':2,'S':3}
rps_win_pairs = {('R','P'), ('P','S'), ('S','R')}

score = 0
with open('input.txt') as input:
    for line in input.readlines():
        opponent, player = line.split()
        opponent, player = token_to_rps_map[opponent], token_to_rps_map[player]
        score += rps_to_score_map[player]
        if opponent == player:
            score += 3
        if (opponent, player) in rps_win_pairs:
            score += 6
    print(score)