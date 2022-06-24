import time
import uuid



def lazzy_function():

    uuid_gerado = uuid.uuid4()
    uuid_gerado = str(uuid_gerado)

    root_folder = "/opt/airflow/dags"
    file = f"{root_folder}/logs_python/teste.txt"

    with open(file, 'a') as f:
        f.write(f"Id gerado = {uuid_gerado}\n")

    max_range = 500

    for i in range(max_range):
        print(f'{i + 1 } seconds')
        with open(file, 'a') as f:
            f.write(f"Contando: {i} / {max_range}\n")
        time.sleep(1)

    return "funfou"