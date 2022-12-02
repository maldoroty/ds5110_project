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
    g_id int,
    foreign key (d_id) references directors(d_id)
		on delete cascade,
	foreign key (a_id) references actors(a_id)
		on delete cascade
);

CREATE TABLE rating(
	m_id int,
    rating decimal(2, 1) not null,
    primary key (m_id),
    foreign key (m_id) references media(m_id)
		on delete cascade    
);

CREATE TABLE genre(
	g_id int primary key auto_increment,
    genre_name varchar(10) not null
);

CREATE TABLE subscription_plan(
	s_type varchar(20) primary key not null,
    price decimal(4, 2) not null,
    length int
);

CREATE TABLE subscription(
	s_id int primary key auto_increment,
    start_sub date,
    end_sub date,
    customer_id int,
    foreign key (customer_id) references customer(customer_id)
		on delete cascade 
);

CREATE TABLE trending_list(
	ranks int primary key,
    title varchar(20) not null,
    m_id int, 
    foreign key (m_id) references media(m_id)
		on delete cascade
);

CREATE TABLE soundtracks(
	st_id int primary key auto_increment,
    title varchar(20) not null,
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
INSERT INTO actors VALUES(default, "Larry David", 9);
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

-- inserting 10 rows into genre 
INSERT INTO genre VALUES(default, "Adventure");
INSERT INTO genre VALUES(default, "Drama");
INSERT INTO genre VALUES(default, "Western");
INSERT INTO genre VALUES(default, "History");
INSERT INTO genre VALUES(default, "Romance");
INSERT INTO genre VALUES(default, "Animation");
INSERT INTO genre VALUES(default, "Horror");
INSERT INTO genre VALUES(default, "Action");
INSERT INTO genre VALUES(default, "Comedy");
INSERT INTO genre VALUES(default, "Sci-Fi");

-- inserting 10 rows into media
INSERT INTO media VALUES(default, 4, 1, "Obi-Wan Kenobi", "TV Show", 1);
INSERT INTO media VALUES(default, 1, 3, "Don't Look Up", "Movie", 2);
INSERT INTO media VALUES(default, 2, 2, "Django Unchained", "Movie", 3);
INSERT INTO media VALUES(default, 3, 10, "The First Lady", "TV Show", 4);
INSERT INTO media VALUES(default, 5, 4, "Little Women", "Movie", 5);
INSERT INTO media VALUES(default, 6, 5, "Toy Story 4", "Movie", 6);
INSERT INTO media VALUES(default, 7, 8, "Beast", "Movie", 7);
INSERT INTO media VALUES(default, 8, 6, "Black Panther", "Movie", 8);
INSERT INTO media VALUES(default, 10, 9, "Curb Your Enthusiasm", "TV Show", 9);
INSERT INTO media VALUES(default, 9, 7, "The Hunger Games", "Movie", 10);

-- inserting 10 rows into rating
INSERT INTO rating VALUES(1, 7.1);
INSERT INTO rating VALUES(2, 7.2);
INSERT INTO rating VALUES(3, 8.4);
INSERT INTO rating VALUES(4, 7.1);
INSERT INTO rating VALUES(5, 7.8);
INSERT INTO rating VALUES(6, 7.7);
INSERT INTO rating VALUES(7, 5.6);
INSERT INTO rating VALUES(8, 7.3);
INSERT INTO rating VALUES(9, 8.8);
INSERT INTO rating VALUES(10, 6.6);

-- inserting 10 rows into subscription plan
INSERT INTO subscription_plan VALUES("Rental", 3.00);
INSERT INTO subscription_plan VALUES("One week", 4.99);
INSERT INTO subscription_plan VALUES("One month", 6.99);
INSERT INTO subscription_plan VALUES("One year", 72.00);
INSERT INTO subscription_plan VALUES("Family Month", 8.99);
INSERT INTO subscription_plan VALUES("Family Year", 80.00);
INSERT INTO subscription_plan VALUES("Giant Family Month", 12.99);
INSERT INTO subscription_plan VALUES("Giant Gamily Year", 99.99);
