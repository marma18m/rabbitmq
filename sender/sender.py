import pika

#RabbitMQ Connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='test_queue')

message_to_send = 'Hello RabbitMQ!'

#Send to RabbitMQ
channel.basic_publish(exchange='', routing_key='test_queue', body=message_to_send)
print('Sent: ' + message_to_send)

connection.close()