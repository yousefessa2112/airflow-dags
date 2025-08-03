from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.timetables.interval import CronDataIntervalTimetable
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 7, 30),
}

with DAG(
    dag_id='hello_airflow',
    timetable=CronDataIntervalTimetable("0 0 * * *", timezone="UTC"),  # replaces schedule
    default_args=default_args,
    catchup=False,
) as dag:
    task1 = BashOperator(
        task_id='say_hello',
        bash_command='echo "Hello from Airflow!"'
    )
