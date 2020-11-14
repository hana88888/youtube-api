from apiclient.discovery import build
import json
from collections import OrderedDict
import pprint
import pandas as pd

# input your api key
api_key = ''

youtube = build('youtube', 'v3', developerKey=api_key)

search_res = youtube.search().list(
    part='snippet',
    q='ウェブマーケ',
    order='viewCount',
    type='video',
    maxResults=50
).execute()

res_list = search_res.get('items')

df = pd.DataFrame()

for i,item in enumerate(res_list):
    if i == 0:
        df = pd.io.json.json_normalize(item)
    else:
        df1 = pd.io.json.json_normalize(item)
        df = df.append(df1)
df.head(10)
