from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from nytimes_best_seller_etl import run_nytimes_best_seller_etl

default_args = {
    'owner' : 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 9, 26),
    'email': ['nelsongee5+airflow_test@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)

}

dag = DAG(  'nytimes_best_seller_etl', 
            default_args=default_args,
            description='DAG to the nytimes bestseller',
            schedule_interval=timedelta(days=1),)

run_etl = PythonOperator(
    task_id='nytimes_bestseller_etl',
    python_callable=run_nytimes_best_seller_etl,
    dag=dag
)

if run_etl > 1:
    print("Report is Updated with the New Best Sellers.")
else:
    print("Report is not updated as the data is not updated.")
    