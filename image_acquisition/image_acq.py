import pika, sys, os
import time
import json
from schemas.message import MessageJSON
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

while True:
    log.info('Writing image acquisition info...')
    # Initialize json message
    msg = MessageJSON()

    # set timestamp current unix timestamp
    msg.set_timestamp(int(time.time()))
    msg.set_acquisition_device_info(1, 'baumer_camera')
    image_ID = +1
    msg.set_image_info(image_ID, 1, '/path/to/image')

    # Serialize the message to a JSON formatted string
    json_message = json.dumps(msg.get_message())

    model_queue = 'model_queue'

    # RabbitMQ Connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()
    channel.queue_declare(queue=model_queue)

    log.info('Sending image to RabbitMQ...')
    # Send to RabbitMQ
    channel.basic_publish(
        exchange='',
        routing_key=model_queue,
        body=json_message,
    )

    log.info('Image sent')

    connection.close()

    # Wait for 10 seconds
    time.sleep(10)
