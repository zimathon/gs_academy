import boto3
import json
 
# キューの名前を指定して
name = 'gs'
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName=name)

while True:
    # メッセージを取得
    msg_list = queue.receive_messages(MaxNumberOfMessages=10)
    if msg_list:
        for message in msg_list:
            print(message.body)
            json_message = json.loads(json.loads(message.body))
            print(json_message)
            print(json_message["email"])
            print(json_message["html_body"])
            message.delete()
    else:
        # メッセージがなくなったらbreak
        break