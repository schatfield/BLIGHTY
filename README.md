# BLIGHTY

Blight·y <br>
/ˈblīdē/ <br>
noun BRITISH <br>
<i>An informal and typically affectionate term for Britain or England, chiefly as used by soldiers of World War I and World War II.</i>


BLIGHTY is curated directory of some of the best country pubs in England. With Blighty pub lovers are able to track the entire life cycle of their own personal bucket list from daydream to experience by creating collections of pubs they’d like to visit, keep track of pubs they’ve been to, and there’s the ability to record their experiences at pubs they’ve checked off their list.


# Why was BLIGHTY created?

As a self professed Anglophile, BLIGHTY is my personal loveletter to one of England's most unique institutions that is the English Pub. 

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
<img src="https://imgur.com/xBuLENr">

