from .views import (
    get_all_orders, robot_serial_is_available, send_email_to_customer
)
from xls_export.views import create_xls


def check_robot_serial_for_email():
    orders = get_all_orders()
    for order in orders:
        robot = robot_serial_is_available(order.robot_serial)
        if robot:
            send_email_to_customer(order.customer.email, robot)


def create_xls_and_upload():
    print('Выгружаем в excel')
    create_xls()

