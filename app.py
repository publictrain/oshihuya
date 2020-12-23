import tweepy
from statistics import mode
from flask import Flask, render_template , request
import collections
import csv
import re
import pandas as pd
import numpy as np
import pprint
import os

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
        pato=[23, 0, 0, 0, 0, 0, 0, 1, 1, 0, 7, 0, 0, 1, 0, 14, 0, 0, 1, 4, 1, 5, 34, 7]
        sha=[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 20, 1, 5, 1, 2, 3, 5, 7, 6, 38]
        mea=[17, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 11, 8, 2, 0, 1, 0, 1, 1, 0, 19, 9, 6, 5]
        miko=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 6, 29, 4, 5, 42, 2, 3, 2, 0, 0]
        yuge=[4, 3, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 0, 1, 5, 4, 6, 8, 21, 10, 18, 5, 8]
        meto=[5, 2, 0, 1, 0, 0, 0, 1, 14, 2, 0, 2, 3, 1, 0, 1, 2, 4, 11, 3, 11, 10, 17, 9]
        kanon=[10, 2, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 2, 1, 3, 3, 5, 14, 11, 17, 16, 4, 3]
        ank=[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 3, 0, 5, 4, 33, 19, 7, 5, 9, 9, 2]
        wat=[5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 6, 8, 8, 7, 11, 10, 19, 6, 4, 9]
        camo=[44, 1, 1, 0, 0, 0, 0, 14, 0, 0, 0, 2, 1, 14, 0, 1, 1, 3, 1, 2, 3, 4, 5, 2]
        rin=[10, 4, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 4, 1, 1, 3, 1, 6, 10, 16, 19, 18, 3]
        anna=[2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 0, 8, 1, 11, 16, 16, 13, 9, 17]
        chris=[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 19, 0, 1, 3, 7, 15, 8, 11, 18, 7]
        haneru=[2, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 9, 2, 1, 1, 1, 0, 2, 3, 2, 1, 16, 53]
        soya=[6, 0, 0, 0, 0, 0, 0, 14, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 32, 26, 6]
        ran=[17, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 3, 2, 2, 1, 1, 4, 5, 9, 13, 23, 9, 4]
        izu=[3, 3, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 25, 5, 5, 17, 30, 4]
        kuku=[10, 2, 0, 0, 0, 0, 1, 2, 0, 1, 3, 1, 1, 1, 1, 5, 1, 11, 7, 8, 21, 9, 12, 2]
        mimi=[44, 1, 1, 0, 0, 0, 0, 14, 0, 0, 0, 2, 1, 14, 0, 1, 1, 3, 1, 2, 3, 4, 5, 2]
        hasi=[11, 12, 0, 0, 0, 0, 1, 3, 0, 0, 0, 2, 1, 0, 3, 4, 4, 0, 3, 33, 7, 12, 3, 0]
        hira=[0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 3, 0, 1, 0, 1, 1, 2, 4, 4, 15, 3, 0]
        sesimaru=[2, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 3, 5, 10, 3, 2, 1]
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
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

#2020/11/1117:23    今やってることフォームのバリデーションとエラーハンドリング
#2020/11/1120:56    バリデーション完了？