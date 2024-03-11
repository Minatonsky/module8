import pika
import json
from faker import Faker
from part2.db_connection import establish_connection
from part2.models import Contact

establish_connection()


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='email_queue', durable=True)

fake = Faker()
num_contacts = 10

for _ in range(num_contacts):
    contact = Contact(
        full_name=fake.name(),
        email=fake.email()
    )
    contact.save()

    message = {'contact_id': str(contact.id)}
    channel.basic_publish(exchange='',
                          routing_key='email_queue',
                          body=json.dumps(message),
                          properties=pika.BasicProperties(
                              delivery_mode=2,
                          ))

print(f"{num_contacts} contacts added to the queue.")

connection.close()
