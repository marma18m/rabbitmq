import pika, sys, os
from schemas.message import MessageJSON
from model_utils import predict_result
import logging
import json

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


def main():
    # RabbitMQ Connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()

    # Declare the queues
    model_queue = 'model_queue'
    comms_queue = 'communications_queue'
    channel.queue_declare(queue=comms_queue)
    channel.queue_declare(queue=model_queue)

    log.warning('Queues declared')

    def model_callback(ch, method, properties, body):
        log.warning("Image received: ")
        msg = MessageJSON()
        msg.parse_from_string(body)

        log.warning("body:\n " + json.dumps(msg.get_message(), indent=4))

        msg.set_inference_service_id(1)
        # Predict result and set the info in the message
        image_path = msg.message["imageInfo"]["path"]
        result, result_timestamp = predict_result(image_path)
        result_path = f'/path/to/result/{result}'
        comms_result_path = f'/path/to/comms/result/{result}'
        msg.set_result_info(result_timestamp, result_path, comms_result_path)

        # Serialize the message to a JSON formatted string
        json_message = json.dumps(msg.get_message())

        # Publish the received message to the comms queue
        channel.basic_publish(
            exchange='',
            routing_key=comms_queue,
            body=json_message,
        )
        log.warning('Sent message to ' + comms_queue)

    # Consume messages from the image_acquisition_queue
    channel.basic_consume(
        queue=model_queue, on_message_callback=model_callback, auto_ack=True
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
