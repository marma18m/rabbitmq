import pika, sys, os
from messages.output import test_pb2


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()

    image_acq_queue = 'image_acquisition_queue'
    ram_volume_queue = 'ram_volume_queue'

    channel.queue_declare(queue=image_acq_queue)
    channel.queue_declare(queue=ram_volume_queue)

    def image_callback(ch, method, properties, body):
        print("\nReceived: ")
        message = test_pb2.ImageAcquisition()
        message.ParseFromString(body)

        message.timestamp = 1715605786
        message.image_location = 'new_path/to/image'

        print("\nbody:\n ", message)

        # Publish the received message to the other queue
        channel.basic_publish(
            exchange='',
            routing_key=ram_volume_queue,
            body=message.SerializeToString(),
        )
        print('Sent message to ' + ram_volume_queue)

    channel.basic_consume(
        queue=image_acq_queue, on_message_callback=image_callback, auto_ack=True
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
