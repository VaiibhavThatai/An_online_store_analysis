from dagster import schedule

from jobs.data_ingestion import data_ingestion


@schedule(
    cron_schedule=" /2 * * * *", 
    job=data_ingestion, 
    execution_timezone="US/Central")
def data_ingestion_schedule(_context):
    """
    https://docs.dagster.io/overview/schedules-sensors/schedules
    """
    run_config = {}
    return run_config
