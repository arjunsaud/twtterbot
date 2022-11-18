from flask import Flask, render_template ,request
import customFunctions as cf
from werkzeug.wrappers import Response

app=Flask(__name__)
app.secret_key='super-secret-key'

@app.route("/",methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/fetch", methods=['GET','POST'])
def fetchDatas():
    if(request.method=='POST'):
        twitterusername=request.form.get('username')
        mxr=request.form.get('maxresults')
        maxresult=int(mxr)
        pg=request.form.get('page')
        page=int(pg)
        if(twitterusername):
            if(cf.getFollowers(twitterusername,maxresult,page) and 
            cf.getFollowing(twitterusername,maxresult,page) and 
            cf.getMentionedTweets(twitterusername,maxresult,page) and
            cf.getAllTweets(twitterusername,maxresult,page) and
            cf.getTweetsOnly(twitterusername,maxresult,page) and
            cf.retweetsOnly(twitterusername,maxresult,page) and
            cf.repliesResponse(twitterusername,maxresult,page)):
                return render_template('fetched.html')
            else:
                return "Somthing Went Wrong"
             
        else:
            return "Uername is Required"  

@app.route('/download')
def download():
    response = Response(mimetype='text/csv')
    response.headers.set("Content-Disposition", "attachment", filename="./csv/followers.csv")
    response.headers.set("Content-Disposition", "attachment", filename="./csv/userReplies.csv")
    response.headers.set("Content-Disposition", "attachment", filename="./csv/userRetweets.csv")
    response.headers.set("Content-Disposition", "attachment", filename="./csv/TweetsOnly.csv")
    response.headers.set("Content-Disposition", "attachment", filename="./csv/following.csv")
    response.headers.set("Content-Disposition", "attachment", filename="./csv/allTweets.csv")
    return response

if __name__=='__main__':
    app.run()
