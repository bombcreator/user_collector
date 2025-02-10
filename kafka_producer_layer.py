from kafka import KafkaProducer

class KafkaProducerLayer():
    def __init__(self, host, port, topic):
        self.producer = KafkaProducer(bootstrap_servers="{}:{}".format(host, port))
        self.topic = topic

    def produce(self, message):
        self.producer.send(self.topic, message)
        self.producer.flush()

        