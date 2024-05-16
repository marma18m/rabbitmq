import pika, sys, os


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()

    ram_volume_queue = 'ram_volume_queue'
    comms_queue = 'communications_queue'

    channel.queue_declare(queue=comms_queue)
    channel.queue_declare(queue=ram_volume_queue)

    def model_callback(ch, method, properties, body):
        print("\nReceived: ")
        message = comms_pb2.ImageAcquisition()
        message.ParseFromString(body)

        comms_message = comms_pb2.CommsMessage()

        print("\nbody:\n ", message)

        # Publish the received message to the other queue
        channel.basic_publish(
            exchange='',
            routing_key=ram_volume_queue,
            body=message.SerializeToString(),
        )
        print('Sent message to ' + ram_volume_queue)

    channel.basic_consume(
        queue=comms_queue, on_message_callback=model_callback, auto_ack=True
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
