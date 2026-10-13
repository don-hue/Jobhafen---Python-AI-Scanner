import os
from pika.adapters.blocking_connection import BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel
from pika import ConnectionParameters

class RabbitMQConnection: 
    def __init__(self):
        self._connection: BlockingConnection | None = None

    def get_connection(self) -> BlockingConnection: 
        if self._connection is None or self._connection.is_closed: 
            self._connection = BlockingConnection(
                ConnectionParameters(
                    host=os.getenv("RABBITMQ_HOST", "localhost"),
                    port=int(os.getenv("RABBITMQ_PORT", "5672")),
                    virtual_host=os.getenv("RABBITMQ_VHOST", "/"),
                    credentials=pika.PlainCredentials(
                        username=os.getenv("RABBITMQ_USER", "admin"),
                        password=os.getenv("RABBITMQ_PASSWORD", "admin"),
                    ),
                    heartbeat=60,
                    blocked_connection_timeout=30,
                )
            )

        return self._connection

    def get_channel(self) -> BlockingChannel:
        if self._connection is None or self._connection.is_closed: 
            self._connection = self.get_connection()
            return self._connection.channel()

        else: 
            return self._connection.channel()

    def close(self) -> None: 
        if self._connection is not None and self._connection.is_open: 
            self._connection.close()

        self._connection = None
    


