
import sys,os
import logging
def my_scheduled_job():
    
    logging.info("This is a scheduled job")
    from .models import MyModel
    val = MyModel.objects.create(name="Scheduled Job", description="This is a scheduled job")
    logging.info(f"Created a new record with id: {val.id}")
    logging.info("Scheduled job completed")
    print_execution_env_info()
    
def print_execution_env_info():
    logging.info(f"Current working directory: {os.getcwd()}")
    logging.info(f"Python version: {sys.version}")
    logging.info(f"Python path: {sys.path}")
    logging.info(f"Python executable: {sys.executable}")
    logging.info(f"Python prefix: {sys.prefix}")
    logging.info(f"Python platform: {sys.platform}")
    logging.info(f"Python version info: {sys.version_info}")
    logging.info(f"Python implementation: {sys.implementation}")
    logging.info(f"Python build info: {sys.version_info}")
    # all environment variables
    logging.info(f"Environment variables: {os.environ}")
    