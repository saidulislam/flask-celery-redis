import os
import time

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_task")
def create_task(task_type):
    # time.sleep(int(task_type) * 10)

    my_json_val = """
    {
        "eBooks":[
            {
                "language":"Pascal",
                "edition":"third"
            },
            {
                "language":"Python",
                "edition":"four"
            },
            {
                "language":"SQL",
                "edition":"second"
            }
        ]
    }
    """

    # Writing to file
    with open("/usr/src/app/myfile.txt", "w") as file1:
        # Writing data to a file
        print(my_json_val)
        file1.write(my_json_val)
    return True
