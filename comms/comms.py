import json
import logging
import pika, sys, os
import time
from schemas.message import MessageJSON
from schemas.comms_message import CommsMessageJSON
from comms_utils import extract_results_action, take_action

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


def main():

    # RabbitMQ Connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()

    # Declare the queues yo want to use
    comms_queue = 'communications_queue'
    image_acq_queue = 'image_acquisition_queue'
    inference_config_queue = 'inference_config_queue'
    channel.queue_declare(queue=comms_queue)
    channel.queue_declare(queue=image_acq_queue)
    channel.queue_declare(queue=inference_config_queue)
    log.warning('Queues declared')

    # Build message to publish
    img_msg = CommsMessageJSON()
    img_msg.set_timestamp(int(time.time()))

    # Build message to publish
    inference_msg = CommsMessageJSON()
    inference_msg.set_timestamp(int(time.time()))

    # Example of a Trigger message
    img_msg.set_tag('Trigger')
    img_msg.set_value(1)
    channel.basic_publish(
        exchange='',
        routing_key=image_acq_queue,
        body=json.dumps(img_msg.get_message()),
    )

    # Example of a LoadRecipe message
    inference_msg.set_tag('LoadRecipe')
    inference_msg.set_value(1)
    channel.basic_publish(
        exchange='',
        routing_key=inference_config_queue,
        body=json.dumps(inference_msg.get_message()),
    )

    # Method to handle the message received
    def comms_callback(ch, method, properties, body):
        log.warning("Results received: ")
        message = MessageJSON()
        message.parse_from_string(body)
        log.warning("body:\n " + json.dumps(message.get_message(), indent=4))

        action = extract_results_action(message)
        take_action(action)

    channel.basic_consume(
        queue=comms_queue, on_message_callback=comms_callback, auto_ack=True
    )

    log.warning(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
