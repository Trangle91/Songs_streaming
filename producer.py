from confluent_kafka import Producer
from faker import Faker
import json
import time
import logging

#Create Faker object
fake=Faker()

#Sara Bareilles playlist
songs = ["Gravity", "A safe place to land", "She used to be mine","Manhattan","Armor","Love song","The same blood","Upside down","I choose you","Brave"]

#Configure logger
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Create Kafka Producer
p=Producer({'bootstrap.servers':'localhost:9092'})

#Callback function
def receipt(err,msg):
    if err is not None:
        print('Failed to deliver message: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

#Write Producer loop that acts like user activity
def main():
    for i in range(20):
        random_song_id = fake.random_int(min=0, max=9)
        data={
           'user_id': fake.random_int(min=20000, max=100000),
           'artist': 'Sara-Bareilles',
           'song_id': random_song_id, 
           'song_name':  songs[random_song_id],
           'event_type':'song_completed',
           'timestamp': str(fake.date_time_this_month())    
           }
        m=json.dumps(data)
        p.produce('Sara-Bareilles-plays', m.encode('utf-8'),callback=receipt)
        p.poll(1) 
        p.flush() 
        time.sleep(3)

if __name__ == '__main__':
    main()