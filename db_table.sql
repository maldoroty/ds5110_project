use streaming_service_db;

CREATE TABLE customer(
	customer_id int primary key,
    name varchar(20) not null,
    email varchar(30) not null,
    username varchar(10) not null,
    password varchar(10) not null,
    credit_card int
);