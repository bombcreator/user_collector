from kafka import KafkaProducer
from kafka.errors import KafkaError
from log_utility import LoggerLayer
class KafkaProducerLayer():
    def __init__(self, host, port, topic):
        self.producer = KafkaProducer(bootstrap_servers="{}:{}".format(host, port),
                                      value_serializer = lambda x: x.encode('utf-8'))
        self.topic = topic
        self.logger = LoggerLayer()
        

    def produce(self, message):
        try:
            self.producer.send(self.topic, message)
            self.producer.flush()
            self.logger.log_info(f"message sent to topic {self.topic}")
        except KafkaError as e:
            self.logger.log_error(f"error while sending message to topic {self.topic} : {e}")


        