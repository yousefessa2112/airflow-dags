from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="example_dag",
    start_date=datetime(2023, 1, 1),
    schedule='@daily',
    catchup=False,
) as dag:
    task1 = BashOperator(
        task_id='start_task',
        bash_command='echo "Start Task Running"'
    )

    task2 = BashOperator(
        task_id='end_task',
        bash_command='echo "End Task Running"'
    )

    task1 >> task2
