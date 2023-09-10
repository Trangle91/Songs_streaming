from confluent_kafka import Consumer
from google.cloud import bigquery
import ast

from google.oauth2 import service_account

#Create BQ credentials object
credentials = service_account.Credentials.from_service_account_file('streamingproject-397921-01dd7416da37.json')

# Construct a BigQuery client object.
bq_client = bigquery.Client(credentials=credentials)

#Speficy BigQuery table to stream to
table_id = 'streamingproject-397921.music.songs'

################ Kafka Consumer #################
c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'Sara-Bareilles-consumer','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

c.subscribe(['Sara-Bareilles-plays'])

def main():
    try:
        while True:
            msg=c.poll(timeout=1.0)  
            if msg is None:
                continue
            if msg.error():
                print('Error: {}'.format(msg.error()))
                continue
            else:
                data=msg.value().decode('utf-8')

                res = ast.literal_eval(data) 
                print(res)

                ##### Stream data into BigQuery table #######
                rows_to_insert = [res]
                print((rows_to_insert))
                errors = bq_client.insert_rows_json(table_id,rows_to_insert) 

                if errors==[]:
                    print("New rows added.")
                else:
                    print("Encountered erros while inserting rows: {}".format(errors))
    finally:
        c.close() 

if __name__ == "__main__":
    main()