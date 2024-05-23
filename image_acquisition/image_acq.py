import pika, sys, os
import time
import json
from schemas.message import MessageJSON
from schemas.comms_message import CommsMessageJSON
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)

while True:

    model_queue = 'model_queue'
    comms_queue = 'communications_queue'
    image_acq_queue = 'image_acquisition_queue'

    # RabbitMQ Connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()
    channel.queue_declare(queue=model_queue)
    channel.queue_declare(queue=comms_queue)
    channel.queue_declare(queue=image_acq_queue)

    log.warning('Writing image acquisition info...')

    # Initialize json message
    msg = MessageJSON()

    # Set timestamp current unix timestamp
    msg.set_timestamp(int(time.time()))
    msg.set_acquisition_device_info(1, 'baumer_camera')
    image_ID = +1
    msg.set_image_info(image_ID, 1, '/path/to/image')

    log.warning('Sending image to model inference queue...')

    # Send to RabbitMQ
    channel.basic_publish(
        exchange='',
        routing_key=model_queue,
        body=json.dumps(msg.get_message()),
    )
    log.warning('Image sent')

    # Example of a LoadRecipe message
    comms_message = CommsMessageJSON()
    comms_message.set_timestamp(int(time.time()))
    comms_message.set_tag('RecipeLoaded')
    comms_message.set_value(1)

    # Send to RabbitMQ
    channel.basic_publish(
        exchange='',
        routing_key=comms_queue,
        body=json.dumps(comms_message.get_message()),
    )

    def img_acq_callback(ch, method, properties, body):
        log.warning('Received message from image_acquisition_queue')
        message = CommsMessageJSON()
        message.parse_from_string(body)

        log.warning('Received message: ' + message.get_message())

    channel.basic_consume(
        queue=image_acq_queue,
        on_message_callback=img_acq_callback,
        auto_ack=True,
    )

    # TODO: research wether this is necessary
    connection.close()

    # Wait for 10 seconds
    time.sleep(10)
