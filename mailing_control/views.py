from smtplib import SMTPException

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from mailing_control.models import Sent_email
from orders.models import Order
from robots.models import Robot


def get_all_orders():
    """Получаются только заказы по которым еще не отправляли письма."""
    orders = Order.objects.all().select_related(
        'customer', 'sent_email').filter(sent_email__sent=None)
    return orders


def robot_serial_is_available(serial):
    """Проверяется наличие роботов."""
    robots = Robot.objects.filter(serial=serial)
    if robots:
        return robots[0]
    else:
        return None


def send_email_to_customer(order, robot):
    """Отправка письма, в случае удачи запись в отправленных."""
    text_content = render_to_string(
        template_name="emails/customer_email.txt",
        context={'X': robot.model, 'Y': robot.version},
    )
    email = EmailMessage(
        'Добрый день! По Вашему заказу...',
        text_content,
        'from@example.com',
        [order.customer.email.rstrip(),],
    )
    try:
        email.send()
        email = Sent_email.objects.create(order=order)
        email.save()
    except SMTPException as e:
        print('There was an error sending an email: ', e)
