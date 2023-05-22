"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def read_csv(data):
    empty_list = []
    with open(f'{data}.csv', 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=',')
        for line in file_reader:
            empty_list.append(line)

    return empty_list


data = 'customers_data'
data1 = 'employees_data'
data2 = 'orders_data'
print(read_csv(data))


def main():
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='fallout4')
    data_ = read_csv(data)
    data_1 = read_csv(data1)
    data_2 = read_csv(data2)
    with conn:
        cursor = conn.cursor()
        for item in data_[1:]:
              cursor.execute(
                  f"INSERT INTO customers (customer_id, company_name, contact_name) VALUES('{item[0]}', '{item[1]}', '{item[2]}')")

        for item in data_1[1:]:
             cursor.execute(
                 f"INSERT INTO employess (first_name, last_name, title, birth_date, notes) VALUES('{item[0]}', '{item[1]}', '{item[2]}', '{item[3]}', '{item[4]}')")

        for item in data_2[1:]:
            cursor.execute(f"INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES('{item[0]}', '{item[1]}', '{item[2]}', '{item[3]}', '{item[4]}')")


if __name__ == '__main__':
    main()
