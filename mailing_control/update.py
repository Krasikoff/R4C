from .views import (get_all_orders, robot_serial_is_available,
                    send_email_to_customer)


def check_robot_serial_for_email():
    """Проверка наличия желанного заказа(робота)
    и отправка письма заказчику в случае успеха."""
    orders = get_all_orders()
    for order in orders:
        robot = robot_serial_is_available(order.robot_serial)
        if robot:
            send_email_to_customer(order, robot)
