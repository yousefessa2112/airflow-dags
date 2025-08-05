from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, Airflow!")

with DAG(
    dag_id='hello_world_dag',
    start_date=datetime(2025, 8, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    task = PythonOperator(
        task_id='hello_task',
        python_callable=hello_world,
    )
