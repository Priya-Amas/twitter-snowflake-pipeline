from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import sys

# Adds your project root (one level above airflow/) to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from src.twitter_to_csv import fetch_and_save_tweets
from src.load_to_snowflake import load_csv_to_snowflake

default_args = {
    'owner': 'priya',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='twitter_pipeline_dag',
    default_args=default_args,
    description='Fetch tweets and load them into Snowflake',
    schedule_interval='@daily',
    start_date=datetime(2025, 6, 1),
    catchup=False,
    tags=['twitter', 'snowflake'],
) as dag:

    fetch_tweets = PythonOperator(
        task_id='fetch_tweets',
        python_callable=fetch_and_save_tweets,
    )

    load_to_snowflake = PythonOperator(
        task_id='load_to_snowflake',
        python_callable=load_csv_to_snowflake,
    )

    fetch_tweets >> load_to_snowflake
