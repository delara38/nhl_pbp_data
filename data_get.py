import pandas as pd
import hockey_scraper as hockey
import os

for i in range(1271):
    id = 2017020001 + i
    if not os.path.exists("games/{}.csv".format(id)):
        try:
            game = hockey.scrape_games([id], False,data_format="Pandas")['pbp']
            game.to_csv('games/{}.csv'.format(id))
        except:
            print(id)
            pass

