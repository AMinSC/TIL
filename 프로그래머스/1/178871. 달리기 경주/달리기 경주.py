def solution(players, callings):
    rank = {player: int(rank) for rank, player in enumerate(players)}
    
    for call in callings:
        i = rank[call]
        
        players[i - 1], players[i] = players[i], players[i - 1]
        
        rank[call] -= 1
        rank[players[i]] += 1

    return players