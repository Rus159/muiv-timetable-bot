'''
Unnamed 0: Дни недели
Unnamed 1: Дата
Unnamed 2: Время
Unnamed [3-n]: [1-(n-2)] группа
'''
import pandas as pd
import parse_link
import urllib
import logging

logging.basicConfig(format="%(levelname)s %(asctime)s %(message)s")

url = parse_link.parse()
filename = list(url.split('iblock/'))[1][4:]
urllib.request.urlretrieve(url, filename)
timetable = pd.ExcelFile(filename)
user_xls_association = {}
user_xls_file = []

def get_week_timetable(group, sheet):
    message = {}
    column = 'Unnamed: ' + str(int(list(group.split('.'))[1][0])+2)
    for i in range(18, len(sheet)-10, 12):
        lesson = {}
        for j in range(i, i + 12, 2):
            if type(sheet[column][j]).__name__ != 'float':
                lesson.update([(sheet['Unnamed: 2'][j], [sheet[column][j+1], sheet[column][j]])])
        message.update([(sheet['Unnamed: 0'][i], lesson)])
    return message


def excelFile():
    return pd.ExcelFile(filename)


def get_sheetnames(xls):
    return xls.sheet_names


def get_groupnames(sheet):
    groups = []
    for column in sheet.columns:
        if column[-1] not in '012':
            groups.append(sheet[column][15])
    return groups


def check_file_update():
    global url
    global filename
    if list(parse_link.parse().split('iblock/'))[1][4:] != filename:
        url = parse_link.parse()
        filename = list(url.split('iblock/'))[1][4:]
        print(filename)
        urllib.request.urlretrieve(url, filename)
        logging.info('Файл обновлен')
