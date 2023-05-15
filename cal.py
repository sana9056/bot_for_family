import openpyxl
import datetime


def get_date_birth():
    # Открываем файл Excel с календарем
    wb = openpyxl.load_workbook('calendar.xlsx')
    ws = wb.active

    # Список для др
    list_date = []

    # Получаем текущую дату
    today = datetime.date.today()

    # Определяем дату начала и конца периода (1 месяц от текущей даты)
    start_date = today.replace(day=1)
    if today.month == 12:
        end_date = today.replace(year=today.year+1, month=1, day=1)
    else:
        end_date = today.replace(month=today.month+1, day=1)

    # Проходим по всем строкам таблицы календаря
    for row in ws.iter_rows(min_row=1):
        # Получаем дату из ячейки "День рождения"
        bday = row[1].value
        # Проверяем, что дата не является пустой и находится в заданном периоде
        if bday is not None:
            bday_month_day = datetime.date(today.year, bday.month, bday.day)
            if start_date <= bday_month_day < end_date:
                # Получаем имя из ячейки "Имя"
                name = row[0].value
                # Записываем имя и дату рождения
                list_date.append(f'{name}: {bday.strftime("%d.%m")}')

    return list_date

print(get_date_birth())
