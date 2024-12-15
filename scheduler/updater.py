from apscheduler.schedulers.background import BackgroundScheduler
from .update import check_robot_serial_for_email


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_robot_serial_for_email, 'interval', minutes=1)
    scheduler.start()
