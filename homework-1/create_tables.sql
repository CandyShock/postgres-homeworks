-- SQL-команды для создания таблиц
CREATE TABLE orders
(
	order_id varchar(100) PRIMARY KEY UNIQUE,
	customer_id varchar(100),
	employee_id int,
	order_date date,
	ship_city varchar(100)

)

CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY UNIQUE REFERENCES orders(order_id),
	company_name varchar(100) NOT NULL,

	contact_name varchar(100) NOT NULL

)

CREATE TABLE employess
(
	first_name varchar(100) PRIMARY KEY,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date  date,
	notes text

)

