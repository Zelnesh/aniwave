import requests
import json
import plotly.express as px
import plotly

class AnimeRate:

    url = 'https://api.jikan.moe/v4/top/anime'
    

    def get_data(self):
        r = requests.get(self.url)
        stat_code = r.status_code
        rsp_data = r.json()
        clear_data = json.dumps(rsp_data, indent=4)
        data_json = json.loads(clear_data)


        titles = []
        scores = []
        hover_texts = []

        for i in range(0, 20):
            trailer_url = f'<a href="{data_json["data"][i]["trailer"]["url"]}">{data_json["data"][i]["titles"][2]["title"]}</a>'
            titles.append(trailer_url)
            scores.append(data_json["data"][i]["score"])
            hover_text = f'{data_json["data"][i]["synopsis"]}'
            hover_texts.append(hover_text)
    
    



        title = "Top 20 Anime"
        labels = {'x' : 'Title', 'y' : 'Score'}
        fig = px.bar(x=titles, y=scores, title=title, labels=labels, hover_name=hover_texts)
        fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
        return plotly.offline.plot(fig, filename='templates/rate.html', auto_open=False)


