"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def read_csv(data):
    """Распаковка словарей в список"""
    with open(f'{data}.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        a = []
        for i in reader:
            a.append(i)
        return a


"""Переменные для распаковки"""
data = 'customers_data'
data1 = 'employees_data'
data2 = 'orders_data'


def main():
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='fallout4')
    data_ = read_csv(data)
    data_1 = read_csv(data1)
    data_2 = read_csv(data2)

    with conn:
        cursor = conn.cursor()
        for i in data_:
            cursor.execute(
                f'INSERT INTO customers(customer_id, company_name, contact_name) VALUES (%s, %s, %s)',
                (i["customer_id"], i["company_name"], i["contact_name"]))

        for i in data_1:
            cursor.execute(
                f'INSERT INTO employees(first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s)',
                (i["first_name"], i["last_name"], i["title"], i["birth_date"], i["notes"]))

        for i in data_2:
            cursor.execute(
                f'INSERT INTO orders(order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)',
                (i["order_id"], i["customer_id"], i["employee_id"], i["order_date"], i["ship_city"]))


if __name__ == '__main__':
    main()
