import psycopg2
class Queries():

    #HOMEWORK 5
    #All questions should be one query
    #Put your queries within the """

    #Ex:
    #      """
    #       Your query here
    #      """

    # For this homework we will be looking at a database for not so secret "agents"
    # The schema is provided below
    # Assume data is already populated in the tables
    # All table names need to be exact!

    # CREATE TABLE agents(
    #     agent_id SERIAL PRIMARY KEY,
    #     real_name VARCHAR(255),
    #     code_name VARCHAR(255),
    #     status VARCHAR(255)
    #    );


    # CREATE TABLE gadgets(
    #     gadget_id SERIAL PRIMARY KEY,
    #     assigned_agent INTEGER,
    #     gadget_name VARCHAR(255),
    #     FOREIGN KEY (assigned_agent) REFERENCES agents(agent_id)
    #  );

    # CREATE TABLE missions(
    #     mission_id SERIAL PRIMARY KEY,
    #     mission_name VARCHAR(255),
    #     assigned_agent INTEGER,
    #     mission_funds DOUBLE PRECISION
    #     FOREIGN KEY (assigned_agent) REFERENCES agents(agent_id)
    #  );

    #  CREATE TABLE payroll(
    #      agent_id INTEGER,
    #      salary DOUBLE PRECISION,
    #      FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
    # );

    def insert_data(self):
    #Question 1:
        # Insert at least 5 new agents, 5 new gadgets, 10 missions and 5 payroll rows
        # You are allowed to submit more than 1 query
        return """
        INSERT INTO agents(real_name,code_name,status) VALUES ('NOZE','NOZEWORLD','GOOD'),
        ('NOZEE','NOZEWORLDDDD','FAIL'),('NOZEEEE','NOZEWORLDDDDDD','VERY GOOD'),('NOZEEEEEEEEE','NOZEWORLDDDDDDDD','GREAT'),('NOZEYO','NOZEWORLDDD','GREAT');

        INSERT INTO gadgets(assigned_agent,gadget_name) VALUES ('23','WORLDTOUR'),('11','BUSANTOUR'),('53','DAEGUOUR'),
        ('61','ULSANTOUR'),('22','JEJUTOUR');

        INSERT INTO missions(mission_name,mission_funds,assigned_agent) VALUES ('SEOULTOUR','850000.35','77'),('DAEGUTOUR','850000.99','77'),('SSEOULTOUR','850000.6','77'),
        ('SEOULTOUURR','800.456','7'),('SEOULTOUUUUR','650.4','17'),('SEOOOOULTOUR','8500.24','57'),('SEEEOULTOUR','850.44','37'),('SSSSSSEOULTOUR','8500.54','67'),('SSSSEOULTOUR','5000.99','77'),
        ('SEOULTOURRR','8000.687','87'),('SSEOULTOURR','85.55','97');

        INSERT INTO payroll(agent_id,salary) VALUES ('11','150000.66'),('12','100000.47'),('9','600000.35'),('51','70000.88'),('21','1500.99');
            """

    def active_missions(self):
    #Question 2:
        # The spy master wants to view all active missions/agents
        # A mission is active if the assigned agent's status is "ACTIVE" (case sen.)
        # Write a query to return the agent's code names, mission names, and the salary of said agent
        # Note an agent may be part of multiple missions, return each on their seperate rows
        return """
        SELECT code_name, mission_name, salary FROM agents a, missions m, payroll p WHERE
        m.assigned_agent IN (SELECT agent_id FROM agents WHERE status = 'ACTIVE') AND
        m.assigned_agent = a.agent_id AND
        m.assigned_agent = p.agent_id;
            """

    def gadgets(self):
    #Question 3:
        # Some of our agents are new and have not been assigned any gadgets
        # We want to be able to provide each agent with their own gadget
        # A agent is assigned a gadget if in the gadget table their agent_id can be found in the assigned_agent column
        # Write a query that will return a list of agents codenames that are not assigned a gadget
        return """

        SELECT code_name FROM agents a WHERE a.agent_id NOT IN (SELECT DISTINCT assigned_agent FROM gadgets);
            """


    def reassign_gadgets(self):
    #Question 4:
        # We want to reassign gadgets belonging to KIA or TERMINATED(status of the agent is either KIA or TERMINATED, case sen.)
        # agents to the new agents
        # We want to ensure that the gadgets aren't used twice in the same mission
        # Write a query to fetch the codename of the agent (either KIA or TERMINATED),
        #                  the gadget name assigned to that agent
        #                  and any missions that agent has been on
        # Note: Multiple rows will appear for the same agent
        return """

        SELECT code_name, gadget_name, mission_name FROM agents a, gadgets g, missions m WHERE
        g.assigned_agent IN (SELECT agent_id FROM agents WHERE status = 'KIA' OR status = 'TERMINATED') AND
        g.assigned_agent = a.agent_id AND
        a.agent_id = m.assigned_agent;
            """

    def house_keeping(self):
    #Question 5:
        # The spy master wants to set up a list for currently inactive agents so they could be assigned work
        # We define an inactive agent as a agent that is not currently assigned a mission
        # Before they are assigned a mission, we need to decide which mission they are fit to do
        # We want to look at a agent's salary,and any gadgets they currently are assigned
        # Write a query to return the code_name of agents,and the agent's salary of all inactive agents that do NOT have a gadget assigned to them
        # Note agents can have multiple lines
        return """
        SELECT code_name, salary FROM agents, payroll WHERE
        agents.agent_id IN (SELECT agent_id FROM agents WHERE status = 'INACTIVE') AND
        agents.agent_id NOT IN (SELECT assigned_agent FROM gadgets) AND
        agents.agent_id = payroll.agent_id;
             """


    def real_intentions(self):
    #Question 6:
        # I have a personal request
        # I need to send a report to my bosses overseas
        # Can you write a query that provides me with the following information for all active agents that are on missions that have funding > 5000 (in this order):
        #       agent's real name,
        #       assigned gadget for each agent,
        #       assigned mission names for each agent
        # Note: All active agents have a status of "ACTIVE"
        return """
        SELECT real_name, gadget_name, mission_name FROM agents a FULL JOIN gadgets g ON
        a.agent_id = g.assigned_agent FULL JOIN missions m ON a.agent_id = m.assigned_agent WHERE
        a.status = 'ACTIVE' AND mission_funds > 5000;
            """
