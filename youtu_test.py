#api_key = "AIzaSyDxIHQ43Znxm10xz8OytsHFU8eg_-AhyLM"
from apiclient.discovery import build
import json
import codecs
import pandas as pd
from apiclient.errors import HttpError
import csv
import re
import pprint
import numpy as np


lislislis=0

API_list = ['AIzaSyBQkqrNbLGKIgAmzxPK-k02nCd79L0Sl6A']
movie_id = ['UCDh2bWI5EDu7PavqwICkVpA','UCeLzT-7b2PBcunJplmWtoDg','UCYTz3uIgwVY3ZU-IQJS8r3A','UCwePpiw1ocZRSNSkpKvVISw','UC0Owc36U9lOyi9Gx9Ic-4qg','UC2kyQhzGOB-JPgcQX9OMgEw','UCRvpMpzAXBRKJQuk-8-Sdvg','UCW8WKciBixmaqaGqrlTITRQ','UCXp7sNC0F_qkjickvlYkg-Q','UCtzCQnCT9E4o6U3mHHSHbQQ','UC_BlXOQe5OcRC7o0GX8kp8A','UCFsWaTQ7kT76jNNGeGIKNSA','UC_WOBIopwUih0rytRnr_1Ag','UC3EhsuKdEkI99TWZwZgWutg','UCmqrvfLMws-GLGHQcB5dasg','UChXm-xAYPfygrbyLo2yCASQ','UCV4EoK6BVNl7wxuxpUvvSWA','UCzUNASdzI4PV5SlqtYwAkKQ','UCL-2thbJ7grC9fmGF4OLuTg','UC2hc-00y-MSR6eYA4eQ4tjQ','UCvPPBoTOor5gm8zSlE2tg4w','UC--A2dwZW7-M2kID0N6_lfA']

for movmov in movie_id:
    API_KEY = API_list[0]
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    CHANNEL_ID = 'CHANNEL_ID'
    channels = []  # チャンネル情報を格納する配列
    searches = []  # videoidを格納する配列
    videos = []  # 各動画情報を格納する配列
    nextPagetoken = None
    nextpagetoken = None
    count = 0
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=API_KEY
    )

    channel_response = youtube.channels().list(
        part='snippet,statistics',
        id=movmov
    ).execute()
    '''
    for channel_result in channel_response.get("items", []):
        if channel_result["kind"] == "youtube#channel":
            channels.append([channel_result["snippet"]["title"], channel_result["statistics"]["subscriberCount"],
                            channel_result["statistics"]["videoCount"], channel_result["snippet"]["publishedAt"]])
    '''

    while True:
        if nextPagetoken != None:
            nextpagetoken = nextPagetoken

        search_response = youtube.search().list(
            part="snippet",
            channelId=movmov,
            maxResults=50,
            order="date",  # 日付順にソート
            pageToken=nextpagetoken  # 再帰的に指定
        ).execute()

        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                searches.append(search_result["id"]["videoId"])#ここでSearchリストに追加

        if count == 2:#ここで取得数の制御
            break

        try:
            nextPagetoken = search_response["nextPageToken"]#ここで再帰して、制限解除？
            count += 1

        except:
            break

    for result in searches:
        video_response = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            id=result
        ).execute()

        for video_result in video_response.get("items", []):
            if video_result["kind"] == "youtube#video":
                videos.append([video_result["snippet"]["title"], video_result["statistics"]["viewCount"]
                            , video_result["snippet"]["publishedAt"], video_result["contentDetails"]["duration"]])

    videos_report = pd.DataFrame(videos,
                                columns=['title', 'viewCount', 'publishedAt', 'duration'])
    name_list=['miko','pato','sha','mea','haneru','soya','ran','izu','kuku','mimi','hasi','hira','sesimaru','yuge','kanon','anko','wat','meto','camomi','rin','anna','chris']
    videos_report.to_csv("videos_report_"+name_list[lislislis]+".csv", index=None, encoding='utf_8_sig')
    lislislis = lislislis+1
#channel_report = pd.DataFrame(channels, columns=['title', 'subscriberCount', 'videoCount', 'publishedAt'])
#channel_report.to_csv("channels_report.csv", index=None)

