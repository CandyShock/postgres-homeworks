-- SQL-команды для создания таблиц
create table employees
(
    employee_id serial UNIQUE not null,
    first_name varchar(50) not null,
    last_name  varchar(50) not null,
    title      varchar(50) not null,
    birth_date   date        not null,
    notes      text
);
create table customers (
    customer_id varchar(10) UNIQUE not null,
    company_name varchar(100) not null,
    contact_name varchar(100) not null
);
create table orders (
    order_id serial UNIQUE not null,
    customer_id varchar(10) references customers(customer_id),
    employee_id int not null references employees(employee_id),
    order_date date not null,
    ship_city varchar(50)

);
)

