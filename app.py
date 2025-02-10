from utility import UtilityClass
from kafka_producer_layer import KafkaProducerLayer
import schedule


def send_message():
    result= UtilityClass.send_get_request("http://randomuser.me/api/", {"results": 100})
    if result  == None:
        return
    kfka = KafkaProducerLayer("localhost", 9092, "users")
    kfka.produce(result)
    
        
def run_app(): 
    schedule.every(10).seconds.do(send_message)
    while True:
        schedule.run_pending()   


if __name__ == "__main__":
    run_app()