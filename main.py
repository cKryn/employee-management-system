"""
main.py

This script initializes and populates the database with sample data for a company structure.
It defines departments with their respective employees and managers, including budget allocations.

Modules Imported:
    - Department, Employee, Manager, Budgets: ORM models for database tables.
    - session: SQLAlchemy session object for database interactions.
"""
from src.database.models import Department, Employee, Manager, Budgets, session

# Creating the HR Department with employees and manager
department1 = Department(Department_ID=101, Department_Name="HR",
    employees=[
        Employee(LastName="Popa", FirstName="Ion", SSN="1890812283456", Email="popa.ion@gmail.com"),
        Employee(LastName="Cirstea", FirstName="Mara", SSN="2021805453216", Email="maria.cirstea@gmail.com")
    ],
    manager=Manager(Manager_ID=100, LastName="Chivu", FirstName="Sorina",
        budget=[
            Budgets(Resources="Hiring", Money=20000),
            Budgets(Resources="Investments", Money=40000),
            Budgets(Resources="Vacations", Money=10000)
        ]))

# Creating the Testing Department with employees and manager
department2 = Department(Department_ID=102, Department_Name="Testing",
    employees=[
        Employee(LastName="Dinu", FirstName="Cristian", SSN="1910610455632", Email="dinu.cristian@gmail.com")
    ],
    manager=Manager(Manager_ID=200, LastName="Pruna", FirstName="Ioana",
        budget=[
            Budgets(Resources="Vacations", Money=10000),
            Budgets(Resources="Hiring", Money=10000),
            Budgets(Resources="Investments", Money=43000)
        ]))

# Creating the DevOps Department with employees and manager
department3 = Department(Department_ID=103, Department_Name="DevOps",
    employees=[
        Employee(LastName="Vasile", FirstName="Georgiana", SSN="2880721822217", Email="georgiana.vasile@gmail.com")
    ],
    manager=Manager(Manager_ID=300, LastName="Streche", FirstName="Bogdan",
        budget=[
            Budgets(Resources="Investments", Money=50000),
            Budgets(Resources="Hiring", Money=20000),
            Budgets(Resources="Vacations", Money=7000)
        ]))

# Adding departments to the session and committing changes
session.add_all([department1, department2, department3])
session.commit()
session.close()