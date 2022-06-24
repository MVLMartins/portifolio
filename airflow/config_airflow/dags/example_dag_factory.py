from airflow import DAG
import dagfactory

root_folder = "/opt/airflow/dags/templates"

configsFiles = [f"{root_folder}/example_customize_operator.yml", 
                # f"{root_folder}/example_dag_factory.yml", 
                # f"{root_folder}/example_dag_factory2.yml"
                # f"{root_folder}/template_stress.yml"
                ]

for file in configsFiles:
    example_dag_factory = dagfactory.DagFactory(config_filepath = file)
    example_dag_factory.clean_dags(globals())
    example_dag_factory.generate_dags(globals())



