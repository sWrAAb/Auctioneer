<h1 align="center">The Auctioneer</h1>
<h2 align="center"> Auction and Web Shop</h2>

## Table of Contents

1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Databases**](#databases)
    - [**Libraries**](#libraries)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)
    - [**Dark Mode**](#Dark-Mode)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Heroku Deployment**](#heroku-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

<br>
<br>

## UX

****
<br>

The online store you have been waiting for is just few clicks away.
This project is part of my Code Institute Full Stack Software Development studies. The objective for this milestone project is to create online shop and auction using Django framework. 

[**The Auctioneer can be viewed here**](https://the-auctioneer.herokuapp.com). 

The fully responsive project consists of HTML5 with Django Templates format, CSS3, JQuery, JavaScript, Python/Django(Frameworks).
Databases was stored and retrieved in the backend via sqlite3. Deployment technologies like Heroku and PostgreSQL were used to store Heroku database. 
AWS3 Bucket was also be used for  for static file storages and Amazon IAM service for security.

"**_As a Guest user, I would like to_**:"

- As a Guest, I want to view the website from any device *(mobile, tablet, desktop)*.
- As a Guest, I want to easily navigate through website.
- As a Guest, I want to search for shop for items i want.
- As a Guest, I want to view product details.
- As a Guest, I want to view rare artifacts.
- As a Guest, I want to create my password protected account.

"**_As a Registered user, I would like to_**:"

- As a Registered user, I want to login to the site via my registered details.
- As a Registered user, I want to bid online.
- As a Registered user, I want to pay with my credit card.
- As a Registered user, I want to view my profile.
- As a Registered user, I want to be able to view my Cart and any items I currently have awaiting payment in my Cart.
- As a Registered user, I want to add product the to cart and change quantity at any time.
- As a Registered user, I want to have the ability to Logout of the application.

"**_As a Administrator User, I would like to_**:"

- As a Site Administrator, I want to be able to login to an administration panel.
- As a Site Administrator, I want to have the ability to edit and update site content.
- As a Site Administrator, I want to ensure any user navigating to my site has a positive User experience between content and responsive design.

"**_As a Developer, I would like to_**:"

- As a Developer, I want to demonstrate my growing abilities as a Full Stack Software developer during my time on the CI course.
- As a Developer, I want a project that I can proudly showcase to potential employers via my Github Repository.
- As a Developer, I want to create a project that is fully scalable and can be expanded upon as I continue to grow as a developer.

### Design

The Auctioneer was designed to be simple and presentable with a purpose to sell items and not to distract users with many details.

#### Framework

- [Bootstrap 4.4.1](https://getbootstrap.com/)
    - I really like Bootstrap as a framework with great number of components and  its simple-to-understand documentation.
- [jQuery 3.4.1](https://code.jquery.com/jquery/)
    - In an effort to keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.
- [Django 2.2](https://www.djangoproject.com/)
    - Django is a framework I have used to render the back-end Python with the front-end Bootstrap 4.

#### Icons

- [Font Awesome 4.7.0](https://fontawesome.com/) 
  - I only used icons for social networks and angles for pagination.

#### Typography

- I have incorporated three of [Google Fonts](https://fonts.google.com/) throughout the entire application. The font I have selected for main title is
[Trade Winds](https://fonts.google.com/specimen/Trade+Winds),for page titles is
[Lora](https://fonts.google.com/specimen/Lora) and [Roboto](https://fonts.google.com/specimen/Roboto) for rest of the text.

### Wireframes

- For my wireframes, I have used [Balsamiq](https://balsamiq.com)
- Images can be viewed in my [Wireframes](https://github.com/sWrAAb/Auctioneer/tree/master/static/wireframes) folder


##### back to [top](#table-of-contents)

## Features

### Existing Features

#### **User Account**

- User can create account or login into existing account which alows him access to all content or log out.

#### **View All Products**

- All product can be viewed on products page

#### **Search Products**

- Products can be searched via search bar.

#### **Add Product to Cart**

- User can change product quantity inside of cart.

#### **Checkout**

- User can buy items via credit card.

#### **Auction**

- User can visit auction page.

### Features Left to Implement

Because of lack of time for finishing this project some requirements were not completed.

#### **Password Reset**

- Had some truble translating from Django 1.11 which was used in lesson into 2.2 I used for my project

#### **Bids**

- In the future, ability to bid for items will be added to auction.

#### **Dynamic search bar**

- Toggle buttons for categories will be added and they will display products from selected categories on the products page. 

#### **Product details**

- I have started to work on the funcionality but had trouble with slugs so I had to give it up for the time being. 

##### back to [top](#table-of-contents)

# Technologies Used

### Tools

- [Visual Studio Code](https://code.visualstudio.com/) is the IDE used for developing this project. 
- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
- [Stripe](https://stripe.com) as payment platform to validate and accept credit card payments securely.
- [Travis](https://travis-ci.org/) for continuous integration.
- [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.
- [Django Heroku](https://pypi.org/project/django-heroku/) to improve deployment of django projects on heroku.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.
- [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Adobe Photoshop](https://www.photoshop.com/en) used to resize images. 

### Databases

- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Libraries

- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide social icons for the website.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.
- [Dark Mode](https://darkmodejs.learn.uno/) tochange appearance of the website on demand.

##### back to [top](#table-of-contents)

## Testing

****

Testing information can be found in separate [testing.md](https://github.com/sWrAAb/Auctioneer/blob/master/testing.MD) file.

### Validators

#### **HTML**

- [W3C HTML Validator](https://validator.w3.org) - Unfortunately the W3C Validator for HTML does not understand the Django templating syntax, so it therefore shows a lot of errors with regards to `{{ variables }}`, `{% for %} {% endfor %}`, etc. Aside from the Jinja warnings and errors, all of the remaining code is perfectly validating.

#### **CSS**

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  - Did not show any problems

#### **JavaScript**

- [JShint](https://jshint.com/)
  - No major errors

#### **Python**

- [PEP8 Online](http://pep8online.com/)
  - No major errors

### Compatibility

To ensure a broad range of users can successfully use this site, I tested it on major browsers in both desktop and mobile configuration.

- Chrome
- Edge
- Firefox
- Opera
- Internet Explorer

[Autoprefixer](https://autoprefixer.github.io) was used for parsing CSS and adding vendor prefixes.

### Dark Mode

Dark Mode can be found in separate [darkmode.md](https://github.com/sWrAAb/Auctioneer/blob/master/darkmode.MD) file.

##### back to [top](#table-of-contents)

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools:
    - An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

Please click the links above for documentation on how to set these up and retrieve the necessary environment variables.

### Instructions

1. Save a copy of the github repository located at https://github.com/sWrAAb/Auctioneer by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
   ```
    git clone https://github.com/sWrAAb/Auctioneer
    ```

2. Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
    ```
    python -m .venv venv
    ```  
_NOTE: The `python` part of this command and the ones in other steps below assumes  you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_

4. Activate the .venv with the command:
    ```
    .venv\Scripts\activate 
    ```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

5. If needed, Upgrade pip locally with
    ```
    pip install --upgrade pip.
    ```

6. Install all required modules with the command 
    ```
    pip -r requirements.txt.
    ```

7. Set up the following environment variables within your IDE. 

    - If using VSCode, locate the `settings.json` file within the .vscode directory and add your environment variables as below. Do not forget to restart your machine to activate your environment variables or your code will not be able to see them: 

    ```json
    "terminal.integrated.env.windows": {
        "HOSTNAME": "<enter hostname here>",
        "DEV": "1",
        "SECRET_KEY": "<enter key here>",
        "STRIPE_PUBLISHABLE": "<enter key here>",
        "STRIPE_SECRET": "<enter key here>",
        "STRIPE_SUCCESS_URL": "<enter url here>",
        "STRIPE_CANCEL_URL": "<enter url here>",
        "AWS_ACCESS_KEY_ID": "<enter key here>",
        "AWS_SECRET_ACCESS_KEY": "<enter key here>",
        "AWS_STORAGE_BUCKET_NAME": "<enter bucket name here>",
    }
    ```

    - If using an IDE that includes a `bashrc` file, open this file and enter all the environment variables listed above using the following format: 
    ```
    HOSTNAME="<enter key here>"
    ```
    - `HOSTNAME` should be the local address for the site when running within your own IDE.
    - `DEV` environment variable is set only within the development environment, it does not exist in the deployed version, making it possible to have different settings for the two environments. For example setting DEBUG to True only when working in development and not on the deployed site.

8. If you have restarted your machine to activate your environment variables, do not forget to reactivate your virtual environment with the command used at step 4.

9. Migrate the admin panel models to create your database template with the terminal command
    ```
    python manage.py migrate
    ```

10. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:
    ```
    python manage.py createsuperuser
    ```

11. You can now run the program locally with the following command: 
    ```
    python manage.py runserver
    ```

12. Once the program is running, go to the local link provided and add `/admin` to the end of the ur. Here log in with your superuser account and create instances of ShippingDestination and Product within the new database.

13. Once instances of these items exist in your database your local site will run as expected.

## Heroku Deployment

To deploy The Auctioneer to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.

5. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

6. Confirm the linking of the heroku app to the correct GitHub repository.

7. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

8. Set the following config vars:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your secret key>`
AWS_SECRET_ACCESS_KEY | `<your secret key>`
AWS_STORAGE_BUCKET_NAME | `<your AWS S3 bucket name>`
DATABASE_URL | `<your postgres database url>`
HOSTNAME | `<your heroku app hostname>`
SECRET_KEY | `<your secret key>`
STRIPE_PUBLISHABLE | `<your secret key>`
STRIPE_SECRET | `<your secret key>`

8. From the command line of your local IDE:
    - Enter the heroku postgres shell 
    - Migrate the database models 
    - Create your superuser account in your new database
    
     Instructions on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View app" button provided.

11. From the link provided add `/admin` to the end of the url, log in with your superuser account and create instances of Auctions and Product within the new database.

12. Once instances of these items exist in your database your heroku site will run as expected.

## Credits

### Media

#### Images

All images were taken from google search.

### Code

- Template code was taken from [Bootstrap](https://getbootstrap.com) and [W3Schools](https://www.w3schools.com)
- CSS code from [CSS Tricks](https://css-tricks.com)
- Python code from Code Institute lessons

### Acknowledgements

- To my mentor, Spencer Barriball, for incredible mentoring, support and for assisting during my project reviews with great insight.

##### back to [top](#table-of-contents)
