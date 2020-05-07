# Dark Mode

Readme file](https://github.com/sWrAAb/Auctioneer/blob/master/README.md)

To change appearance on click I used [Darkmode.js](https://darkmodejs.learn.uno/) library.

- It appears it does not work well with python so I made some adjustments.
Darkmode works great for most of the content but some elements were not included when the library was activated (products from database, buttons and forms) so I had to add them manually with jQuery.
It has some included options like save to cookies so website stays darkened but I had trouble to make jQuery do the same. When I navigate to another page on my website, it remains darkened but jQuery does not stay toggled and since I failed to make jQuery to detect if darkmode class is active I decided not to select cookies. When dark mode is activated it remains until page is refreshed.

- Another option is widget location. Options only allow to select distance from the bottom, not from the top, which does not agree with different screen sizes. In the future I will find a way to  place it on the navbar, which I made sticky so its always visible. Also had to add z-index to widget because it was under product elements on small screen sizes.

- Darkmode does not work with disabled buttons. When cart is empty, checkout button is disabled but the widget or jQuery were not able to change the color of the button. Another option was to hide button completely when cart is empty.
