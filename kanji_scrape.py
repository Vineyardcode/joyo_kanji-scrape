import requests
from bs4 import BeautifulSoup
import json

# Send a request to the Wikipedia page with the list of jōyō kanji
url = "https://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji"
response = requests.get(url)

# Parse the HTML content of the page using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table element containing the kanji list
table = soup.find("table", class_="wikitable")

# Find all the rows in the table except the header row
rows = table.find_all("tr")[1:]

# Create a list to store the kanji
kanji_list = []

# Loop through each row and extract the kanji character and additional info about it
for row in rows:
    columns = row.find_all("td")
    id = columns[0].text.strip()
    kanji = columns[1].text.strip()
    readings = [reading.strip() for reading in columns[8].text.split(",")]
    radicals = [reading.strip() for reading in columns[3].text.split(",")]
    strokes = [reading.strip() for reading in columns[4].text.split(",")]
    eng_meaning = [reading.strip() for reading in columns[7].text.split(",")]
    kanji_list.append({"id": id, "kanji": kanji, "readings": readings, "radicals": radicals, "strokes": strokes, "eng_meaning": eng_meaning})

# Write the kanji list to an existing JSON file
with open("jouyou_kanji.json", "w", encoding='utf-8') as f:
    json.dump(kanji_list, f, ensure_ascii=False, indent=4)