video_file_list = ['videos_report_pato.csv','videos_report_sha.csv','videos_report_mea.csv','videos_report_miko.csv',
'videos_report_yuge.csv','videos_report_meto.csv','videos_report_kanon.csv','videos_report_anko.csv','videos_report_wat.csv',
'videos_report_camo.csv','videos_report_rin.csv','videos_report_anna.csv','videos_report_chris.csv','videos_report_haneru.csv',
'videos_report_soya.csv','videos_report_ran.csv','videos_report_izu.csv','videos_report_kuku.csv','videos_report_mimi.csv',
'videos_report_hasi.csv','videos_report_hira.csv','videos_report_sesimaru.csv' ]

person_list = ['pato','sha','mea','miko','yuge','meto','kanon','ank','wat','camo','rin','anna','chris','haneru','soya','ran','izu','kuku','mimi','hasi','hira','sesimaru']
count = 0

for video in video_file_list:
    if video == 'videos_report_hira.csv' or video == 'videos_report_sesimaru.csv' :
        person = person_list[count]
        with open(video, encoding="utf_8") as f:
            t = 0
            graph = []
            reader = csv.reader(f)
            l = [row for row in reader]
            regex = re.compile('\d+')
            for hoge in range(1, 40):
                # print(l[t][2])
                t += 1
                date_match = regex.findall(l[t][2])
                #print(date_match)
                dur_match = regex.findall(l[t][3])
                #print(dur_match)
                if 'H' in l[t][3] and 'M' in l[t][3]:  # 1時間以上の場合,秒数が０の場合が存在するので
                    ans = int(date_match[3]) + 9 - int(dur_match[0])
                    if int(date_match[4]) <= int(dur_match[1]):  # 分数が長い場合
                        if ans - 1 < 25:  # ここで１２じ以降の条件分岐ぺこ
                            graph.append(ans - 1)
                            #print("nyan")
                            #print(ans - 1)
                        else:
                            graph.append(ans - 1 - 24)
                            #print(ans - 1 - 24)


                    else:  # 分数引かない
                        if ans < 25:  # ここで１２じ以降の条件分岐ぺこ
                            graph.append(ans)
                            #print(ans)
                        else:
                            graph.append(ans - 24)
                            #print(ans - 24)

                        #print("nyan2")
                elif 'H' in l[t][3] and 'M' not in l[t][3]:  # 分数が存在しない場合
                    ans = int(date_match[3]) + 9 - int(dur_match[0])
                    if ans < 25:  # ここで１２じ以降の条件分岐ぺこ
                        graph.append(ans)
                        #print("nyan3")
                    else:
                        graph.append(ans - 24)
                        #print("nyan24")
                else:  # こっちは1時間以下の場合
                    ans = int(date_match[3]) + 9
                    if int(date_match[4]) < int(dur_match[0]):  # 分数が長い場合,これここにも条件分岐必要Dur
                        if ans - 1 < 25:
                            graph.append(ans - 1)
                            #print("nyan4")
                        else:
                            graph.append(ans - 1 - 24)
                            #print("nyan4")
                    else:
                        if ans < 25:  # ここで日付またぐ処理
                            graph.append(ans)
                        else:
                            graph.append(ans - 24)

        # 最適化するとしたらここか
        x1 = graph.count(1)
        x2 = graph.count(2)
        x3 = graph.count(3)
        x4 = graph.count(4)
        x5 = graph.count(5)
        x6 = graph.count(6)
        x7 = graph.count(7)
        x8 = graph.count(8)
        x9 = graph.count(9)
        x10 = graph.count(10)
        x11 = graph.count(11)
        x12 = graph.count(12)
        x13 = graph.count(13)
        x14 = graph.count(14)
        x15 = graph.count(15)
        x16 = graph.count(16)
        x17 = graph.count(17)
        x18 = graph.count(18)
        x19 = graph.count(19)
        x20 = graph.count(20)
        x21 = graph.count(21)
        x22 = graph.count(22)
        x23 = graph.count(23)
        x24 = graph.count(24)

        graph_ans = [x24, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, 
        x17, x18, x19, x20, x21, x22, x23,]

        print('{0}={1}'.format(person,graph_ans))
        count = count + 1
    else:
        person = person_list[count]
        with open(video, encoding="utf_8") as f:
            t = 0
            graph = []
            reader = csv.reader(f)
            l = [row for row in reader]
            regex = re.compile('\d+')
            for hoge in range(1, 100):
                # print(l[t][2])
                t += 1
                date_match = regex.findall(l[t][2])
                #print(date_match)
                dur_match = regex.findall(l[t][3])
                #print(dur_match)
                if 'H' in l[t][3] and 'M' in l[t][3]:  # 1時間以上の場合,秒数が０の場合が存在するので
                    ans = int(date_match[3]) + 9 - int(dur_match[0])
                    if int(date_match[4]) <= int(dur_match[1]):  # 分数が長い場合
                        if ans - 1 < 25:  # ここで１２じ以降の条件分岐ぺこ
                            graph.append(ans - 1)
                            #print("nyan")
                            #print(ans - 1)
                        else:
                            graph.append(ans - 1 - 24)
                            #print(ans - 1 - 24)


                    else:  # 分数引かない
                        if ans < 25:  # ここで１２じ以降の条件分岐ぺこ
                            graph.append(ans)
                            #print(ans)
                        else:
                            graph.append(ans - 24)
                            #print(ans - 24)

                        #print("nyan2")
                elif 'H' in l[t][3] and 'M' not in l[t][3]:  # 分数が存在しない場合
                    ans = int(date_match[3]) + 9 - int(dur_match[0])
                    if ans < 25:  # ここで１２じ以降の条件分岐ぺこ
                        graph.append(ans)
                        #print("nyan3")
                    else:
                        graph.append(ans - 24)
                        #print("nyan24")
                else:  # こっちは1時間以下の場合
                    ans = int(date_match[3]) + 9
                    if int(date_match[4]) < int(dur_match[0]):  # 分数が長い場合,これここにも条件分岐必要Dur
                        if ans - 1 < 25:
                            graph.append(ans - 1)
                            #print("nyan4")
                        else:
                            graph.append(ans - 1 - 24)
                            #print("nyan4")
                    else:
                        if ans < 25:  # ここで日付またぐ処理
                            graph.append(ans)
                        else:
                            graph.append(ans - 24)

        # 最適化するとしたらここか
        x1 = graph.count(1)
        x2 = graph.count(2)
        x3 = graph.count(3)
        x4 = graph.count(4)
        x5 = graph.count(5)
        x6 = graph.count(6)
        x7 = graph.count(7)
        x8 = graph.count(8)
        x9 = graph.count(9)
        x10 = graph.count(10)
        x11 = graph.count(11)
        x12 = graph.count(12)
        x13 = graph.count(13)
        x14 = graph.count(14)
        x15 = graph.count(15)
        x16 = graph.count(16)
        x17 = graph.count(17)
        x18 = graph.count(18)
        x19 = graph.count(19)
        x20 = graph.count(20)
        x21 = graph.count(21)
        x22 = graph.count(22)
        x23 = graph.count(23)
        x24 = graph.count(24)

        graph_ans = [x24, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, 
        x17, x18, x19, x20, x21, x22, x23,]

        print('{0}={1}'.format(person,graph_ans))
        count = count + 1
    file_path = "./vtube_list.json"
        # with open(file_path, "r") as json_file:
        #     json_data = json.load(json_file)
    if count == 1:
        json_data = {}
        json_data['vtub_list'] = [] 
    else:
        pass
    json_data['vtub_list'].append(
        {
        count:graph_ans
        }
    )
    print(count)
    with open(file_path, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)







'''
youtube = build("youtube","v3",developerKey=api_key)

search_response = youtube.videos().list(
    part='statistics,contentDetails',
    id=id_,
).execute()

hoge = search_response['items'][0]
details = {'viewCount': int(hoge['statistics']['viewCount']),
           'likeCount': int(hoge['statistics']['likeCount']),
           'dislikeCount': int(hoge['statistics']['dislikeCount']),
           'commentCount': int(hoge['statistics']['commentCount']),
           'duration': ConvertDuration(str(hoge['contentDetails']['duration']))}


request = youtube.search().list(
    part="snippet",
    channelId="UCDh2bWI5EDu7PavqwICkVpA",
    order="date",
    type="video"
)
response = request.execute()

f = codecs.open('output.json', 'w', 'utf-8')
json.dump(response, f,indent=2, ensure_ascii=False)
'''