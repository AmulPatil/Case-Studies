from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import data_collection

default_args = {
    'owner': 'default_admin',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'api_to_mysql_dag',
    default_args=default_args,
    description='Fetch data from API and insert into MySQL daily',
    schedule_interval=timedelta(days=1),
)

fetch_and_insert_task = PythonOperator(
    task_id='fetch_and_insert_data_into_MYSQL',
    python_callable=fetch_and_insert_data,
    dag=dag,
)

fetch_and_insert_task
