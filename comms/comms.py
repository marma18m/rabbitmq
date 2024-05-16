import pika, sys, os
from schemas.message import MessageJSON
from comms_utils import extract_comms_action, take_action
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def main():

    # RabbitMQ Connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()

    comms_queue = 'communications_queue'
    channel.queue_declare(queue=comms_queue)
    log.info('Queues declared')

    def comms_callback(ch, method, properties, body):
        log.info("Results received: ")
        message = MessageJSON()
        message.parse_from_string(body)
        log.info("body:\n ", message)

        action = extract_comms_action(message)
        take_action(action)

    channel.basic_consume(
        queue=comms_queue, on_message_callback=comms_callback, auto_ack=True
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
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
