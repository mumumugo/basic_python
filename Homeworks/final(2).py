import psycopg2
class Queries():

    # Final
    #All questions should be one query
    #Put your queries within the """

    #Ex:
    #      """
    #       Your query here
    #      """

    # All table names need to be exact!
    # The topic of this test will focused on HR-Data

    # For any questions related to selects, assume there is already data there



#   CREATE TABLE locations (
#     location_id integer NOT NULL,
#     street_address character varying(40),
#     postal_code character varying(12),
#     city character varying(30) NOT NULL,
#     state_province character varying(25),
#     country_id character(2) NOT NULL
# );

# CREATE TABLE countries (
#     country_id character(2) NOT NULL,
#     country_name character varying(40),
#     region_id integer NOT NULL
# );

# CREATE TABLE departments (
#     department_id integer NOT NULL,
#     department_name character varying(30) NOT NULL,
#     location_id integer
# );

# CREATE TABLE dependents (
#     dependent_id integer NOT NULL,
#     first_name character varying(50) NOT NULL,
#     last_name character varying(50) NOT NULL,
#     relationship character varying(25) NOT NULL,
#     employee_id integer NOT NULL
# );


# CREATE TABLE employees (
#     employee_id integer NOT NULL,
#     first_name character varying(20),
#     last_name character varying(25) NOT NULL,
#     email character varying(100) NOT NULL,
#     phone_number character varying(20), (This is in the format xxx.xxx.xxxx)
#     hire_date date NOT NULL,
#     job_id integer NOT NULL,
#     salary numeric(8,2) NOT NULL,
#     manager_id integer,
#     department_id integer
# );

# CREATE TABLE jobs (
#     job_id integer NOT NULL,
#     job_title character varying(35) NOT NULL,
#     min_salary numeric(8,2),
#     max_salary numeric(8,2)
# );

