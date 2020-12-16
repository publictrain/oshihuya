import tweepy
from statistics import mode
from flask import Flask, render_template , request
import collections
import csv
import re
import pandas as pd
import numpy as np
import pprint

# 取得した各種キーを格納---------------------------------------------
consumer_key ="VFK2ZOVvUyBGjElOiSVFVdd3t"
consumer_secret ="tr9IVfluXTEvUCGROUAU25xx6ra669kyRuecaUmB9LKqMgKObW"
access_token="1041705087502970881-9xWbgxJPmC4v4Xd2NHNy8nGlqLlHac"
access_token_secret ="VLmcGglV8PzYLzKsV5MBxllcxVPhElQz7Pjsec3eqrgg4"
 
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#-------------------------------------------------------------------
 
app = Flask(__name__)

#@app.route('/', methods=['POST'])
#def post():
#	name = request.form.get('inin')
    

@app.route("/about.html")
def index():
    return render_template("about.html")

@app.route("/contact.html")
def index2():
    return render_template("contact.html")

@app.route('/' , methods= ['GET' , 'POST'])


#ツイートを投稿

def twi():
    try:

        name = request.form.get('name')
        tweet_number = request.form.get('name2')

        Account = name #取得したいユーザーのユーザーIDを代入
        tweets = api.user_timeline(Account, count=tweet_number, page=1)
        num = 1 #ツイート数を計算するための変数
        date_list = []
        for tweet in tweets:
            #print('twid : ', tweet.id)               # tweetのID
            #print('user : ', tweet.user.screen_name)  # ユーザー名
            #print('date : ', tweet.created_at)      # 呟いた日時
            #print(tweet.text)                  # ツイート内容
            #print('favo : ', tweet.favorite_count)  # ツイートのいいね数
            #print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
            #print('ツイート数 : ', num) # ツイート数
            #print('='*80) # =を80個表示
            num += 1 # ツイート数を計算
            str_date = str(tweet.created_at)
            #str_time = str_date.split('-')[2]
            str_time = int(str_date.split(' ')[-1].split(':')[0]) + 9
            if str_time >= 24:
                str_time = str_time - 24
            date_list.append(str_time)
        
        sent_list = []

        for i in range(24):
            #print(i)#debug
            #print(date_list.count(i))#debug
            sent_list.append(date_list.count(i))
        

        print(Account)
        pato=[21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1, 0, 1, 2, 10, 2, 0, 4, 8, 4, 5, 29, 6]
        sha=[4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 21, 0, 5, 1, 2, 3, 4, 6, 4, 35]
        mea=[17, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 14, 6, 2, 0, 1, 0, 0, 0, 0, 20, 6, 5, 8]
        miko=[2, 0, 0, 1, 0, 0, 3, 0, 0, 1, 1, 1, 7, 1, 4, 23, 3, 7, 38, 3, 0, 2, 1, 1]
        yuge=[0, 3, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 3, 0, 2, 2, 4, 5, 9, 28, 10, 15, 6, 9]
        meto=[2, 2, 0, 1, 0, 0, 1, 2, 12, 2, 2, 1, 6, 2, 0, 1, 3, 4, 7, 3, 8, 9, 24, 7]
        kanon=[10, 2, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 2, 1, 3, 3, 5, 13, 11, 19, 16, 3, 3]
        ank=[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 2, 0, 3, 4, 34, 16, 8, 10, 9, 8, 2]
        wat=[5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 7, 10, 6, 9, 9, 21, 9, 5, 10]
        camo=[24, 13, 10, 4, 0, 0, 1, 0, 0, 0, 0, 2, 0, 3, 1, 4, 1, 0, 1, 4, 1, 4, 11, 15]
        rin=[12, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 3, 8, 10, 19, 14, 20, 3]
        anna=[2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 0, 7, 1, 8, 16, 17, 14, 10, 17]
        chris=[3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 2, 1, 15, 0, 0, 3, 7, 16, 10, 11, 22, 7]
        haneru=[1, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 11, 2, 0, 1, 1, 0, 1, 1, 2, 3, 16, 53]
        soya=[5, 0, 0, 0, 0, 0, 0, 15, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 7, 34, 24, 6]
        ran=[16, 0, 0, 0, 1, 1, 0, 0, 1, 2, 1, 2, 3, 2, 1, 1, 1, 5, 6, 10, 13, 19, 9, 5]
        izu=[2, 1, 5, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 28, 4, 10, 15, 25, 4]
        kuku=[7, 2, 0, 0, 0, 0, 1, 1, 0, 1, 2, 1, 1, 1, 1, 5, 1, 13, 5, 8, 22, 9, 14, 4]
        mimi=[48, 0, 1, 0, 0, 0, 0, 15, 0, 0, 0, 2, 0, 14, 0, 0, 3, 3, 1, 2, 4, 1, 4, 1]
        hasi=[11, 11, 0, 0, 0, 0, 1, 3, 1, 1, 0, 2, 1, 2, 2, 5, 5, 0, 3, 29, 8, 12, 2, 0]
        hira=[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 2, 0, 1, 0, 0, 1, 2, 3, 5, 12, 8, 0]
        sesimaru=[5, 1, 0, 0, 0, 0, 0, 9, 0, 0, 0, 1, 2, 2, 0, 0, 0, 1, 2, 4, 7, 4, 0, 0]
        modomodo = mode(date_list)
        print(sent_list)
        print(date_list)
        return render_template('index.html', name=name, modomodo=modomodo, sent_list=sent_list,
        miko=miko,mea=mea, pato=pato, sha=sha, yuge=yuge, meto=meto, kanon=kanon, ank=ank, wat=wat, camo=camo, rin=rin, anna=anna, chris=chris, 
        haneru=haneru, soya=soya, ran=ran, izu=izu, kuku=kuku, mimi=mimi, hasi=hasi, hira=hira, sesimaru=sesimaru)
    except:
        error = 'error'
        print('えらーだにゃん')
        return render_template('index.html', title='flask test',error=error)




#print(date_list)
#print(mode(date_list))
#def graph():
#    peko
#    print(peko)
#    return render_template('index.html', peko=peko)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)

#2020/11/1117:23    今やってることフォームのバリデーションとエラーハンドリング
#2020/11/1120:56    バリデーション完了？