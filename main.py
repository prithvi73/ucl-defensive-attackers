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
df = combined_df[combined_df["field_position"] == "Forward"].copy()
# print(df.to_string())

# calculating top attacking defenders
df["tackle_success_pct"] = (df["tackles_won"] / df["tackles"]) * 100
df["tackle_success_pct"] = df["tackle_success_pct"].fillna(0)
# print(df["tackle_success_pct"]) 

df["total_defensive_impact"] = (df["tackles_won"] + df["balls_recovered"])

# player must have attempted atleast 5 tackles or recovered 5 balls
qualified_attackers = df[(df["tackles"] >= 5) | (df["balls_recovered"] >= 5)]

top_defending_attackers = qualified_attackers.sort_values(by="total_defensive_impact", ascending=False)

print(top_defending_attackers[["player_name", "total_defensive_impact", "tackle_success_pct"]].head(10))