# CREATE TABLE regions (
#     region_id integer NOT NULL,
#     region_name character varying(25)
# );


    def Q1(self):
    #Question 1:
        # We are running a HR raffle, we have decided to reward an employee
        # We made up random constraints in which to pick our winner
        # The winner needs to fit the following requirements
            # employee_id should be an odd number ( use the % operator on the attribute and check if it's 1)
            # the employee's salary is less than 4000
            # they are the oldest employee after filtering via the last two restrictions
        # Write a query that will return to me the first name, last name and their email address (in this order)

        return """
        SELECT first_name,last_name,email FROM employees WHERE employee_id % 2 =1 AND salary < 4000 ORDER BY hire_date LIMIT 1;
            """

    def Q2(self):
    #Question 2:
        # Find all employees who's salary is between the following range:
        # [MAX(min_salary),MAX(max_salary)]
        # In other words, which employees have a salary that is within the highest min_salary and the highest max_salary provided by this company
        # Write a query to return the first name, last name, email, and job title of all employees who meet this requirement
        return """
        SELECT first_name,last_name,email,job_title FROM employees e, jobs j WHERE salary BETWEEN (SELECT MAX(min_salary) FROM jobs) AND (SELECT MAX(max_salary) FROM jobs)
        AND e.job_id = j.job_id;
            """


    def Q3(self):
    #Question 3:
        # We want to know how many locations we have in each "region"
        # Write a query that will return the region name, and the amount of locations we have in each region
        # Output Ex)
        #    'region1' 5
        #    The row above details that there are 5 locations in region 1
        return """
        SELECT region_name, COUNT(*) FROM regions r, countries c, locations l WHERE r.region_id = c.region_id
        AND c.country_id = l.country_id GROUP BY r.region_name;

         """

    def Q4(self):
    #Question 4:
        # Due to difficult times, we will have to be closing all locations that aren't located in either the US or CA locations due to tax reasons
        # Write a query to return the first name, last name and email of all employees we will have to lay off
        return """
        SELECT first_name, last_name, email FROM employees e, departments d, locations l WHERE e.department_id NOT IN (
        SELECT department_id FROM departments WHERE location_id IN (SELECT location_id FROM locations WHERE country_id='CA' OR country_id = 'US'));
             """


    def Q5(self):
    #Question 5:
        # Rumor has it that the CEO has been planning on downsizing the company
        # The rumor is any employees without a dedicated phone_number is marked for "termination" (phone number is NULL)
        # Also it seems that the CEO wants to completely eliminate the entire job title
        # We recently learned that if a job title has more than 2 employees then they are most likely the target
        # Write a query that will return the job title and the amount of employees with that job title that match the description above.
        return """
        SELECT job_title, COUNT(employee_id) FROM employees e, jobs j WHERE phone_number IS NULL AND e.job_id = j.job_id
        GROUP BY job_title HAVING COUNT(*) > 2;

          """


    def Q6(self):
    #Question 6:
        # We are ready to issue new insurance policies for the quarter
        # Some of our employees have dependents and some don't
        # We want a list of employees that have dependents
        # Write a query that will return:
        #       employee's first name
        #       employee's last name
        #       employee's email
        #       dependent's first name
        #       dependent's last name
        #       dependent's relationship
        return """
        SELECT e.first_name, e.last_name, e.email, d.first_name, d.last_name, d.relationship FROM employees e, dependents d WHERE
        e.employee_id = d.employee_id;

            """


    def Q7(self):
    #Question 7:
        # After laying off some people, we have money to expand!
        # We want you to gather a list of countries and the regions that we don't have locations in
        # Write a query that will return 2 columns that meets the requirements above:
        #   The first column should be country and will display the country name
        #   The second column should be named region and will display the region
        return """
        SELECT country_name AS country, region_name AS region FROM countries c, regions r WHERE
        c.region_id = r.region_id AND c.country_id NOT IN (SELECT country_id FROM locations);
            """


    def Q8(self):
    #Question 8:
        # Someone left a message for an employee and wrote their information on a post-it note
        # The issue is that the post-it note is hardly readable and it was marked urgent!
        # However we can make out some parts of the post-it note
            # The employee's phone number seems to have a 5 followed by some digits then a 4.
            # Their job title's third letter is an 'o'
            # There seems to be 5 total characters total in their first name
            # Their email ends in .com
            # Their email also contains a number in it
        # Write a query to return all the attributes that exists in Employees based on the restrictions above
        return """
        SELECT * FROM employees e, jobs j WHERE e.phone_number LIKE '%5%4%' AND j.job_title LIKE '__o%' AND LENGTH(e.first_name) = 5 AND
        e.email LIKE '%.com' AND e.job_id = j.job_id AND email IN (SELECT email FROM employees WHERE email [0-9]);
            """

    def Q9(self):
    #Question 9:
        # It seems i have won an online contest i forgot i entered!
        # To claim my prize i need to submit information about employees that work at our company!
        # The contest states that i need find employees that aren't located in north America (US or CA) and they MUST have a phone number
        # They want me to give them an employee with a valid postal code so i can pick it up at the employee's place!
        # NOTE: Employees without a phone number/postal code will have that field displayed as NULL
        # Write a query that will return the first name, last name, phone number, street address, email, salary, job title of all employees that meet this requirement
        return """
        SELECT first_name, last_name, phone_number, street_address, email, salary, job_title FROM employees e, jobs j, departments d, locations l, countries c WHERE
        e.department_id = d.department_id AND d.location_id = l.location_id AND l.country_id = c.country_id AND c.country_id != 'US' AND c.country_id != 'CA' AND
        e.job_id = j.job_id AND phone_number IS NOT NULL AND postal_code IS NOT NULL;
           """


    def Q10(self):
    #Question 10:
        # We want to view the employee salary disparity
        # We want to compare the difference in salary of the manager to every other employee (including the manager)
        # Write a query that will return the first name, last name and the difference in salary compared to the manager (manager salary - employee salary)
        # Name the 3rd column as 'salary_diff'
        # Note: The manager will have manager_id as NULL, there should also be a row where the diff is 0 (the row will be comparing the manager's salary with itself)
        return """
        SELECT first_name, last_name, ((SELECT salary FROM employees WHERE manager_id IS NULL)- salary)AS salary_diff FROM employees;

             """
