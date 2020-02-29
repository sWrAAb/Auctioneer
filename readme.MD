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
    - [**Known Issues**](#known-issues)

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

The Auctioneer can be viewed https://the-auctioneer.herokuapp.com. 

The fully responsive project consists of HTML5 mostly in Jinja Templates format, CSS3, JQuery, JavaScript, Python/Django(Frameworks).
Databases was stored and retrieved in the backend via sqlite3. Deployment technologies like Heroku and PostgreSQL were used to store Heroku database. 
AWS3 Bucket was also be used for  for static file storages and Amazon IAM service for security.

"**_As a user, I would like to_**:"

- view the website from any device *(mobile, tablet, desktop)*
- easily navigate through website
- search for shop for items i want
- add product the to cart and change quantity at any time
- view product details
- view rare artifacts
- bid online
- pay with my credit card
- create my account and view my profile


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
  - I only used icons for social networks.

#### Typography

- I have incorporated three of [Google Fonts](https://fonts.google.com/) throughout the entire application. The font I have selected for main title is
[Trade Winds](https://fonts.google.com/specimen/Trade+Winds),for page titles is
[Lora](https://fonts.google.com/specimen/Lora) and [Roboto](https://fonts.google.com/specimen/Roboto) for rest of the text.

### Wireframes

- For my wireframes, I have used Windows Paint
- Images can be viewed in my [Wireframes](https://github.com/sWrAAb/Auctioneer/tree/master/static/wireframes) folder


##### back to [top](#table-of-contents)

## Features

### Existing Features


**User Account**
- User can create account or login into existing account which alows him access to all content or log out.

**View All Products**
- All product can be viewed on products page

**Search Products**
- Products can be searched via search bar.



**Add Product to Cart**
- User can change product quantity inside of cart. 

**Checkout**
- User can buy items via credit card. 


**Auction**
- User can visit auction page.


### Features Left to Implement

Because of lack of time for finishing this project some requirements were not completed.

**Pagination**
- At this time all products are displayed on a single page. It works now but might take long time to load when more products are added.

**Bids**
- In the future, ability to bid for items will be added to auction.


**Dynamic search bar**
- Toggle buttons for categories will be added and they will display products from selected categories on the products page. 

**Product details**
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

### Databases
- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Jasmine](https://jasmine.github.io/) to run automated tests on JavaScript and jQuery code.
- [Jasmine-jQuery](https://github.com/velesin/jasmine-jquery) to make it possible to test jQuery code using Jasmine.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for The House of Mouse webshop.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.

##### back to [top](#table-of-contents)


## Testing

****

Testing information can be found in separate [testing.md](https://github.com/sWrAAb/Auctioneer/blob/master/testing.MD) file.

### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) - Unfortunately the W3C Validator for HTML does not understand the Jinja templating syntax, so it therefore shows a lot of errors with regards to `{{ variables }}`, `{% for %} {% endfor %}`, etc. Aside from the Jinja warnings and errors, all of the remaining code is perfectly validating. 

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - Did not show any problems


**JavaScript**
- [JShint](https://jshint.com/) - 
    - No major errors

**Python**
- [PEP8 Online](http://pep8online.com/)
    -No major errors

### Compatibility

To ensure a broad range of users can successfully use this site, I tested it on major browsers in both desktop and mobile configuration.

- Chrome 
- Edge 
- Firefox 
- Opera 
- Internet Explorer

[Autoprefixer](https://autoprefixer.github.io) was used for parsing CSS and adding vendor prefixes.

### Known Issues

- Search bar has stopped working.  

##### back to [top](#table-of-contents)

