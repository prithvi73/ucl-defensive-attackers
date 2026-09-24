import pandas as pd

# reading the data
defense_df = pd.read_csv("Data/defending_data.csv")
players_df = pd.read_csv("Data/players_data.csv")

# making a df of the columns we need from player data
player_subset = players_df[["id_player", "player_name", "field_position"]]

# combining the data
combined_df = pd.merge(defense_df, player_subset, on='id_player')
# print(combined_df.head())

# # getting the players who are forwards for our actual dataframe
df = combined_df[combined_df["field_position"] == "Forward"]
print(df.head())