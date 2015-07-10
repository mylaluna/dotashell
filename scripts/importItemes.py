__author__ = 'elune'
import json
import psycopg2
from urllib.request import urlopen

getItemsURL = "https://api.steampowered.com/IEconDOTA2_570/GetGameItems/V001/?key=5469BD52850E23FF4F0AFEBD5C0C67B3&language=en_us"
response = urlopen(getItemsURL)
contents = response.read()
text_Origin = contents.decode('utf8')
text = json.loads(text_Origin)

insertitemSQL = "INSERT INTO items_item (id, name, cost, secret_shop, side_shop, recipe, localized_name) VALUES (%s, %s, %s, %s, %s, %s, %s);"
conn = psycopg2.connect('dbname=elune user=elune password=x3j11')
cur = conn.cursor()


for item in sorted(text['result']['items'], key=lambda k: k['id']):
    cur.execute(insertitemSQL,
                (item['id'],
                 item['name'],
                 item['cost'],
                 item['secret_shop'],
                 item['side_shop'],
                 item['recipe'],
                 item['localized_name']))
    print(item['id'])
    print(item['name'])
    print(item['localized_name'])

conn.commit()

cur.close()
conn.close()

print('Successfully Insert and Commit to Database!')
