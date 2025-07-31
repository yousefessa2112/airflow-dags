from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

dag = DAG(
    dag_id="example_dag",
    start_date=datetime(2023, 1, 1),
    schedule='@daily',
    catchup=False,
)

start = EmptyOperator(task_id="start", dag=dag)
end = EmptyOperator(task_id="end", dag=dag)
start >> end
