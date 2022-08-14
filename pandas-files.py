import pandas as pd
import sqlite3
# df = pd.read_csv("driver-data.csv")
# df = pd.read_json("sample.json")
df = pd.read_excel("sample.xlsx")

# connectin = sqlite3.connect("sample.db")
# df = pd.read_sql_query("SELECT * FROM students",connectin)

print(df)