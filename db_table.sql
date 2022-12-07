CREATE TABLE customer(
	customer_id int primary key auto_increment,
    name varchar(20) not null,
    email varchar(30) not null,
    username varchar(20) unique,
    password varchar(20) check (length(password) > 7),
    credit_card int unique
);

CREATE TABLE genre(
	g_id int primary key auto_increment,
    genre_name varchar(10) not null
);

CREATE TABLE actors(
	a_id int primary key auto_increment,
    name varchar(20) not null,
    ranks int
);

CREATE TABLE directors(
	d_id int primary key auto_increment,
    name varchar(20) not null,
    ranks int
);

CREATE TABLE media(
	m_id int primary key auto_increment,
    d_id int,
    a_id int,
    title varchar(20) not null,
    type varchar(20) not null,
    g_id int,
    foreign key (d_id) references directors(d_id)
		on delete cascade,
	foreign key (a_id) references actors(a_id)
		on delete cascade,
	foreign key (g_id) references genre(g_id)
		on delete cascade
);

CREATE TABLE rating(
	m_id int,
    rating decimal(2, 1) not null,
    primary key (m_id),
    foreign key (m_id) references media(m_id)
		on delete cascade    
);

CREATE TABLE subscription_plan(
	s_type varchar(20) primary key not null,
    price decimal(4, 2) not null
);

CREATE TABLE subscription(
	s_id int primary key auto_increment,
    start_sub date,
    end_sub date,
    customer_id int,
    s_type varchar(20),
    foreign key (customer_id) references customer(customer_id)
		on delete cascade,
	foreign key (s_type) references subscription_plan(s_type)
		on delete cascade
);

CREATE TABLE trending_list(
	ranks int primary key auto_increment,
    m_id int, 
    foreign key (m_id) references media(m_id)
		on delete cascade
);

CREATE TABLE soundtracks(
	st_id int primary key auto_increment,
	composer varchar(20) not null,
    title varchar(40) not null,
	m_id int,
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
	p_id int primary key auto_increment,
	name varchar(40) not null,
	m_id int,
    foreign key (m_id) references media(m_id)
		on delete cascade
);

CREATE TABLE contract(
	contract_id int primary key auto_increment,
	p_id int,
	amount int,
    foreign key (p_id) references production_company(p_id)
		on delete cascade
);

CREATE TABLE watched(
	c_id int,
    m_id int,
    primary key (c_id, m_id),
    foreign key (c_id) references customer(customer_id),
    foreign key (m_id) references media(m_id)
);
    