__author__ = 'elune'
import json
import psycopg2
from urllib.request import urlopen

getHeroesURL = "https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key=5469BD52850E23FF4F0AFEBD5C0C67B3&language=en_us"
response = urlopen(getHeroesURL)
contents = response.read()
text_Origin = contents.decode('utf8')
text = json.loads(text_Origin)

insertHeroSQL = "INSERT INTO heroes_hero (id, name, localized_name) VALUES (%s, %s, %s);"
conn = psycopg2.connect('dbname=elune user=elune password=x3j11')
cur = conn.cursor()


for hero in sorted(text['result']['heroes'], key=lambda k: k['id']):
    cur.execute(insertHeroSQL, (hero['id'], hero['name'], hero['localized_name']))
    print(hero['id'])
    print(hero['name'])
    print(hero['localized_name'])

conn.commit()

cur.close()
conn.close()

print('Successfully Insert and Commit to Database!')
