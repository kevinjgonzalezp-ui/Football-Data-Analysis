
def home_advantage(df):
    home_wins = len(df[df["FTResult"] == "H"])
    away_wins = len(df[df["FTResult"] == "A"])
    draws = len(df[df["FTResult"] == "D"])

    total = len(df)

    return {
        "Home %": home_wins/total*100,
        "Away %": away_wins/total*100,
        "Draw %": draws/total*100
    }