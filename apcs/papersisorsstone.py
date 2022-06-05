ROCK = 0
SCISSORS = 2
PAPER = 5
WINNING_PLAY_VS = {ROCK: PAPER,
                   PAPER: SCISSORS,
                   SCISSORS: ROCK}

F = int(input())
N = int(input())
sis = [int(x) for x in input().split()]