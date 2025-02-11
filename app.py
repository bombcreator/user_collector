from utility import UtilityClass
from kafka_producer_layer import KafkaProducerLayer
import schedule
import json


def send_message():
    result= UtilityClass.send_get_request("http://randomuser.me/api/", {"results": 100, "nat": "ir"})
    if result  == None:
        return
    kfka = KafkaProducerLayer("localhost", 19092, "users")
    for user in result:
        kfka.produce(json.dumps(user))

    
        
def run_app(): 
    schedule.every(10).seconds.do(send_message)
    while True:
        schedule.run_pending()   


if __name__ == "__main__":
    run_app()