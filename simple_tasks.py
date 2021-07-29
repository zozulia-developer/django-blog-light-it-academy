from celery import Celery

app = Celery(
    'tasks',
    # broker='redis://localhost',
    # backend='redis://localhost'
)
# app.conf.update(
#     task_serializer='json',
#     result_serializer='json',
# )

app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    return x + y


@app.task
def long(x, y):
    import time
    time.sleep(10)
    return x + y


@app.task
def class_task(cls):
    print(cls)


# @app.on_after_configure.connect
# def setup(sender, **kwargs):
#     sender.add_periodic_task(5, add.s(2, 2), name='add every 5 sec')
