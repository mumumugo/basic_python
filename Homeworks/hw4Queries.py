import psycopg2
class Queries():

    #HOMEWORK 4 (wild cards, regex and join )
    #All questions should be one query
    #Put your queries within the """

    #Ex:
    #      """
    #       Your query here
    #      """

    # For this homework we will be looking at a simple blog
    # The schema is provided below
    # Assume the tables are already populated with data
    # All table names need to be exact!

    # CREATE TABLE users(user_id SERIAL PRIMARY KEY, password VARCHAR(255), email VARCHAR(255));
    # CREATE TABLE posts(user_id BIGINT , post TEXT, FOREIGN KEY (user_id) REFERENCES users(user_id));
    # CREATE TABLE followers(user_id BIGINT, follower_id BIGINT, FOREIGN KEY (user_id) REFERENCES users (user_id), FOREIGN KEY (follower_id) REFERENCES users (user_id));

    def insert_data(self):
    #Question 1:
        # Insert at least 2 users, 5 new posts, and 10 followers relationships
        # You are allowed to submit more than 1 query
        return """
        INSERT INTO users (password, email) VALUES
        ('security55','noze@gmail.com'),
        ('zzang22!','nozezzang@gmail.com'),
        ('nugasorirnae22^^','iky_kr@gmail.com');

        INSERT INTO posts (user_id, post) VALUES
        ('1','please follow, subscribe, and like!'),
        ('2','hi, please contact follow person~'),
        ('3','assume i have already poplated!'),
        ('4','you are allowed!'),
        ('5','you are not allowed to read this contants!');

        INSERT INTO followers (user_id, follower_id) values
        ('21','1'),('1324','74'),('131','42'),('53','34'),
        ('3','21'),('755','4'),('34','53'),('321','123'),
        ('67','32'),('84','234'),('73','757'),('948','934');

            """

    def search(self):
    #Question 2:
        # A user on the blog posted their password and email address by accident.
        # They quickly deleted the post but there were a few details about his password and email i can recall
        # Their password was exactly 10 characters long with the 3rd and 4th characters being 'l'
        # Their text before the @ symbol was more than 9 characters long (name@domain.com, i'm talking about the name part here)
        # Write a query to display the user_id,password, and email of all users that match this description
        return """
        SELECT user_id,password,email FROM users WHERE password LIKE '__ll______' AND email LIKE '_________%@%';'
            """

    def bots(self):
    #Question 3:
        # We have detected some bots (automated accounts likely to increase follower count)
        # These bots have registered with a non-valid email
        # We define a non-valid email as an email with the absences of the @ symbol
        # We also have noticed that the bots are generating posts of strictly only numberical values/ exclude empty post
        # Write a query to list out the emails of potential bot accounts
        return """
        SELECT email FROM users WHERE STRPOS(users.email,'@') = 0  AND user_id IN (SELECT user_id FROM posts WHERE post~'^[0-9]+$');
            """


    def get_posts(self):
    #Question 4:
        # We want to run a query to pull all posts that a specific user follows
        # Write a query that will return to me the email and posts for the people user_id 1 follows.
        # Ex) If user 1 follows users 2(email:user2@email.com) and 3(email:user3@emai.com), and user 2 has a post of "post 1" and user 3 has a post of "post 2"
        #     your table should return two rows along the lines of:
        #     user2@email.com, post 1
        #     user3@email.com, post 2

        return """
        SELECT email,post FROM users INNER JOIN posts ON users.user_id = posts.user_id INNER JOIN followers ON users.user_id = followers.user_id;
            """


    def spammer(self):
    #Question 5:
        # We are interested in finding the users that generate post with the most words
        # Write a query to return the email and post of the posts containing the highest word count
        # Hint: In a sentence to count the words you count the spaces
        return """
        SELECT email,post FROM users u,posts p WHERE length(p.post)>
            """


    def exposed_passwords(self):
    #Question 6:
        # Recently a lot of people have been hacked, we think it's due to the fact that some people have posted their passwords within a post
        # We want to force a password reset for all users who have their passwords anywhere within their posts
        # Write a query to return the email,password, and the post where we detected the user's password.
        # Ex)
        # If my password was password (with email was email@emailaddress.com) and i had a post with the following content ("I forgot my password")
        # A row in the return table should look like:
        # email@emailaddress.com ,password, I forgot my password
        # There can be multiple rows for the same user (cases where they post their password at different times)

        return """
        SELECT email,password,post FROM
             """
