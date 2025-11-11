# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster = ["Evans", "High", "Brown", "Dixon", "Young", "Denis", "Davis", "Trimble", "Wilson", "Powell"],
player = {"Last Name": roster,
          "First Name": ["Kyan", "Zayden", "James", "Derek", "Jaydon", "Isaiah", "Elijah", "Seth", "Caleb", "Jonathan"],
          "Height": [62, 61, 61, 65, 64, 64, 63, 63, 61, 66],
          "Weight": [175, 230, 240, 200, 200, 180, 205, 200, 215, 190]}
data = pd.DataFrame(player)
print(data) 


