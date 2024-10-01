#!/usr/bin/python3
"""Prime Game Interview"""


def isWinner(x, nums):
    """Find winner"""
    winner_counter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        round_winner = isRoundWinner(nums[i], x)
        if round_winner is not None:
            winner_counter[round_winner] += 1

    if winner_counter['Maria'] > winner_counter['Ben']:
        return 'Maria'
    if winner_counter['Ben'] > winner_counter['Maria']:
        return 'Ben'
    return None


def isRoundWinner(n, x):
    """find round winner"""
    game_list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        current_player = players[i % 2]
        selected_idxs = []
        prime = -1
        for idx, num in enumerate(game_list):
            if prime != -1:
                if num % prime == 0:
                    selected_idxs.append(idx)
            else:
                if isPrime(num):
                    selected_idxs.append(idx)
                    prime = num
        if prime == -1:
            if current_player == players[0]:
                return players[1]
            return players[0]

        for idx, val in enumerate(selected_idxs):
            del game_list[val - idx]
    return None


def isPrime(n):
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return "Not prime"
        return True
