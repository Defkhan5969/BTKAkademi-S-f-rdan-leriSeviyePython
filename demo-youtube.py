import pandas as pd

df = pd.read_csv("youtube-ing.csv")

result = df

result = df.head(10)
result = df[100:].head()

result = len(df.columns)
result = df.columns
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis=1)
result = df
print(result)