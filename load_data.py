import pandas as pd
from faker import Faker
from sqlalchemy.types import Integer, String

# faker = Faker()
# profiles = [faker.profile() for i in range(1000)]
# df = pd.DataFrame(profiles)

df = pd.read_csv("data.csv", dtype={"keyword": str, "score": float})
df.reset_index(inplace=True, names=["id"])


def load_engine():
    from sqlalchemy import create_engine

    engine = create_engine("sqlite:///instance/db.sqlite3")

    return engine


def load_data():
    df.to_sql(
        "users",
        con=load_engine(),
        if_exists="replace",
        schema=None,
        index=False,
        dtype={
            "id": Integer(),
            "name": String(200),
        },
    )


def read_data():
    df = pd.read_sql("users", con=load_engine())
    print(df.head())


if __name__ == "__main__":
    load_data()
    read_data()
