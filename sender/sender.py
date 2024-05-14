import sys
import os
import pika
from messages.output import test_pb2

# Create a message
message = test_pb2.ImageAcquisition()

# Set the message fields
message.timestamp = 1715605786
message.image_location = 'path/to/image'
message.camera_specs.camera_spec_1 = 'Camera Spec 1'
message.camera_specs.camera_spec_2 = 2

# RabbitMQ Connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='test_queue')

# Send to RabbitMQ
channel.basic_publish(
    exchange='', routing_key='test_queue', body=message.SerializeToString()
)
print('Sent message to RabbitMQ')

connection.close()
