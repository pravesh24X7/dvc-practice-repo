import pandas as pd
import os


def download_and_save(URL: str="https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv") -> None:
    os.makedirs("./data/", exist_ok=True)
    df = pd.read_csv(URL)

    df.to_csv("./data/titanic.csv", index=False)


def preprocess_data(filepath: str="", save_to: str="unnamed.csv") -> None:

    # load the file
    df = pd.read_csv(filepath)
    
    # removing the ID column
    df.drop(columns=["PassengerId"], inplace=True)

    # change the `Sex` categorical column to integer column
    df["Sex"] = df["Sex"].apply(
        lambda x: 1 if x == "male" else 0
    )
    
    df.to_csv(f"./{save_to}")


if __name__ == "__main__":
    download_and_save()

    preprocess_data(filepath="data/titanic.csv", save_to="data/updated_titanic_dataset001.csv")