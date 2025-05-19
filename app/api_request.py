import requests
import json

class RequestAPI():
    def __init__(self, tag):
        self.tag = tag

    def retrive_data(self):
        url = f"https://api.waifu.pics/sfw/{self.tag}"
        r = requests.get(url)
        data = r.json()
        url_data = data['url']
        return url_data
