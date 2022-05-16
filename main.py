import requests, json
from datetime import datetime

COOKIE = 'kdt=YpXVjcRvvie41eCaFhjgZthMUohnYSgVX7Ip5yjv; remember_checked_on=1; night_mode=1; guest_id_marketing=v1:163654089706383564; guest_id_ads=v1:163654089706383564; mbox=PC#67d728b726074c4b8345229670c2d915.38_0#1706531559|session#8a387d67035f4da1ba9e4bd40b280094#1643288619; _ga_BYKEBDM7DS=GS1.1.1643286758.3.1.1643286776.0; _ga=GA1.2.2019531962.1608127929; ads_prefs="HBERAAA="; auth_multi="835384057:ffd96d300440b30373d1731e7443743a38433a21"; auth_token=d24969cf3442dc0ec1f357ccabba319a5155e6ad; personalization_id="v1_L58B1wYoKZZqV2n+IpXIOA=="; guest_id=v1:164440397856716100; twid=u=1451877111921135623; ct0=e165b0b966fc2838f68f5dc9273e7e24249cb7124a21c0e907fb85a813149d562c343e8a550fca8ad17355c981462a2168b5ef5bd04558e385942842c620ab34f80d3f2b108576c4eb2b863a146b3d01; _gid=GA1.2.851256753.1644749471; lang=th'
TARGET_ACCOUNT_NAME = None
init = 1
posts = []

start_time = None

def get_csrf_token(cookie):
    start = cookie.find('ct0=') + 4
    end = cookie.find('ct0=') + 164
    return cookie[start:end]

FETCH_HEADERS = {
    'Host': 'twitter.com',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'x-twitter-client-language': 'th',
    'x-csrf-token': get_csrf_token(COOKIE),
    'sec-ch-ua-mobile': '?0',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-active-user': 'yes',
    'sec-ch-ua-platform': 'Windows',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://twitter.com/bbangbangz',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'eth-TH,th;q=0.9,en;q=0.8',
    'Cookie': COOKIE,
}

def get_account_id(username):
    
    PARAMS = '{{"screen_name":"{0}","withSafetyModeUserFields":true,"withSuperFollowsUserFields":false,"withNftAvatar":false}}'.format(username)
    ENDPOINT_URL = 'https://twitter.com/i/api/graphql/1CL-tn62bpc-zqeQrWm4Kw/UserByScreenName?variables={0}'.format(PARAMS)
    
    response = requests.get(ENDPOINT_URL, headers=FETCH_HEADERS)
    return response.json()

def fetch_tweets(user_id):
    PARAMS = '{{"userId":"{0}","count":20,"withTweetQuoteCount":true,"includePromotedContent":false,"withQuickPromoteEligibilityTweetFields":false,"withSuperFollowsUserFields":false,"withUserResults":true,"withBirdwatchPivots":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":false,"withVoice":true,"withNftAvatar":false}}'.format(user_id)
    ENDPOINT_URL = 'https://twitter.com/i/api/graphql/7H08fw6RZtSMEWmmICCvJA/UserTweets?variables={0}'.format(PARAMS)
    
    response = requests.get(ENDPOINT_URL, headers=FETCH_HEADERS)
    return response.json()

def reply_tweets(username, tweet_id, message):
    
    payload = json.dumps(
        {
            "variables": {
                "tweet_text": "{0}".format(message),
                "reply": {
                    "in_reply_to_tweet_id": "{0}".format(tweet_id),
                    "exclude_reply_user_ids":[]
                },
                "media": {
                    "media_entities":[],
                    "possibly_sensitive":False
                },
                "withReactionsMetadata":False,
                "withReactionsPerspective":False,
                "withSuperFollowsTweetFields":False,
                "withSuperFollowsUserFields":False,
                "semantic_annotation_ids":[],
                "dark_request":False,
                "withUserResults":True,
                "withBirdwatchPivots":False,
                "withNftAvatar":False
            },
            "queryId": "IvH4F5G1xsfhz2uHC1d4IQ"
        }
    )
    
    
    headers = {
        'Host':'twitter.com',
        'Connection':'keep-alive',
        'sec-ch-ua':'"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'x-twitter-client-language':'th',
        'x-csrf-token': get_csrf_token(COOKIE),
        'sec-ch-ua-mobile':'?0',
        'authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'content-type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'x-twitter-auth-type':'OAuth2Session',
        'x-twitter-active-user':'yes',
        'sec-ch-ua-platform':"Windows",
        'Accept':'*/*',
        'Origin':'https://twitter.com',
        'Sec-Fetch-Site':'same-origin',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Dest':'empty',
        'Referer': 'https://twitter.com/{0}/status/{1}'.format(username, tweet_id),
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'th-TH,th;q=0.9,en;q=0.8',
        'Cookie': COOKIE,
    }
    
    ENDPOINT_URL = 'https://twitter.com/i/api/graphql/IvH4F5G1xsfhz2uHC1d4IQ/CreateTweet'
    
    response = requests.post(ENDPOINT_URL, headers=headers, data=payload)
    
    return response.json()

def check_timeline(username):
    
    global init, posts, start_time
    
    user_id = get_account_id(username)['data']['user']['result']['rest_id']
    entries = fetch_tweets(user_id)['data']['user']['result']['timeline']['timeline']['instructions'][1]['entries']

    #print(entries)
    
    for entry in entries:
        if entry['entryId'].startswith('tweet-'):
            
            post_id = entry['entryId'].split('-')[1]
            
            
            if init == 1:
                if post_id not in posts:
                    posts.append(post_id)
            if init == 0:
                if post_id not in posts:

                    raw_created_at = entry['content']['itemContent']['tweet_results']['result']['legacy']['created_at']

                    #Wed Feb 09 10:25:12 +0000 2022
                    created_at = datetime.strptime(raw_created_at, '%a %b %d %X %z %Y')
                    fetched_time = datetime.strftime(created_at, "%Y-%m-%d %H:%M:%S")
                    
                    print(post_id)
                    print(fetched_time)
                    print(start_time)
                    
                    if fetched_time >= start_time:
                        posts.append(post_id)
                        reply_tweets(username, post_id, "hi")
                        print("Replied.")
                        return True
            
    print("Checking")
    return False

start_time = datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%M:%S")
while True:
    
    
    if check_timeline("Mild20159") == True:
        break
    init = 0
