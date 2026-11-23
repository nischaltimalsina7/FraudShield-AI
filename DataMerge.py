import pandas as pd

transactions = pd.read_csv("Datasets/transactions_data.csv")
cards = pd.read_csv("Datasets/cards_data.csv")
users = pd.read_csv("Datasets/users_data.csv")

merged = transactions.merge(
    cards, left_on="card_id", right_on="id", how = "left", suffixes=("", "_card")
)
merged = merged.merge(
    users, left_on="client_id", right_on="id", how="left", suffixes=("", "_users")
)
merged.to_csv("fraud_dataset_merged.csv", index=False)