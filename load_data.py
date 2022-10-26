import pandas as pd
from faker import Faker
from sqlalchemy.types import Integer, String

faker = Faker()
profiles = [faker.profile() for i in range(1000)]
df = pd.DataFrame(profiles)
df.reset_index(inplace=True, names=["id"])


def load_engine():
    from sqlalchemy import create_engine

    engine = create_engine("postgresql://bossruji:password@localhost/bossruji")

    return engine


def load_data():
    df.to_sql(
        "users",
        con=load_engine(),
        if_exists="replace",
        schema="public",
        index=False,
        dtype={
            "id": Integer(),
            "name": String(200),
        },
    )


def read_data():
    df = pd.read_sql("users", con=load_engine())

    return df


if __name__ == "__main__":
    load_data()
    result = read_data()
    print(result.head())
