from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="new_hello_airflow",
    start_date=datetime(2025, 8, 1),
    schedule="@hourly",
    catchup=False,
) as dag:
    bash_task = BashOperator(
        task_id="bash_hello_task",
        bash_command='echo "This is a brand new hello from Airflow!"',
    )
