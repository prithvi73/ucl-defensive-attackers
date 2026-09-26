import pandas as pd
import matplotlib.pyplot as plt

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

# sorting the top attacking defenders
top_defending_attackers = qualified_attackers.sort_values(by="total_defensive_impact", ascending=False)

print(top_defending_attackers[["player_name", "total_defensive_impact", "tackle_success_pct"]].head(10))


# visualizing the data

fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Graph 1 : Scatter Plot
ax1.scatter(df["tackles"], df["tackles_won"], alpha=0.7, color="red")

# Reference Line
max_tackles = df["tackles"].max()
ax1.plot([0, max_tackles], [0, max_tackles], color="gray", linestyle="--", label="100% Success Rate")

ax1.set_xlabel("Tackles Attempted")
ax1.set_ylabel("Tackles Won")
ax1.set_title("UCL Forwards: Tackles Attempted Vs Tackles Won")
ax1.legend()


# Graph 2 : Bar Chart
top_10 = top_defending_attackers.head(10)
ax2.barh(top_10["player_name"], top_10["total_defensive_impact"], color="blue")
ax2.invert_yaxis()

ax2.set_xlabel("Total Defensive Impact")
ax2.set_title("Top 10 Defensive Forwards in UCL 25/26")

plt.tight_layout()
plt.show()