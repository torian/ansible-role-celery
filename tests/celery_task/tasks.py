from celery import Celery

app = Celery('tasks', broker='redis://localhost')

@app.task
def add(x, y):
  return x + y

# vi:ts=2:sw=2:et
