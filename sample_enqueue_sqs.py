# -*- coding: utf-8 -*-
import boto3
import json
from time import time
import multiprocessing

name = 'gs'
sqs = boto3.resource('sqs')
try:
    # キューの名前を指定してインスタンスを取得
    queue = sqs.get_queue_by_name(QueueName=name)
except:
    # 指定したキューがない場合はexceptionが返るので、キューを作成
    queue = sqs.create_queue(QueueName=name)
 
def enqueue():
    message = '{"email":"test@gmail.com","html_body":"&lt;html&gt;test&lt;/html&gt;","text_body":""}'
    
    # メッセージ×3をキューに送信
    msg_num = 3
    msg_list = [{'Id' : '{}'.format(i+1), 'MessageBody' : json.dumps(message)} for i in range(msg_num)]
    response = queue.send_messages(Entries=msg_list)
    print(response)

if __name__ == '__main__':    
    for n in range(1000):
        p = multiprocessing.Process(target=enqueue,args=())
        p.start()