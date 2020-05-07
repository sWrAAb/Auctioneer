Readme file](https://github.com/sWrAAb/Auctioneer/blob/master/README.md)

[Heroku Live - The Lost Page](https://the-auctioneer.herokuapp.com)

### Python testing

Some of the functions were tested using unittest.
Because of testing complexity and lack of time only 5 functions were tested.


#### Testing instructions

To run tests use command:  python manage.py test

## UX Testing

- To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it.

- Navbar is laid out in the conventional way:

- Navbar is at the top of the screen.

- The primary purpose of the site - webshop and auction - are easily found in the navbar.

- The footer is also laid out in a conventional way.

- Contact information and links are provided in the footer.

- Social media links also provided in the footer where the user would expect to find them.

- The information I am presented with to be laid out in a way that is easy for me to navigate, so that I find what I need quickly and efficiently.

- The page is broken up into easy to understand sections, and the data displayed in a way that is most easy to read.

- Tables and icons are used where applicable, which all aid in easily accessible information for the user.
- As a user accessing this site from a mobile phone or tablet, I want the site designed responsively so that it is still easy to navigate and use on my smaller devices. 

The Auctioneer was carefully planned and designed to be responsive and work well on mobile, tablet and desktop devices.

## Manual Testing

Navbar

  - Tested on all screen sizes to confirm it is positioned correctly.
  - Tested on small screens to confirm dropdown menu appears.
  - User registration, login and logout were tested.
  - All links and buttons were tested to make sure they work
  - All components were tested  on all screen sizes to confirm it is positioned correctly.

Home page

- Tested on all screen sizes to confirm it is positioned correctly.

Register and login

  - Form was tested to confirm it inputs data correctly. 

Profile 
  - Profile page was tested to make sure it correctly displays user info.

Product page and Auction page
- Tested to make sure all products are visible and responsive.
- Redirect to checkout was tested.
- Search bar was tested to see if it works correctly.
- Pagination was tested to confirm if it works correctly and is hidden when only one mage is needed.
- Product buttons were tested to confirm add to cart correctly
- Add product quantity was tested to confirm selected quantity is added.
- Auction page is tested to confirm all elements are displayed properly on all screen sizes.

Cart and Checkout
- Cart page was tested to confirm correct products were added.
- Cart buttons were tested to confirm they redirect properly.
- Checkout button was tested to confirm it is shown when they are items in the cart and disabled when cart is empty.
- Checkout page was tested to confirm forms were displayed correctly.
- Payment forms were tested to confirm they work properly.
- When correct data is entered message displayed is: You have successfully paid.
- When incorrect data is entered message displayed is: Your card was declined!

Footer
- Footer was tested to confirm it is always positioned at bottom  of the page on every screen size
- Footer social network links were tested to confirm they open in new tab and change color on hover.

### Python Testing

#### How to run Python tests

To run the existing Python tests:
1. Activate your virtual environment.
2. In the terminal enter the following command:
```
python manage.py test
```
3. If you wish to run the tests within a specific app only you can specify with: 
```
python manage.py test <app name here>
```
4. The test results will be shown within the terminal.

_NOTE: The `python` part of these commands assumes you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_