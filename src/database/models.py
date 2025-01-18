"""
models.py

Defines the SQLAlchemy ORM models for the company's database schema, establishing relationships
between employees, departments, managers, and budgets.

Modules Imported:
    - os: For environment variable access.
    - load_dotenv: Loads environment variables from a .env file.
    - SQLAlchemy modules: Used to define database schema and relationships.
    - WORKDIR: Project's working directory for loading environment configuration.
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from src.settings import WORKDIR

# Load environment variables from the .env file
load_dotenv(WORKDIR / ".env")

# Retrieve database credentials from environment variables
USERNAME = os.getenv("MYSQL_USERNAME")
PASSWORD = os.getenv("MYSQL_PASSWORD")

# MySQL database connection URL
db_url_for_mysql = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@localhost:3306/company"

# Initialize SQLAlchemy engine
engine = create_engine(db_url_for_mysql)

# Base class for declarative models
Base = declarative_base()

# Create a session for database operations
Session = sessionmaker(bind=engine)
session = Session()

class Employee(Base):
    """
    Represents an employee in the company.
    Establishes a many-to-one relationship with the Department.

    Attributes:
        id (int): Primary key, auto-incremented.
        LastName (str): Employee's last name.
        FirstName (str): Employee's first name.
        SSN (str): Social Security Number (unique).
        Email (str): Employee's email address (unique).
        Department_ID (int): Foreign key referencing the Department.
    """
    __tablename__ = "Table_Employee"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    LastName = Column(String(20), nullable=False)
    FirstName = Column(String(20), nullable=False)
    SSN = Column(String(13), nullable=False, unique=True)
    Email = Column(String(30), nullable=False, unique=True)
    Department_ID = Column(Integer, ForeignKey("Table_Department.Department_ID"), nullable=False)

    department = relationship("Department", back_populates="employees")

    def __repr__(self):
        return f"<Employee({self.LastName}, {self.FirstName}, {self.SSN}, {self.Email}, {self.Department_ID})>"

class Department(Base):
    """
    Represents a department in the company.
    Establishes one-to-one relationship with Manager and one-to-many with Employees.

    Attributes:
        Department_ID (int): Primary key.
        Department_Name (str): Name of the department.
        Manager_ID (int): Foreign key referencing the Manager.
    """
    __tablename__ = "Table_Department"
    Department_ID = Column(Integer, primary_key=True, nullable=False)
    Department_Name = Column(String(20), nullable=False)
    Manager_ID = Column(Integer, ForeignKey("Table_Manager.Manager_ID"), unique=True)

    employees = relationship("Employee", back_populates="department", cascade="all, delete-orphan", uselist=True)
    manager = relationship("Manager", back_populates="department", uselist=False)

    def __repr__(self):
        return f"<Department({self.Department_ID}, {self.Department_Name}, {self.Manager_ID})>"

class Manager(Base):
    """
    Represents a manager of a department.
    Establishes a one-to-one relationship with Department and one-to-many with Budgets.

    Attributes:
        Manager_ID (int): Primary key.
        LastName (str): Manager's last name.
        FirstName (str): Manager's first name.
    """
    __tablename__ = "Table_Manager"
    Manager_ID = Column(Integer, primary_key=True, nullable=False)
    LastName = Column(String(20), nullable=False)
    FirstName = Column(String(20), nullable=False)

    department = relationship("Department", back_populates="manager")
    budget = relationship("Budgets", back_populates="manager", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Manager({self.Manager_ID}, {self.LastName}, {self.FirstName})>"

class Budgets(Base):
    """
    Represents a budget category managed by a Manager.
    Establishes a many-to-one relationship with Manager.

    Attributes:
        Manager_ID (int): Foreign key referencing the Manager.
        Resources (str): Type of resource (e.g., Hiring, Investments).
        Money (int): Amount allocated for the resource.
    """
    __tablename__ = "Table_Budgets"
    Manager_ID = Column(Integer, ForeignKey("Table_Manager.Manager_ID"), nullable=False)
    Resources = Column(String(20), nullable=False)
    Money = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("Manager_ID", "Resources"),
    )

    manager = relationship("Manager", back_populates="budget")

    def __repr__(self):
        return f"<Budgets({self.Manager_ID}, {self.Resources}, {self.Money})>"

# Create all defined tables in the database
Base.metadata.create_all(engine)
