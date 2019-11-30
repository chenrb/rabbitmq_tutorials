import pika
import sys

# 创建连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        virtual_host='itsm'
    )
)
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)  # 消息持久性

message = ' '.join(sys.argv[1:]) or 'Hello World!'
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent消息持久性
    )
)
print(" [x] Sent %r" % message)

connection.close()
