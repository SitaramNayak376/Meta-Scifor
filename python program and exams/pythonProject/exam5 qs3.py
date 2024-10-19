import random

def random_quote():
    quotes =[
        "The gratest glory in living lies not in never falling :- nelson mandela",
        "The way to get started is to quit talking and begin doing :- walt disney",
        "Your time is limited, so don't waste your time:- steve jobs"

    ]
    return random.choice(quotes)
print('Random Quote:', random_quote())