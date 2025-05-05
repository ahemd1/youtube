
import pandas as pd
import requests

file_id = "1_vMBXL4WlXWPqazLg-_9BbIPSymnEenY"
url = f"https://drive.google.com/uc?export=download&id={file_id}"
r = requests.get(url)
with open("Trending.csv", "wb") as f:
    f.write(r.content)



df = pd.read_csv("Trending.csv", encoding="utf-8", sep=",", engine="python", on_bad_lines='skip')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.to_csv("Trending_Cleaned.csv", index=False)
print("✅ Data cleaned")
print(df.head(5))
