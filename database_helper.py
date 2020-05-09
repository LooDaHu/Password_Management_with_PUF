import pandas as pd


def enrollment(x_col: str, y_row: str, challenge: str):
    database = pd.read_csv("database.csv")
    y = int(y_row, base=16)
    challenge = hex(int(challenge, base=2))
    database[x_col][y] = challenge
    database.to_csv('database.csv', index=False)


def authentication(x_col: str, y_row: str, response: str) -> bool:
    database = pd.read_csv("database.csv")
    y = int(y_row, base=16)
    response = hex(int(response, base=2))
    challenge = database[x_col][y]
    print("Saved challenge in database is:" + challenge)
    if challenge == response:
        return True
    else:
        return False
