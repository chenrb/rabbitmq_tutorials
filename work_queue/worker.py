import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        virtual_host='itsm'
    )
)
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 消息确认


channel.basic_qos(prefetch_count=1)  # 公平模式，需要开启消息确认
channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
)

channel.start_consuming()
