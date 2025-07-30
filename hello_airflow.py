from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("🎉 Hello from Airflow!")

with DAG(
    dag_id='hello_airflow',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=["example"]
) as dag:

    task = PythonOperator(
        task_id='say_hello_task',
        python_callable=say_hello
    )
