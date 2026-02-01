# PetTracker CLI

A simple command-line application to help pet owners track care tasks for their pets. Built with Python and SQLAlchemy ORM.
Each pet gets a specifc ID, this is made possible by the ORM. The user inputs a pets name and type in order for the info to be stored in the database. Easy to follow steps and options are given to the user and the user is expected to select what they need.
Naturally each task also gets an ID that gets linked to a pet that will be the subject to the task.

## Features
- **Pet Management**: Add, view, find, and delete pets. CRUD functions inclusive.
- **Task Management**: Create, complete, and delete tasks for each pet
- **Relationship Viewing**: See all tasks assigned to a specific pet
- **Data Persistence**: All data stored in SQLite database using SQLAlchemy ORM
- **Input Validation**: User-friendly error messages and confirmation prompts

## Installation

1. **Clone the repository**:
   Open a specifc location on your device you would want to store the folder
   Open the folder.
   clone the repository using "git clone <repo link>"
   Navigate to PeTracker_CLI using <cd PeTracker_CLI>
2. **Set up environment**:
    Once you are in the required directory, copy the code below
    pipenv install
    pipenv shell
    The database will be automatically created after running
3. **Run the application**:
    Once finished setting up, run the code below to start up the app.
    cd lib
    python cli.py

## Tables & Relationships
pets table: id, name, species

tasks table: id, description, completed, pet_id (foreign key)

Relationship: One Pet → Many Tasks (one-to-many)

## Key ORM Features Demonstrated
SQLAlchemy declarative base models

Foreign key relationships with ForeignKey('pets.id')

Bidirectional relationships with relationship() and back_populates

Automatic table creation with Base.metadata.create_all()

## Technologies Used
Python 3.8 

SQLAlchemy ORM 

SQLite 

Pipenv 