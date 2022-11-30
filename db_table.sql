use streaming_service_db;

CREATE TABLE customer(
	customer_id int primary key,
    name varchar(20) not null,
    email varchar(30) not null,
    username varchar(10) not null,
    password varchar(10) not null,
    credit_card int
);

CREATE TABLE actors(
	a_id int primary key,
    name varchar(20) not null,
    ranks int
);

CREATE TABLE directors(
	d_id int primary key,
    name varchar(20) not null,
    ranks int
);

CREATE TABLE media(
	m_id int primary key,
    d_id int,
    a_id int,
    title varchar(20) not null,
    type varchar(20) not null,
    average_rating int,
    genre_name varchar(10) not null,
    runtime int,
    rate_times int,
    foreign key (d_id) references directors(d_id)
		on delete cascade,
	foreign key (a_id) references actors(a_id)
		on delete cascade
);

CREATE TABLE rating(
	a_id int,
    name varchar(20) not null,
    ranks int,
    primary key (a_id),
    foreign key (a_id) references actors(a_id)
		on delete cascade    
);

CREATE TABLE genre(
	g_id int primary key,
    genre_name varchar(10) not null,
    num_plays int
);

CREATE TABLE subscription_plan(
	s_type varchar(20) not null,
    price varchar(10) not null,
    length decimal(4, 2)
);

CREATE TABLE trending_list(
	m_id int,
    title varchar(20) not null,
    ranks int
);

CREATE TABLE soundtracks(
	st_id int primary key,
    m_id int,
    title varchar(20) not null,
    foreign key (m_id) references media(m_id)
		on delete cascade  
);

CREATE TABLE recently_added(
	m_id int,
    add_date date,
    primary key (m_id),
    foreign key (m_id) references media(m_id)
		on delete cascade 
);

CREATE TABLE leaving_soon(
	m_id int,
    removal_date date,
    primary key (m_id),
    foreign key (m_id) references media(m_id)
		on delete cascade
);

CREATE TABLE production_company(
	p_id int primary key,
	name varchar(20) not null,
	m_id int,
    foreign key (m_id) references media(m_id)
		on delete cascade
);

CREATE TABLE contract(
	contract_id int primary key,
	name varchar(20) not null,
    length int,
    add_date date,
    removal_date date,
	amount int
);