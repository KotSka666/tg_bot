import sqlite3
from datetime import datetime, date, time

def get_recorts_day():
    try:
        sqlite_connection = sqlite3.connect('Check_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        cursor.execute("SELECT COALESCE(SUM(summa), 0) AS total_sum FROM Unusual_checks WHERE data BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime')")
        summa = cursor.fetchall()
        summ1 = float(0)
        for i in summa:
            summ1 += float(i[0])
        cursor.execute("SELECT COALESCE(SUM(summa), 0) AS total_sum FROM usual_checks WHERE data BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime')")
        summa = cursor.fetchall()
        summ2 = float(0)
        for i in summa:
            summ2 += float(i[0])
        return summ1, summ2, summ1 + summ2
    except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def get_recorts_week():
    try:
        sqlite_connection= sqlite3.connect('Check_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        cursor.execute("SELECT SUM(summa) FROM unusual_checks WHERE data BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') ")
        summa = cursor.fetchall()
        summ1 = int(0)
        for i in summa:
            summ1 += int(i[0])
        cursor.execute("SELECT SUM(summa) FROM usual_checks WHERE data BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') ")
        summa = cursor.fetchall()
        summ2 = int(0)
        for i in summa:
            summ2 += int(i[0])
        return summ1, summ2, summ1 + summ2
    except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def get_recorts_monch():
    try:
        sqlite_connection= sqlite3.connect('Check_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        cursor.execute("SELECT COALESCE(SUM(summa), 0) AS total_sum FROM unusual_checks WHERE data BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime')")
        summa = cursor.fetchall()
        summ1 = int(0)
        for i in summa:
            summ1 += int(i[0])
        cursor.execute("SELECT COALESCE(SUM(summa), 0) AS total_sum FROM usual_checks WHERE data BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime')")
        summa = cursor.fetchall()
        summ2 = int(0)
        for i in summa:
            summ2 += int(i[0])
        return summ1, summ2, summ1 + summ2
    except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def get_recorts_monchs():
    try:
        sqlite_connection = sqlite3.connect('Check_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        cursor.execute("SELECT SUM(summa) FROM unusual_checks WHERE data >= datetime(CURRENT_DATE, '-1 month', 'start of month')")
        summa = cursor.fetchall()
        summ1 = int(0)
        for i in summa:
            summ1 += int(i[0])
        cursor.execute("SELECT SUM(summa) FROM usual_checks WHERE data >= datetime(CURRENT_DATE, '-1 month', 'start of month')")
        summa = cursor.fetchall()
        summ2 = int(0)
        for i in summa:
            summ2 += int(i[0])
        return summ1, summ2, summ1 + summ2
    except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def get_recorts_year():
    try:
        sqlite_connection= sqlite3.connect('Check_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        cursor.execute("SELECT SUM(summa) FROM unusual_checks WHERE data BETWEEN datetime('now', 'start of year') AND datetime('now', 'localtime') ")
        summa = cursor.fetchall()
        summ1 = int(0)
        for i in summa:
            summ1 += int(i[0])
        cursor.execute("SELECT SUM(summa) FROM usual_checks WHERE data BETWEEN datetime('now', 'start of year') AND datetime('now', 'localtime') ")
        summa = cursor.fetchall()
        summ2 = int(0)
        for i in summa:
            summ2 += int(i[0])
        return summ1, summ2, summ1 + summ2
    except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def get_recorts_all():
    try:
        sqlite_connection = sqlite3.connect('Check_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        cursor.execute("SELECT SUM(summa) FROM unusual_checks")
        summa = cursor.fetchall()
        summ1 = int(0)
        for i in summa:
            summ1 += int(i[0])
            print(f"Общая сумма Ч: {summ1} ")
        cursor.execute("SELECT SUM(summa) FROM usual_checks")
        summa = cursor.fetchall()
        summ2 = int(0)
        for i in summa:
            summ2 += int(i[0])
            print(f"Общая сумма П: {summ2}")
        print(f'"Общая сумма Ч+П:" {summ1 + summ2}')
        return summ1, summ2, summ1 + summ2
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

# get_recorts_day()
# get_recorts_week()
# get_recorts_monch()
# get_recorts_year()
# get_recorts_all()