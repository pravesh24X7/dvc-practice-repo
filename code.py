import pandas as pd
import os


def download_and_save(URL: str="https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv") -> None:
    os.makedirs("./data/", exist_ok=True)
    df = pd.read_csv(URL)

    df.to_csv("./data/titanic.csv", index=False)


if __name__ == "__main__":
    download_and_save()