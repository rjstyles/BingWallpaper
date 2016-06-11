import re
import os
import time
import json
import requests
import urllib.request

time.sleep(5)
URL = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
try:
    image_data = json.loads(requests.get(URL).text)
    image_url = 'http://www.bing.com' + image_data['images'][0]['url']
    image_name = image_url[re.search("rb/", image_url).end():re.search('_EN', image_url).start()] + '.jpg'
    
    # add your own path to download the image
    file_path = ''+image_name
    if os.path.exists(file_path) is False:
        urllib.request.urlretrieve(image_url, filename=file_path)
        image_desc = image_data['images'][0]['copyright']
        # modify below line as per your file path
        command = 'gsettings set org.gnome.desktop.background picture-uri file://'+file_path
        os.system(command)
        notify = 'notify-send -u critical "Wallpaper for the Day updated!" "' + image_desc + '"'
        os.system(notify)
    else:
        notify = 'notify-send -u critical "Bing Wallpaper" "Wallpaper for the day has been updated!"'
        os.system(notify)
except:
    notify = 'notify-send -u critical "Bing Wallpaper" "Wallpaper can\'t be updated!"'
    os.system(notify)
