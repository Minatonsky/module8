import pika
import json

from part2.db_connection import establish_connection
from part2.models import Contact


establish_connection()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='email_queue', durable=True)


def send_email(contact):
    print(f"Simulating email sent to {contact.email}...")


def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message['contact_id']

    contact = Contact.objects.get(id=contact_id)

    send_email(contact)

    contact.message_sent = True
    contact.save()

    print(f"Message sent to {contact.email}. Contact updated.")


channel.basic_consume(queue='email_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print('Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
