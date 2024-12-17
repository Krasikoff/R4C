import datetime

import xlwt
from django.db.models import Count
from django.http import HttpResponse
from django.utils import timezone

from robots.models import Robot


def export_robots_xls(request):
    """Экспорт в Exel произведенных за прошлую неделю роботов."""
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = (
        'attachment; filename="Last_Week_Made_Robots.xls"'
    )
    wb = xlwt.Workbook(encoding='utf-8')
    today = timezone.now()
    weekday = today.weekday()
    start_delta = datetime.timedelta(days=weekday, weeks=1)
    start_of_week = today - start_delta
    rows = Robot.objects.all().values_list(
        'serial', 'model', 'version').order_by(
        'serial').annotate(count=Count('serial')).filter(
            created__range=(start_of_week, today)
            )
    model = ''
    for row in rows:
        if model != row[1]:
            ws = wb.add_sheet(f'Модель {row[1]}')
            model = row[1]
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['Модель', 'Версия', 'Количество за неделю', ]
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()
        row_num += 1
        for col_num in range(len(row)):
            if col_num:
                ws.write(row_num, col_num - 1, row[col_num], font_style)
    wb.save(response)
    return response
