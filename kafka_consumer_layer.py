from kafka import KafkaConsumer

class KafkaConsumerLayer():
    def __init__(self, host, port, topic):
        self.consumer = KafkaConsumer(topic, bootstrap_servers="{}:{}".format(host, port))

    def consume(self):
        