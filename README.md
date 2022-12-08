# DS5110 Final Project
by Hajera Siddiqui and Michael Aldoroty


Our database was designed to model a media streaming service, similar to Netflix, HBO, Hulu, and others. However, we chose to model it from the context of the administrative side. We want to be able to store different types of movies and TV shows that customers are watching. This was achieved by using mySQL to create a relational database of 15 different tables with four main components. The most important component was the media table, this held the bulk of the information regarding information about the movie or TV show. Connected to this media table were the other details needed such as genre, director, or actor.

## How to use
Before running our application, first install and run a MySQL database on `localhost` and use the SQL files in this repo to populate the data. After that, please install the following packages via `pip`:
- `tabulate`
- ` mysql-connector-python`

Now to run our application, navigate to where you have downloaded the project via the command line and enter the following command:
```bash
python App/python_app.py
```