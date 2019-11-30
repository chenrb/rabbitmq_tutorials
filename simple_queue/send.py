import pika

# 创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', virtual_host='itsm'))
channel = connection.channel()

# 创建队列
channel.queue_declare(queue='hello')

# 指定交换机
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World')
print(" [x] Sent 'Hello World!'")

connection.close()