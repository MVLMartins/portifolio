from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import functools

from tasks_function_utils.lazzy_task_42 import lazzy_function, lazzy_function_2

def print_hello():
    return 'Hello world from first Airflow DAG!'

dag = DAG('lazzy_test_317', description='Hello World DAG',
          schedule_interval='@once',
          start_date=datetime(2017, 3, 20), catchup=False)

hello_operator = PythonOperator(task_id='lazzy_function', python_callable=lazzy_function, dag=dag)

hello_operator
