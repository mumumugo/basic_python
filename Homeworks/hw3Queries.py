import psycopg2
class Queries():

    #HOMEWORK 3
    #All questions should be one query
    #Put your queries within the """

    #Ex:
    #      """
    #       Your query here
    #      """

    # For this homework we will be talking an gaming leaderboard system
    # The schema is provided below
    # Assume I have already populated the tables with data
    # All table names need to be exact!

    # CREATE TABLE users (user_id SERIAL PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), email VARCHAR(255));
    # CREATE TABLE games (game_id SERIAL PRIMARY KEY , game_name VARCHAR(255),high_score BIGINT);
    # CREATE TABLE user_scores (user_id INTEGER , game_id INTEGER, score BIGINT, FOREIGN KEY (user_id) REFERENCES users (user_id), FOREIGN KEY(game_id) REFERENCES games (game_id));


    def insert_data(self):
    #Question 1:
        # Insert at least 2 users, 3 new games, and 5 user_scores
        # You are allowed to submit more than 1 query
        return """
        INSERT INTO users (username, password, email) VALUES ('pe3', 'rkrkdldl22', 'pe3@gmail.com'), ('pe4', 'rkrkdldl24', 'pe4@gmail.com'), ('pe5', 'rkrkdldl25', 'pe5@gmail.com');
        INSERT INTO games (game_name, high_score) VALUES ('blackdesrt', '720'), ('amongus', '720'), ('LOL', '720'), ('PUBG', '720');
        INSERT INTO user_scores (user_id, game_id, score) VALUES  ('1','2', '772'), ('2','3', '685'),('4','5', '695'), ('6','7', '772'), ('8','9', '711');
            """

    def fortnite(self):
    #Question 2:
        # I'm looking to build a e-sports team, for my inital scouting reports i want to check out the highscore holders
        # My company is looking to form a e-sports team for the game "Fortnite"
        # I would like to contact the high_score holder for the game "Fortnite" to see if they're interested in joining
        # Write a query that will return the email for the user who holds the high score for "Fortnite"
        return """
        SELECT email FROM users WHERE user_id IN (SELECT user_id FROM user_scores WHERE game_id IN (SELECT game_id FROM games WHERE game_name = 'Fortnite' AND high_score > ANY (SELECT high_score FROM games)));
            """

    def popularity(self):
    #Question 3:
        # I want to scout out what the most popular games are
        # To measure if a game is popular, i want to see how many submitted scores are associated with each game
        # The more submissions (rows found) for a game the more popular i assume it is
        # Write a query that will return the name of the game(s) that are most popular
        return """

        SELECT DISTINCT game_name FROM games WHERE game_id IN (SELECT game_id FROM user_scores WHERE score LIMIT 1);

            """


    def leaderboards(self):
    #Question 4:
        # I now want to view the top 3 players within the entire system
        # The top 3 players are considered to be those users who's scores when summed up are the highest 3
        # Write a query to return the username and emails of the top 3 players
        return """
        SELECT username,email FROM users WHERE user_id IN (SELECT  FROM )
            """


    def dedicated_players(self):
    #Question 5:
        # What a good team needs are dedicated players
        # With the data we are given, we will measure if a player is dedicated if their username contains a listed game in the system
        # Ex) fortniter22 is considered a dedicated player since their username contains the game name "Fortnite", also note the search should be case insensitive
        # Write a query that will return all usernames and emails of "dedicated players"
        return """
        user -> game
        SUBQUERIS

            """


    def emails(self):
    #Question 6:
        # We want to gather more information to form our e-sports team.
        # To do this we're looking at contacting the companys that the users in this database use the most
        # Write a query to extract the top 5 most frequently used domain names from the emails of users in this database
        # The domain name is the part of the email that comes after the @ symbol
        # Ex) email@emailaddress.com -> Domain name for this email is emailaddress.com
        # Your query should return up to 5 rows in the form:
        # domainname.com
        # domainname2.com
        # and so on
        # Note that i want the domain name not the raw email

        return """

            SELECT DISTINCT(SUBSTR(email, STRPOS(email,'@')+1)) FROM users GROUP BY LIMIT 5;

            """
