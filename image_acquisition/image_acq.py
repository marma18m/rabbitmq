import pika, sys, os
import time
from schemas.message import MessageJSON

while True:
    # Initialize json message
    msg = MessageJSON()

    # set timestamp current unix timestamp
    msg.set_timestamp(int(time.time()))
    msg.set_acquisition_device_info(1, 'baumer_camera')
    msg.set_image_info(1, 1, '/path/to/image')

    # RabbitMQ Connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()
    channel.queue_declare(queue='image_acquisition_queue')

    # Send to RabbitMQ
    channel.basic_publish(
        exchange='',
        routing_key='image_acquisition_queue',
        body=msg,
    )
    print('Sent message to RabbitMQ')

    connection.close()

    # Wait for 10 seconds
    time.sleep(10)
