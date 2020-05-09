import pandas as pd
import random


def PUF_generator() -> list:
    puf = []
    for y in range(256):
        temp = []
        for x in range(256):
            cell = random.randint(0, 1)
            temp.append(cell)
        puf.append(temp)
    return puf


def main():
    puf = PUF_generator()
    result = pd.DataFrame(puf)
    result.to_csv("PUF.csv", index=False)


if __name__ == '__main__':
    main()
