from dagster import repository
from jobs.data_ingestion import data_ingestion
from schedules.data_ingestion_schedule import (
    data_ingestion_schedule,
)


@repository
def deploy_docker_repository():
    return [data_ingestion, data_ingestion_schedule]
