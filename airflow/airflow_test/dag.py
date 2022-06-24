from airflow import DAG
import dagfactory

dag_factory = dagfactory.DagFactory(r"C:\Users\matheus\Documents\Codigos\GIT\portifolio\python\airflow_service\dags\config_file.yml")

dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())