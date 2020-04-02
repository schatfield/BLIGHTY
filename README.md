# BLIGHTY

# What is BLIGHTY?


# Why was BLIGHTY created?


# Instructions for running and installing BLIGHTY

Clone this repo using the following command then cd into it

    `git clone git@github.com:schatfield/BLIGHTY.git`

Mac users: create your virtual environment in Terminal

    `python -m venv blightyenv`
    `source ./blightyenv/bin/activate`
    
Windows users: create your virtual environment in Command Line

    `python -m venv blightyenv`
    `source ./blightyenv/Scripts/activate`

Install app dependencies

    `pip install -r requirements.txt`

Build your database from the existing models

    `python manage.py makemigrations blightyapp`
    `python manage.py migrate`

Create a superuser for your local version of the app

    `python manage.py createsuperuser`

Populate your database with initial data from fixture file: 

    `python manage.py loaddata blighty`
    
Run your development server

    `python manage.py runserver`

# Entity Relationship Diagram
<blockquote class="imgur-embed-pub" lang="en" data-id="a/Q4xHQP0"><a href="//imgur.com/a/Q4xHQP0">ERD</a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>
