import requests
import pandas as pd
from bs4 import BeautifulSoup

responce = requests.get('https://www.espncricinfo.com/records/tournament/batting-most-runs-career/indian-premier-league-2023-15129')
soup = BeautifulSoup(responce.content, 'html.parser')

names = soup.find_all('span',class_='ds-text-tight-s ds-font-regular ds-text-typo-primary hover:ds-text-typo-primary-hover ds-block')
Name = []
for i in names:
    d = i.get_text()
    Name.append(d)

runs = soup.find_all('td', class_='ds-bg-ui-fill-translucent')
Runs = []
for i in runs:
    d = i.get_text()
    Runs.append(d)

SR = soup.find_all('td', class_='ds-min-w-max ds-text-right')
BattingSR = []
for i in SR:
    d = i.get_text()
    BattingSR.append(d)

avg = soup.find_all('span', class_="ds-min-w-max ds-text-right")
BowlingAVG = []
for i in avg:
    d = i.get_text()
    BowlingAVG.append(d)

df = pd.DataFrame()
df['Name'] = Name
df['Runs'] = Runs
df['BattingSR'] = BattingSR
df['BowlingAVG'] = BowlingAVG

df.to_csv(IPL_Data.csv)
