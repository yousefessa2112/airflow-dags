from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.timetables.interval import CronDataIntervalTimetable
from datetime import datetime

with DAG(
    dag_id='example_dag',
    timetable=CronDataIntervalTimetable("0 0 * * *", timezone="UTC"),
    start_date=datetime(2025, 8, 1),
    catchup=False,
) as dag:
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")
    start >> end
