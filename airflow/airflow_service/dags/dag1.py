from airflow import DAG
import dagfactory
import glob


list_dags = glob.glob('/opt/airflow/dags/config_file*.yml')

for dag in list_dags:
    dag_factory = dagfactory.DagFactory(dag)
    dag_factory.clean_dags(globals())
    dag_factory.generate_dags(globals())