import pandas as pd


def PUF_reader(x_col: str, y_row: str, type: str) -> str:
    val = ""
    col = int(x_col, base=16)
    row = int(y_row, base=16)
    puf = pd.read_csv("PUF.csv")
    if col + 16 > 255:
        if row == 255:
            next_row = 0
        else:
            next_row = row + 1
        for i in range(col, 256):
            current_value = str(puf[str(i)][row])
            val = val + current_value
            print("Current cell is :" + hex(i) + ", " + hex(row) + " and the value is: " + current_value)
        for i in range(0, col + 16 - 256):
            current_value = str(puf[str(i)][next_row])
            val = val + current_value
            print("Current cell is :" + hex(i) + ", " + hex(next_row) + " and the value is: " + current_value)
    else:
        for i in range(16):
            current_value = str(puf[str(col+i)][row])
            val = val + current_value
            print("Current cell is :" + hex(col+i) + ", " + hex(row) + " and the value is: " + current_value)
    if type == "challenge":
        print("The Challenge is: " + hex(int(val, base=2)) + "\n")
    elif type == "response":
        print("The response is: " + hex(int(val, base=2)) + "\n")
    return val


# PUF_reader(x_col="22", y_row="1f")
