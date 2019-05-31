import requests
import boto3

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #print 'In index'
    client = boto3.client('lambda')	
    client.invoke(FunctionName='PeterHiggs',InvocationType='Event')
    return render_template('success.html')

@app.route('/index2')
def index2():
#The following code block invokes, via the Boto invoke method, the Lambda Function PeterHiggs that resides in the us-east-2 region on the JB AWS account
    #print ('in invoker')
    client = boto3.client('lambda')	
    client.invoke(FunctionName='PeterHiggs',InvocationType='Event')
    return render_template('success.html')

@app.route('/index3')
def index3():
#The following code block invokes PeterHiggs by making an HTTP 
#Get request 
    URL = 'https://nb32f8xq5d.execute-api.us-east-1.amazonaws.com/Birmingham/higgseffect'
    resE = requests.get(url=URL,timeout=200)
    #print ('resE = ',resE)
    return render_template('success.html')

#pete\Scripts\activate
#put the python script in ../python27/pete/Scripts
#cd pete\Scripts
#python my_flask_app.py
#when I first ran python my_flask_app.py I got 
#the error could not find module six
#this error was comming from dropbox
#apparently when I installed flask and zappa six
#one of them caused six to get uninstalled from
#where it had been which was in python27/Lib/site-packages
#weirdness but the way I dealt with it was as
#follows
#pip install --ignore-installed --upgrade six
