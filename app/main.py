import sys

import pika


QUEUE_NAME = 'test_queue'
HOST = 'localhost'


class MessageBroker:
    def __init__(self, queue_name: str = QUEUE_NAME, host: str = HOST) -> None:
        """
        Initialize the MessageBroker with the given queue name and host.

        Args:
            queue_name (str): The name of the queue. Defaults to 'test_queue'.
            host (str): The host of the message broker. Defaults to 'localhost'.

        Returns:
            None
        """
        self.queue_name = queue_name
        self.host = host
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.host)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def send_message(self, message: str) -> None:
        """
        Send a message to the queue.

        Args:
            message (str): The message to send to the queue.
        """
        self.channel.basic_publish(
            exchange='', routing_key=self.queue_name, body=message)
        print(f'Sent {message}')

    def receive_messages(self) -> None:
        """
        Start receiving messages from the queue.
        """
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=lambda ch, method, properties, body: print(
                f'Received {body.decode()}'),
            auto_ack=True
        )

        print('Waiting for messages. To exit press CTRL+C')

        self.channel.start_consuming()

    def close_connection(self) -> None:
        """
        Close the connection to the message broker.
        """
        self.connection.close()


if __name__ == '__main__':
    broker = MessageBroker(queue_name=QUEUE_NAME, host=HOST)
    if len(sys.argv) > 1 and sys.argv[1] == 'send':
        broker.send_message(message='Hello, World!')
    else:
        broker.receive_messages()
