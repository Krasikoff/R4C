# Task 3. От клиента компании. Рассылка писем о возможности получения заказа.

APScheduler установлен в приложение scheduler. Чтобы не было двойного срабатывания APScheduler запускать нужно:
Частота 1 мин в schedule/updater. 

```shell
python manage.py runserver --noreload
```

Отправка писем и отслеживание отправления в mailing_control.
