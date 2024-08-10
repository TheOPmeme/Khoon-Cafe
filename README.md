# KhoonCafe Website

pt1: Project Planning and Design

Target Audiences: Students, Staffs etc.

Objective of the project;
Main functionality.
Khoon Cafe website will be used to make ordering and collecting food items much more efficient and convenient, where customers will be notified when their orders are ready to be collected, especially with larger crowds. A number queuing system would also be set-up on the web to show how crowded the cafe is, letting users decide whether to order on spot rather than having to go to the cafe to check out.

Implementation of main.
USER PAGE
Menu:
Obviously, a menu of the items available will be required, there's also a possibility of an item being sold out and the quantity of the item required to be purchased to be more than 1, which will need to be worked on

Redirect Page to Payment Page:
Confirm with user (verify) the order (maybe using table of data here for the menu might work) before redirecting them to payment [You can choose cash payment or cashless payment] --> may lead to some issues like wrong payments or change of mind of purchase when food is prepared, so have to pay first cashless most likely

Queue Number:
Each day, counter will be set to 0, each order increases the number by 1, regardless physical on website, to a max order number of 999, and whichever was the latest to be marked would be presented

Notification (optional):
Using either email, WhatsApp or SMS (will need to self-find, outside CS50 view)


STAFFS PAGE
Sending of data to staffs:
Using a database would definitely help, WHERE UPDATING THE DATA EVERY 20 SECOND might be necessary
..different colors for payment methods, though most likely only online, so payment has to be made for order to go through

Notification:
With a click of a button on whichever order is done, the order will be made for collection


Some flaws:
If some directly orders from the cafe, Staffs will have to manually recalibrate order number in the database, maybe putting database info as NULL might help, but this is definitely MANUAL and a bit tedious for the staffs to keep track


Other functionalities:
.Login via Email and Username --> password will be considered
..Allows for records of previous purchases to be stored and give them possible suggestions of what they would like to order

.A rewards function (possible implementation)

.feedback form --> split into either for the website, food choices and prices, or anything miscellaneous

.about page for idk what on the home screen, can act for work timings and availability
