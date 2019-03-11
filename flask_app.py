from flask import Flask, render_template, json, request
from flask import Markup
import requests

app=Flask(__name__)
app.config["DEBUG"] = False


@app.route("/")
def chart():
    r = requests.get('https://api.airtable.com/v0/apppd5kwBUmLz7ejM/Imported%20table?api_key=key4aplWFBl8A764P&sortField=_createdTime&sortDirection=desc')
    dict1 = r.json()
    dict2 = {}
    dataset = []
    name_list = []
    point_list = []
    for i in dict1['records']:
         dict2 = i['fields']
         dataset.append(dict2)
    for item in dataset:
        name_list.append(item.get('name'))
        point_list.append(item.get('membership_level'))
    return render_template('chart.html', entries = zip(name_list, membership_level_list))

if __name__ == '__main__':
   app.run(debug = True)
