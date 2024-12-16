from smtplib import SMTPException
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from orders.models import Order
from robots.models import Robot


def get_all_orders():
    orders = Order.objects.all().select_related('customer')
    return orders


def robot_serial_is_available(serial):
    robots = Robot.objects.filter(serial=serial)
    if robots:
        return robots[0]
    else:
        return None


def send_email_to_customer(customer_email, robot):
    text_content = render_to_string(
        template_name="emails/customer_email.txt",
        context={'X': robot.model, 'Y': robot.version},
    )
    email = EmailMessage(
        'Добрый день! По Вашему заказу...',
        text_content,
        'from@example.com',
        [customer_email.rstrip(),],
    )
    try:
        email.send()
    except SMTPException as e:
        print('There was an error sending an email: ', e)
