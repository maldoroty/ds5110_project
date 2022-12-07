use streaming_service_db;

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
INSERT INTO subscription_plan VALUES("Daily", 1.99);
INSERT INTO subscription_plan VALUES("Weekly", 4.99);
INSERT INTO subscription_plan VALUES("Monthly", 6.99);
INSERT INTO subscription_plan VALUES("Quarterly", 19.99);
INSERT INTO subscription_plan VALUES("Half Yearly", 35.99);
INSERT INTO subscription_plan VALUES("Yearly", 72.00);
INSERT INTO subscription_plan VALUES("Family Month", 8.99);
INSERT INTO subscription_plan VALUES("Family Year", 80.00);
INSERT INTO subscription_plan VALUES("Giant Family Month", 12.99);
INSERT INTO subscription_plan VALUES("Giant Family Year", 99.99);

-- inserting 10 rows into subscription plan
-- "YYYY-MM-DD"
INSERT INTO subscription VALUES(default, "2014-03-10", "2024-03-10", 1, "Giant Family Year");
INSERT INTO subscription VALUES(default, "2016-04-14", "2018-06-16", 2, "Giant Family Month");
INSERT INTO subscription VALUES(default, "2020-02-01", "2021-01-29", 3, "Yearly");
INSERT INTO subscription VALUES(default, "2015-07-04", "2023-05-21", 4, "Monthly");
INSERT INTO subscription VALUES(default, "2019-10-09", "2020-01-16", 5, "Weekly");
INSERT INTO subscription VALUES(default, "2022-09-29", "2023-03-27", 6, "Half Yearly");
INSERT INTO subscription VALUES(default, "2022-11-02", "2024-07-12", 7, "Quarterly");
INSERT INTO subscription VALUES(default, "2021-08-23", "2025-08-23", 8, "Family Month");
INSERT INTO subscription VALUES(default, "2017-01-06", "2026-01-05", 9, "Family Year");
INSERT INTO subscription VALUES(default, "2022-12-03", "2022-12-08", 10, "Daily");

-- inserting 10 rows into trending_list
INSERT INTO trending_list VALUES(default, 2);
INSERT INTO trending_list VALUES(default, 3);
INSERT INTO trending_list VALUES(default, 6);
INSERT INTO trending_list VALUES(default, 8);
INSERT INTO trending_list VALUES(default, 1);
INSERT INTO trending_list VALUES(default, 9);
INSERT INTO trending_list VALUES(default, 4);
INSERT INTO trending_list VALUES(default, 5);
INSERT INTO trending_list VALUES(default, 10);
INSERT INTO trending_list VALUES(default, 7);

-- inserting 10 rows into soundtracks
INSERT INTO soundtracks VALUES(default, "John Williams", "Obi-Wan", 1);
INSERT INTO soundtracks VALUES(default, "Nicholas Britell", "Just Look Up", 2);
INSERT INTO soundtracks VALUES(default, "Luis Bacalov", "Django Theme Song", 3);
INSERT INTO soundtracks VALUES(default, "Amdrei Shulgach", "First Lady", 4);
INSERT INTO soundtracks VALUES(default, "Frederic Chopin", "Nocturne No. 5", 5);
INSERT INTO soundtracks VALUES(default, "Randy Newman", "You've got a Friend in Me", 6);
INSERT INTO soundtracks VALUES(default, "Fela Kuti", "Black Man's Cry", 7);
INSERT INTO soundtracks VALUES(default, "Kendrick Lamar", "All the Stars", 8);
INSERT INTO soundtracks VALUES(default, "Luciano Michelini", "Frolic", 9);
INSERT INTO soundtracks VALUES(default, "Suzanne Collins", "The Hanging Tree", 10);


-- inserting 10 rows into recently_added
INSERT INTO recently_added VALUES(1, "2013-01-01");
INSERT INTO recently_added VALUES(2, "2014-04-15");
INSERT INTO recently_added VALUES(3, "2016-06-20");
INSERT INTO recently_added VALUES(4, "2015-10-30");
INSERT INTO recently_added VALUES(5, "2018-12-06");
INSERT INTO recently_added VALUES(6, "2020-09-28");
INSERT INTO recently_added VALUES(7, "2021-07-10");
INSERT INTO recently_added VALUES(8, "2021-11-14");
INSERT INTO recently_added VALUES(9, "2022-02-19");
INSERT INTO recently_added VALUES(10, "2022-08-24");

-- inserting 10 rows into leaving_soon
INSERT INTO leaving_soon VALUES(1, "2019-06-30");
INSERT INTO leaving_soon VALUES(2, "2020-07-15");
INSERT INTO leaving_soon VALUES(3, "2022-03-24");
INSERT INTO leaving_soon VALUES(4, "2021-05-10");
INSERT INTO leaving_soon VALUES(5, "2024-04-02");
INSERT INTO leaving_soon VALUES(6, "2026-01-09");
INSERT INTO leaving_soon VALUES(7, "2027-08-11");
INSERT INTO leaving_soon VALUES(8, "2027-09-23");
INSERT INTO leaving_soon VALUES(9, "2028-11-30");
INSERT INTO leaving_soon VALUES(10, "2028-12-17");


-- inserting 10 rows into production_company
INSERT INTO production_company VALUES(default, "Disney", 1);
INSERT INTO production_company VALUES(default, "Hyperobject Industries", 2);
INSERT INTO production_company VALUES(default, "Columbia Pictures", 3);
INSERT INTO production_company VALUES(default, "Showtime", 4);
INSERT INTO production_company VALUES(default, "Columbia Pictures", 5);
INSERT INTO production_company VALUES(default, "Disney", 6);
INSERT INTO production_company VALUES(default, "Universal", 7);
INSERT INTO production_company VALUES(default, "Disney", 8);
INSERT INTO production_company VALUES(default, "HBO", 9);
INSERT INTO production_company VALUES(default,  "Lionsgate", 10);

-- inserting 10 rows into contract
INSERT INTO contract VALUES(default, 1, 100000);
INSERT INTO contract VALUES(default, 2, 50000);
INSERT INTO contract VALUES(default, 3, 1000000);
INSERT INTO contract VALUES(default, 4, 250000);
INSERT INTO contract VALUES(default, 5, 750000);
INSERT INTO contract VALUES(default, 6, 500000);
INSERT INTO contract VALUES(default, 7, 300000);
INSERT INTO contract VALUES(default, 8, 950000);
INSERT INTO contract VALUES(default, 9, 600000);
INSERT INTO contract VALUES(default, 10, 450000);

-- inserting 10 rows into movies watched
INSERT INTO watched VALUES(2, 7);
INSERT INTO watched VALUES(9, 1);
INSERT INTO watched VALUES(6, 8);
INSERT INTO watched VALUES(10, 5);
INSERT INTO watched VALUES(4, 3);
INSERT INTO watched VALUES(2, 1);
INSERT INTO watched VALUES(3, 4);
INSERT INTO watched VALUES(5, 10);
INSERT INTO watched VALUES(8, 7);
INSERT INTO watched VALUES(6, 3)