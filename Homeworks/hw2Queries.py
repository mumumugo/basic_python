import psycopg2
class Queries():
    """Database queries"""

    #HOMEWORK 2
    #All questions should be one query
    #Put your queries within the """

    #Ex:
    #      """
    #       Your query here
    #      """

    # For this homework we will be talking about a simple online shop
    # The schema is provided below
    # Assume I have already populated the tables with data
    # All table names need to be exact!

    # CREATE TABLE accounts (user_id SERIAL PRIMARY KEY , username VARCHAR(255), password VARCHAR(255) );
    # CREATE TABLE items (product_num SERIAL PRIMARY KEY , quantity INTEGER, price REAL
    # 					, product_name VARCHAR(255));
    # CREATE TABLE transactions (order_num  SERIAL, user_id INTEGER, product_num INTEGER,
    # 						  PRIMARY KEY (order_num),
    # 						   FOREIGN KEY (user_id) REFERENCES accounts (user_id) ,
    # 						   FOREIGN KEY (product_num) REFERENCES items (product_num)
    # 						  );

    def insert_data(self):
    #Question 1:
        # Insert at least 1 new account into the account table,
        # 5 new rows to the items table,
        # and at least 5 rows to the transactions
        # You are allowed to submit more than 1 query
        return """
        INSERT INTO accounts (username, password) VALUES ('beapilot', 'bebbee');

        INSERT INTO items (quantity, price, product_name)
        VALUES ('23','15','bodywash'),
        ('55','22','handcream'),
        ('21','44','bodylotion'),
        ('22','11','soap'),
        ('7','12','cream');

        INSERT INTO transactions (user_id) VALUES (2),(3),(4),(5),(6);
            """

    def distinct_items(self):
    #Question 2:
        # The company's marketing department wants to know the distinct items we have for sale
        # Write a query that will provide to me the amount of distinct items we sell in the store
        # An item is distinct if it has a unique product_name and we have at least one of the item in stock
        return """
        SELECT COUNT(DISTINCT product_name) FROM items WHERE quantity>0;
            """

    def sell_out(self):
    #Question 3:
        # The store owner wants to know what the total profit we can make with the current in stock items
        # Write a query to return the total amount of money we would gain if we were to sell every item in stock
        return """
        SELECT SUM(quantity * price) FROM items;
            """


    def hacked_account(self):
    #Question 4:
        # One of our customer's account has been hacked!
        # We need to revert all transactions made by this account, but first we should gauge the damage
        # Write a query that will tell us how many transactions were made by the account with a username of "notanhackedaccount"
        return """
        SELECT COUNT(user_id) FROM transactions WHERE user_id = (SELECT user_id FROM accounts WHERE username ='notanhackedaccount' );
            """


    def raffle(self):
    #Question 5:
        # We started a raffle for a lucky customer!
        # We want to get the pool of customers that are eligable to win, the requirements are
        # You must have have a purchased a item called "Raffle Ticket"
        # You must have at least 2 transactions
        # Write a query that will return the usernames of any account the meets the conditions above

        return """
        SELECT username FROM accounts WHERE user_id IN
        (SELECT user_id FROM transactions WHERE product_num = (SELECT product_num FROM items WHERE product_name = 'Raffle Ticket')
        AND user_id IN (SELECT user_id FROM transactions WHERE order_num >2));
            """


    def uranium(self):
    #Question 6:
        # For some reason the item "Uranium" has been so popular that the goverment catch wind of us selling it!
        # Apprently the government doesn't like us selling Uranium
        # They have demanded we flag all transactions made by users that have purchased uranium from our store
        # Write a query to return the amount of transactions that we need to flag.
        return """
        SELECT COUNT(product_num) FROM transactions WHERE product_num = (SELECT product_num FROM items WHERE product_name ='Uranium');
            """
