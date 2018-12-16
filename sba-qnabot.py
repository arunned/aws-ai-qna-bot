import datetime
import os, boto3
client = boto3.client('comprehend')
sns_client = boto3.client('sns')


def handler(event, context):
    currentTime = datetime.datetime.now()
    print(event)
    topicId = 'undefined'


    try:

        InputStr=event['req']['_event']['inputTranscript']
        print(InputStr)
        sentiment=client.detect_sentiment(Text=InputStr,LanguageCode='en')['Sentiment']

        if sentiment=='NEGATIVE':
            event['res']['message']='I am sorry you are having trouble. Please contact our Disaster Customer Service Center at 1-800-659-2955 (TTY: 1-800-877-8339)'
            sns_client.publish(TopicArn='arn:aws:sns:us-east-1:988029945936:SBA_EMAIL', 
                            Message='Thanks for contacting us. you can visit at https://disasterloan.sba.gov/ela/Home/Questions')
        if len(event['res']['result']['args'][0])> 0:
            topicId=event['res']['result']['args'][0]




    except Exception as ex: 
        topicId='loanq1'
        print(ex)

    ##event['res']['message']=event['req']['_event']['inputTranscript']+message+event['res']['message']

    return event