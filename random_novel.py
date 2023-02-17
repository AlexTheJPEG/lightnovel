import pickle
from pathlib import Path

import requests
from bs4 import BeautifulSoup

base_url = "https://www.novelupdates.com/random-novel/"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/90.0.4430.85 Safari/537.36"
    )
}
page = 1
title_set = set()

if Path("title_pickle").is_file():
    with open("title_pickle", "rb") as load_file:
        load_dict = pickle.load(load_file)
        page = load_dict["page"]
        title_set = load_dict["title_set"]

while len(title_set) < 10_000:
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title =  soup.select("body > div.l-canvas.col_contside > div.l-main > div > div > div.l-content > div > div > div:nth-child(4) > a")[0].text
        title_set.add(title)
        print(f"Added {title}")
    except KeyboardInterrupt:
        break

dump_dict = {"page": page, "title_set": title_set}
with open("title_pickle", "wb") as dump_file:
    pickled_dict = pickle.dump(dump_dict, dump_file)