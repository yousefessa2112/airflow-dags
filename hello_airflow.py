from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='hello_airflow',
    start_date=datetime(2025, 7, 30),
    schedule='@daily',
    catchup=False,
) as dag:
    task = BashOperator(
        task_id='say_hello',
        bash_command='echo "Hello from Airflow!"'
    )
