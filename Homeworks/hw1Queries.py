import psycopg2
class Queries():
    """Database queries"""

    #HOMEWORK 1
    #All questions should be one query
    #Put your queries within the """

    #Ex:
    #      """
    #       Your query here
    #      """

    # For this homework assignment we'll be focused on creating a grade book for a class
    # All table names need to be exact!

    def create_student_table(self):
    #Question 1:
        # We first should create a table to store student information.
        # Write a query that will generate a table called students 
        # Generate attributes for this table as follows (In this order):
            # student_id -> as an int and primary key
            # first_name -> as a varchar(Size is up to you )
            # last_name -> as a varchar(Size is up to you )
            # gpa -> as an real 
        return """
            """

    def create_homework_table(self):
    #Question 2:
        # We would need to next create a table to store information about homeworks
        # Write a query that will generate a table called homeworks
        # Generate attributes for this table as follows (In this order):
            # homework_id -> as an int and primary key
            # student_id -> as an int and foreign reference to student's primary key 
            # grade -> as an int 
        return """
            """


    def create_student_rows(self):
    #Question 3:
        # A table without data is useless
        # Write a single query to insert exactly 5 entries into the student table (same schema as above)
        # Assume i have generated the table for you with the schema above
        # You are free to insert any data you want, as long as rows get inserted into the table
        return """
            """

    
    def update_homework(self):
    #Question 4:
        # For the first 3 people who submitted the homework, i made a grading mistake.
        # Assuming that the first 3 homeworks are labeled 1-3 as their homework_ids
        # Write a query that adds 5 points to the first 3 homeworks submitted.
        return """
            """

    
    def delete_students(self):
    #Question 5:
        # At the end of the semseter i would likely either make a new table or clear the current one
        # Ideally we would keep a archive of the semseter but for the sake of practice we want to delete the data
        # Write a query to delete all the rows/entries in the students table that does not include my special student account (first_name = "instructor",last_name = "instructor")
        return """
            """
