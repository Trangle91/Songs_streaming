# This project streams songs into Big query using Kafka, containerized with Docker 

## Requirements and installation:
- Docker
- Kafka (pip install confluent-kafka)
- BigQuery API (pip install google-cloud-bigquery)
- Faker (pip install Faker) (to generate songs)

## Prerequisites:
- Enable BigQuery API and configure it for the service account being used.
- Create a table in BQ.

## How to run:
- Build the container: docker-compose up -d
- Build the producer: python producer.py
- Build the consumer: python consumer.py

## Result: data loading into BQ table

<img width="1296" alt="Screen Shot 2023-09-10 at 7 18 30 PM" src="https://github.com/Trangle91/Songs_streaming/assets/25968329/98bceea2-9050-43cd-b0bf-17d6efb2d9b6">


## Improvement:
- the cycle can be automated with airflow.  
- data can then be analyzed in Looker or Power BI for data analysis.
