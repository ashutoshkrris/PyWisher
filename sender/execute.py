from .views import Task
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


scheduler.add_job(Task, 'interval', seconds=10)
scheduler.start()
