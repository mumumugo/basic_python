import psycopg2
class Queries():

    # Midterm
    #All questions should be one query
    #Put your queries within the """

    #Ex:
    #      """
    #       Your query here
    #      """

    # All table names need to be exact!
    # The topic of this midterm will be a banking database

    # All date values are in the form MM/DD/YYYY

    # For any questions related to selects, assume there is already data there

    #Assume that we already have the following table

    # Table: accounts
    # Attributes (
        # account_id serial primary key,
        # account_email string,
        # full_name VARCHAR(200)
    #)

    # Table: savings
    # Attributes (
        # account_id references account's primary key,
        # saving_id serial primary key,
        # saving_balance big int,
        #  open_date date
    # )


    # Note: Q3 and beyond you will only need to refer to the two tables above

    def Q1(self):
    #Question 1:
        # Make a table called checking to represent a checking's account
        # The attributes should be the following (In this order):
            # account_id BIG INT that references account_id from accounts
            # saving_id should be an auto incrementing attribute that's the primary key
            # balance BIG INT
            # open_date date
        return """
        CREATE TABLE checking(account_id BIGINT, checking_id SERIAL, balance BIGINT, open_date DATE, PRIMARY KEY(checking_id), FOREIGN KEY (account_id) REFERENCES accounts (account_id));
            """

    def Q2(self):
    #Question 2:
        # Today is 10/10/2021
        # You are tasked with inserting opening 5 new checking accounts
        # The account_ids are as follows (10,11,12,13,14)
        # Each customer wants to put a deposit for (1000,2000,1000,1500,1) upfront
        # Write a query that will insert 5 rows for the new accounts (Date should be in the form mentioned above)
        return """
        INSERT INTO checking(account_id, balance, open_date) VALUES
        ('10','1000','10/10/2021'),
        ('11','2000','10/10/2021'),
        ('12','1000','10/10/2021'),
        ('13','1500','10/10/2021'),
        ('14','1','10/10/2021');
            """


    def Q3(self):
    #Question 3:
        # The bank manager wants to know about how many saving accounts have been open during the year of 2019
        # Write a query to find the amount of saving accounts opened in the year 2019
        return """
        SELECT COUNT(saving_id) FROM savings WHERE open_date >='01/01/2019' AND open_date <= '12/31/2019';
            """


    def Q4(self):
    #Question 4:
        # The bank wants to send out some junk mail in attempts to get people to open loans
        # Now we don't want just anyone to open a loan so we have the following requirements
        # The person must have a savings account with at least a balance of 5000
        # The person must have opened their account on the date of '1/1/2000' or later
        # Write a query that will return the account_email of all accounts that fit our requirements
        return """
        SELECT account_email FROM accounts WHERE account_id IN (SELECT account_id FROM savings WHERE saving_balance >= 5000 AND open_date >= '1/1/2000');
            """


    def Q5(self):
    #Question 5:
        # The bank is forgiving any saving account debt for those accounts that were opened after 1/1/2000 and before 1/1/2010
        # Write a query that will reset the balance to zero of any saving accounts that are "forgiven"
        return """
        UPDATE savings SET saving_balance = 0 WHERE open_date >='1/1/2000' AND open_date <='1/1/2010';
            """


    def Q6(self):
    #Question 6:
        # We want to email and thank all users who have been maintaining a high balance with us
        # Write a query that will return the full name, and the email of any accounts (in this order) that have more than 1000 as their saving balance
        return """
        SELECT full_name, account_email FROM accounts WHERE account_id IN (SELECT account_id FROM savings WHERE saving_balance > 1000);
            """


    def Q7(self):
    #Question 7:
        # The bank is not doing so hot, we would like our customers to give us more money in the form of saving balances
        # The plan is to send an email offering customers that do not have a savings account with us
        # Write a query that will return the email of any account that does not currently have a savings account but has an account opened with us
        return """
        SELECT account_email FROM accounts WHERE account_id NOT IN (SELECT account_id FROM savings);
            """


    def Q8(self):
    #Question 8:
        # The manager wants a ranking of days with the most saving accounts opened
        # Ex)
        #   If the date '1/1/1111' had 10 accounts opened and this was the most accounts opened on a single day this should be the first row
        #   If date '1/2/1111' had 9 accounts opened and this was the 2nd most accounts opened in a single day this will be the 2nd row
        #   etc
        # Note: The query should return a row for each date once
        # Write a query to return the date followed by the amount of accounts openned for that day in descending order
        return """
        SELECT open_date,COUNT(*) FROM savings GROUP BY open_date ORDER BY COUNT(*) DESC;
            """

    def Q9(self):
    #Question 9:
        # Our IT department found a glitch in our system
        # It seems that some saving accounts where inserted 2 or more times
        # We are tasked with finding duplicated rows in the savings table with the same account_id
        # Write a query that gives us back a list of account_ids that have more than 1 row associated with them
        return """
        SELECT account_id FROM savings GROUP BY account_id HAVING COUNT(account_id)>1;
            """


    def Q10(self):
    #Question 10:
        # The CFO wants to know who the top 3 richest people in our system are
        # Write a query that will return the full names of the top 3 richest people (based on saving balance)
        return """
        SELECT full_name FROM accounts,savings WHERE accounts.account_id = savings.account_id ORDER BY saving_balance LIMIT 3;
            """
