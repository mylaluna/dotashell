__author__ = 'elune'
import json
import urllib
from urllib.request import urlopen

getHeroesURL = "https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key=5469BD52850E23FF4F0AFEBD5C0C67B3&language=en_us"
response = urlopen(getHeroesURL)
contents = response.read()
text_Origin = contents.decode('utf8')
text = json.loads(text_Origin)
error_list = []

getHeroImagesURL = "http://cdn.dota2.com/apps/dota2/images/heroes/"
image_suffix = ('_sb.png', '_lg.png', '_full.png', '_vert.jpg')

print('Start Fetching Hero Images!')

for hero in sorted(text['result']['heroes'], key=lambda k: k['id']):
    for suffix in image_suffix:
        print('Fetching Hero: ', hero['name'][14:] + suffix)
        try:
            CurrentImgURL = getHeroImagesURL + hero['name'][14:] + suffix
            urllib.request.urlretrieve(CurrentImgURL, './HeroImages/' + hero['name'][14:] + suffix)
        except urllib.error.HTTPError as err:
            if 404 == err.code:
                error_list.append(CurrentImgURL)
                continue
            else:
                raise
        # image = urllib.URLopener()
        # image.retrieve()

print('Complete Fetching Hero Images')

print('Start Fetching Item Images!')

getItemsURL = "https://api.steampowered.com/IEconDOTA2_570/GetGameItems/V001/?key=5469BD52850E23FF4F0AFEBD5C0C67B3&language=en_us"
response = urlopen(getItemsURL)
contents = response.read()
text_Origin = contents.decode('utf8')
text = json.loads(text_Origin)


getItemImagesURL = "http://cdn.dota2.com/apps/dota2/images/items/"

for item in sorted(text['result']['items'], key=lambda k: k['id']):
    print('Fetching item: ', item['name'][5:] + '_lg.png')
    try:
        CurrentImgURL = getItemImagesURL + item['name'][5:] + '_lg.png'
        urllib.request.urlretrieve(CurrentImgURL, './ItemImages/' + item['name'][5:] + '_lg.png')
    except urllib.error.HTTPError as err:
        if 404 == err.code:
            error_list.append(CurrentImgURL)
            continue
        else:
            raise

print('Complete Fetching ALL Images!')
print('Following URLs Returns Error, Please Check: ', error_list)
