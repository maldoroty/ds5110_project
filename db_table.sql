CREATE TABLE customer(
	customer_id int primary key auto_increment,
    name varchar(20) not null,
    email varchar(30) not null,
    username varchar(20) unique,
    password varchar(20) check (length(password) > 7),
    credit_card int unique
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
    average_rating int,
    g_id int,
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
	g_id int primary key auto_increment,
    genre_name varchar(10) not null,
    num_plays int
);

CREATE TABLE subscription_plan(
	s_id int primary key auto_increment,
	s_type varchar(20) not null,
    price decimal(4, 2) not null,
    length int
);

CREATE TABLE subscription(
	s_id int auto_increment,
    start_sub date,
    end_sub date,
    customer_id int,
    primary key (s_id, customer_id),
    foreign key (s_id) references subscription_plan(s_id)
		on delete cascade,
    foreign key (customer_id) references customer(customer_id)
		on delete cascade 
);

CREATE TABLE trending_list(
	m_id int,
    title varchar(20) not null,
    ranks int
);

CREATE TABLE soundtracks(
	st_id int primary key auto_increment,
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
-- inserting 10 rows into customer table
INSERT INTO customer VALUES(default, "Cooper", "cooper123@gmail.com", "coops1", "coopspass", 55558392);
INSERT INTO customer VALUES(default, "Alexander", "alexander@aol.com", "alexthegreat", "securepass", 55554920);
INSERT INTO customer VALUES(default, "Morgan", "morgan483@gmail.com", "morgan483", "qwertyuiop", 55559283);
INSERT INTO customer VALUES(default, "Elvis", "fakeelvis@aol.com", "notpresley", "kingofrock", 55554001);
INSERT INTO customer VALUES(default, "Patrick", "patrickstarr@nickelodean.com", "patrickstarr", "nothisispatrick", 55559483);
INSERT INTO customer VALUES(default, "Maggie", "mcgonagall@hogwarts.edu", "profmcgonagal", "thebestprof", 55557382);
INSERT INTO customer VALUES(default, "Stacie", "stacie830@gmail.com", "stacie830", "moviepass", 55554821);
INSERT INTO customer VALUES(default, "Christina", "christina0293@gmail.com", "christina0293", "applegate", 55556372);
INSERT INTO customer VALUES(default, "Allison", "allison9023@gmail.com", "allison9023", "allisonsdabomb", 55557483);
INSERT INTO customer VALUES(default, "Damien", "damien01283@aol.com", "damien0123", "damionion", 55550384);

-- inserting 10 rows into actors table
INSERT INTO actors VALUES(default, "Ewan McGregor", 1);
INSERT INTO actors VALUES(default, "Leonardo DiCaprio", 2);
INSERT INTO actors VALUES(default, "Meryl Streep", 3);
INSERT INTO actors VALUES(default, "Saoirse Ronan", 4);
INSERT INTO actors VALUES(default, "Tom Hanks", 5);
INSERT INTO actors VALUES(default, "Michael B. Jordan", 6);
INSERT INTO actors VALUES(default, "Jennifer Lawrence", 7);
INSERT INTO actors VALUES(default, "Idris Elba", 8);
INSERT INTO actors VALUES(default, "Woody Harrelson", 9);
INSERT INTO actors VALUES(default, "Viola Davis", 10);

-- inserting 10 rows into directors table
INSERT INTO directors VALUES(default, "Adam McKay", 4);
INSERT INTO directors VALUES(default, "Quentin Tarantino", 1);
INSERT INTO directors VALUES(default, "Susanne Bier", 5);
INSERT INTO directors VALUES(default, "Deborah Chow", 2);
INSERT INTO directors VALUES(default, "Greta Gerwig", 3);
INSERT INTO directors VALUES(default, "Josh Cooley", 6);
INSERT INTO directors VALUES(default, "Baltasar Kormakur", 7);
INSERT INTO directors VALUES(default, "Ryan Coogler", 8);
INSERT INTO directors VALUES(default, "Francis Lawrence", 9);
INSERT INTO directors VALUES(default, "Robert B. Wiede", 10);