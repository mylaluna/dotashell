__author__ = 'elune'
import json
import urllib
from urllib.request import urlopen

getHeroesURL = "https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key=5469BD52850E23FF4F0AFEBD5C0C67B3&language=en_us"
response = urlopen(getHeroesURL)
contents = response.read()
text_Origin = contents.decode('utf8')
text = json.loads(text_Origin)

getHeroImagesURL = "http://cdn.dota2.com/apps/dota2/images/heroes/"
image_suffix = ('_sb.png', '_lg.png', '_full.png', '_vert.jpg')

for hero in sorted(text['result']['heroes'], key=lambda k: k['id']):
    for suffix in image_suffix:
        CurrentImgURL = getHeroImagesURL + hero['name'][14:] + suffix
        urllib.urlretrieve(CurrentImgURL, './' + hero['name'][14:] + suffix)
        # image = urllib.URLopener()
        # image.retrieve()

getItemsURL = "https://api.steampowered.com/IEconDOTA2_570/GetGameItems/V001/?key=5469BD52850E23FF4F0AFEBD5C0C67B3&language=en_us"
response = urlopen(getItemsURL)
contents = response.read()
text_Origin = contents.decode('utf8')
text = json.loads(text_Origin)


getItemImagesURL = "http://cdn.dota2.com/apps/dota2/images/items/"

for item in sorted(text['result']['items'], key=lambda k: k['id']):
    CurrentImgURL = getItemImagesURL + item['name'][5:] + '_lg.png'
    urllib.urlretrieve(CurrentImgURL, './' + item['name'][5:] + '_lg.png')



