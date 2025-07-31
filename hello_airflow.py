from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 7, 30),
}

with DAG('hello_airflow', schedule='@daily', default_args=default_args, catchup=False) as dag:
    task1 = BashOperator(
        task_id='say_hello',
        bash_command='echo "Hello from Airflow!"'
    )
