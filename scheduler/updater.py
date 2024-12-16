from apscheduler.schedulers.background import BackgroundScheduler
from .update import check_robot_serial_for_email, create_xls_and_upload()


def start():
    scheduler = BackgroundScheduler()
#    scheduler.add_job(check_robot_serial_for_email, 'interval', minutes=1)
#    scheduler.add_job(create_xls_and_upload, 'interval', minutes=1)    
    scheduler.start()
