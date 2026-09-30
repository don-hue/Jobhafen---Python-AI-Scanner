import pika
from typing import Final
from pika.adapters.blocking_connection import BlockingChannel

class RabbitMQCrawlerConfig:
    EXCHANGE: Final[str] = "jobs.exchange"
    ANALYZE_JOB_QUEUE:Final[str] = "jobs.request.analyzeJob.queue"
    ANALYZE_JOB_ROUTING_KEY:Final[str] = "jobs.analyzeJob.request"

    def __init__(self, channel: BlockingChannel): 
        self.channel = channel

    def configure_anlayze_queue(self) -> None: 
        self.channel.exchange_declare(exchange= self.EXCHANGE, exchange_type="direct")
        self.channel.queue_declare(queue=self.ANALYZE_JOB_QUEUE)
        self.channel.queue_bind(exchange=self.EXCHANGE, queue=self.ANALYZE_JOB_QUEUE,routing_key=self.ANALYZE_JOB_ROUTING_KEY)

