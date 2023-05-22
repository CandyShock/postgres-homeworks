-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
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
CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id int,
	employee_id varchar(100),
	order_date date,
	ship_city varchar(100)

)