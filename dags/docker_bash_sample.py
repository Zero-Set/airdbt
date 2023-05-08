from airflow import models
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
DAG_ID = "docker_test"
TEST_CONN_ID = "docker_test_connection"
# これがよくわからない。
TEST_DOCKER_URL = "tcp://docker-proxy:2375"
TEST_IMAGE = "python:3.9"

with models.DAG(
    DAG_ID,
    schedule="@once",
    start_date = datetime(2023,5,7),
    tags = ["example"]
) as dag:
    op = DockerOperator(
        image = TEST_IMAGE,
        network_mode = "bridge",
        task_id = "docker_bash_sample",
        command = 'echo "command"',
        # とりあえずfalseにすべき
        mount_tmp_dir = False,
        dag = dag
    ) 