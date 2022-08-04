import config
import tweepy
import pandas as pd


def getClient():
    client=tweepy.Client(
        consumer_key=config.API_KEY,
        consumer_secret=config.API_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_TOKEN_SECRET,
        bearer_token=config.BEARER_TOKEN
    )
    return client

# name='elonmusk'
uClient=getClient()

#getting all tweets without filter
def getAllTweets(name,maxresult,page):
    uinfo=uClient.get_user(username=name,user_auth=True)
    userid=uinfo.data.id
    pageinator=tweepy.Paginator(
        uClient.get_users_tweets,
        userid,
        max_results=maxresult,
        limit=page
        )
    id=[]
    text=[]
    for page in pageinator:
        if(page.data!=''):
            for i in page.data:
                id.append(i.id)
                text.append(i.text)
        else:
            id.append('null')
            text.append("null")  
    df=pd.DataFrame({'tweetid':id,'tweets':text})
    df.to_csv("./csv/allTweets.csv")
    print('All Tweets Fetched')
    return True


#get followers
def getFollowers(name,maxresult,page):
    uinfo=uClient.get_user(username=name,user_auth=True)
    userid=uinfo.data.id
    pageinator=tweepy.Paginator(
        uClient.get_users_followers,
        userid,
        max_results=maxresult,
        limit=page
        )
    id=[]
    name=[]
    username=[]
    for page in pageinator:
        if(page.data!=''):
            for i in page.data:
                id.append(i.id)
                name.append(i.name)
                username.append(i.username)
        else:
            id.append('null')
            name.append("null")  
            username.append("null")
    df=pd.DataFrame({'userid':id,'name':name,'username':username})
    df.to_csv("./csv/followers.csv")
    print('Followers Fetched')
    return True

#get following
def getFollowing(name,maxresult,page):
    uinfo=uClient.get_user(username=name,user_auth=True)
    userid=uinfo.data.id
    pageinator=tweepy.Paginator(
        uClient.get_users_following,
        userid,
        max_results=maxresult,
        limit=page
        )
    id=[]
    name=[]
    username=[]
    for page in pageinator:
        if(page.data!=''):
            for i in page.data:
                id.append(i.id)
                name.append(i.name)
                username.append(i.username)
        else:
            id.append('null')
            name.append("null")  
            username.append("null")
    df=pd.DataFrame({'userid':id,'name':name,'username':username})
    df.to_csv("./csv/following.csv")
    print('Following Fetched')
    return True

#filter tweets excluding retweets and replies
def getTweetsOnly(name,maxresult,page):
    uinfo=uClient.get_user(username=name,user_auth=True)
    userid=uinfo.data.id
    pageinator=tweepy.Paginator(
        uClient.get_users_tweets,
        userid,
        exclude='retweets,replies',
        max_results=maxresult,
        limit=page
        )
    id=[]
    text=[]
    for page in pageinator:
        if(page.data!=''):
            for i in page.data:
                id.append(i.id)
                text.append(i.text)
        else:
            id.append('null')
            text.append("null")     
    df=pd.DataFrame({'tweetid':id,'tweets':text})
    df.to_csv("./csv/TweetsOnly.csv")
    print('Tweets Fetched')
    return True

#user Mentioned
def getMentionedTweets(name,maxresult,page):
    uinfo=uClient.get_user(username=name,user_auth=True)
    userid=uinfo.data.id
    pageinator=tweepy.Paginator(
        uClient.get_users_mentions,
        userid,
        max_results=maxresult,
        limit=page
        )
    id=[]
    text=[]
    for page in pageinator:
        if(page.data!='' and page.data=='None'):
            for i in page.data:
                id.append(i.id)
                text.append(i.text)
        else:
            id.append('null')
            text.append("null")
    df=pd.DataFrame({'tweetid':id,'tweets':text})
    df.to_csv("./csv/UserMentionedTweets.csv")
    print("Mentions Fethced")
    return True

getMentionedTweets('mrarjunsaud',5,2)

#retweets only
def retweetsOnly(name,maxresult,page):
    uinfo=uClient.get_user(username=name,user_auth=True)
    userid=uinfo.data.id
    pageinator=tweepy.Paginator(
        uClient.get_users_tweets,
        userid,
        exclude='replies',
        max_results=maxresult,
        limit=page
        )
    id=[]
    text=[]
    for page in pageinator:
        if(page.data!=''):
            for i in page.data:
                id.append(i.id)
                text.append(i.text)
        else:
            id.append('null')
            text.append("null")  
    df=pd.DataFrame({'tweetid':id,'tweets':text})
    newdf=df[df['tweets'].str.contains('RT')]
    newdf.to_csv("./csv/userRetweets.csv")
    print("Retweet Fetched")
    return True
    
#replies/response and UserMentioned
def repliesResponse(name,maxresult,page):
    uinfo=uClient.get_user(username=name,user_auth=True)
    userid=uinfo.data.id
    pageinator=tweepy.Paginator(
        uClient.get_users_tweets,
        userid,
        exclude='retweets',
        max_results=maxresult,
        limit=page
        )
    id=[]
    text=[]
    for page in pageinator:
        if(page.data!=''):
            for i in page.data:
                id.append(i.id)
                text.append(i.text)
        else:
            id.append('null')
            text.append("null")  
    df=pd.DataFrame({'tweetid':id,'tweets':text})
    newdf=df[df['tweets'].str.startswith('@')]
    newdf.to_csv("./csv/userReplies.csv")
    print("Replies Fetched")
    return True

