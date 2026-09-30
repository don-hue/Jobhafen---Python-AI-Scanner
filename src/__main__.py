from .controller import create_app
from .config import RabbitMQConnection
from .config import RabbitMQCrawlerConfig

def main ():
    config = RabbitMQConnection
    try:
        connection = config.get_connection()
        crawler_channel = config.get_channel()
        postgres_channel = config.get_channel()
        crawler_config = RabbitMQCrawlerConfig(crawler_channel)
        

    finally: 
        config.close()
    

if __name__ == "__main__":
    main()