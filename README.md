[![Build Status](https://travis-ci.org/JordenCI/UnicornAttractor---Milestone-4.svg?branch=master)](https://travis-ci.org/JordenCI/UnicornAttractor---Milestone-4)

# Solutions iO

The purpose of this project was to build a full-stack site based around business logic used to control a centrally-owned dataset.
I set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the ability to pay to upvote features.


Deployed project below:

[Solutions iO](https://unicornattractor-msp.herokuapp.com/)

## UX

The website was designed for users of the fictional 'Unicorn Attractor' site to submit bugs, feature requests and general discussion posts
as well as to view statistics on how we handle these requests. On the homepage I have immediately provided links for users to navigate around the
site for ease of use. Users are able to navigate the site and view the resources without being registered however need to sign up to be able to
submit any bugs, feature requests or forum posts.

## User stories

1. A user notices a bug on the Unicorn Attractor website and wants to submit it to be fixed.
2. A user believes a certain feature would be a good addition to the Unicorn Attractor site and wants to submit that feature request.
3. A user is interested in how many bugs/feature requests are being submitted via our site.
4. A user notices a bug and wants to check if this has already been submitted (via the search function).
5. A has an idea for a feature however wants to check if something the same or similar has already been requested (via the search function).
6. A user wants a general discussion with fellow users therefore visits our forum section.

## Wireframes


1. [Homepage - Desktop wireframe](https://ibb.co/wKc62KR)

- Initially on the homepage I planned to display features and bugs however opted to move these to their own page.

2. [Homepage - Mobile wireframe](https://ibb.co/vqgcTj5)

- Mobile view is the same as desktop view.

3. [Base template - Desktop & Mobile wireframe(no difference other than Navbar collapsable)](https://ibb.co/qjHMfYD)

- I planned to display a Navbar and Footer in my base.html with the option to view/hide elements depending on if the user was logged in or not.
- Since then i decided to show all to non registered users but restricted their ability to interact throughout the site.

4. [Bugs, Features and Forum post - Desktop Wireframe](https://ibb.co/n1kc2wP)

- This remained similar to my original wireframe with the exception of displaying the items in rows instead of blocks. I also opted to add the image headers on each page.

5. [Bugs, Features and Forum post - Mobile Wireframe](https://ibb.co/PMbxhjn)

- Again this remained similar to the original wireframe.

6. [Bugs, Features and Forum post detail - Desktop Wireframe](https://ibb.co/1zZxJQJ)

- No major changes from the original wireframe here.

7. [Bugs, Features and Forum post detail - Mobile Wireframe](https://ibb.co/SfdyScd)

- No major changes from the original wireframe here.

8. [Graphs - Desktop Wireframe](https://ibb.co/sb5xjd2)

- No major changes from the original wireframe here.

9. [Graphs - Mobile Wireframe](https://ibb.co/Csf3117)

- No major changes from the original wireframe here.

## Features

1. Base template (navbar & footer)
- Navbar
    - Site logo to navigate back to homepage.
    - Home button to navigate back to homepage.
    - Login button for existing users to log back in.
    - Register button for new users to register.
      Once the user has logged in.
    - removal of login and register button.
    - Logout button to end their session.
    - Explore drop down to enable users to navigate the site from any html page.
    - Search bar enabling users to search for bugs, features and forum posts via key words.
- Footer
    - Contact form enabling users to submit contact requests.
    - Social media buttons which currently link homepage of the sites however would link to this websites social.

2. Index (homepage)
- Register button which is hidden if user is already registered. This is located in two places on the homepage for mobile users.
- Icons which link to different parts of the site.

3. Bugs, features & forum pages.
- Submit item button allowing users to submit requests if registered.
- Completed item button which displays completed items (archive).
- Pagination to only display the 1st 5 items per page.
- Ability to see views, feature upvotes and amount of comments per item as well as when it was posted and sorts by most recent.
- Progress bars displaying the status of the item.

4. Detailed bugs, features & forum pages.
- As well as all the above features users can also comment on the item within the detail page.

5. Features pages.
- If the user is to upvote a feature the item is added to their cart where they can pay to upvote it at their convenience.

6. Profile page.
- Users can view all their submitted items here as well as submit new items or edit and delete existing ones.


## Features Left to Implement

In the future I would like to implement the below features.
- The ability for users to visit other peoples profiles to see what they have posted, upvoted and commented on.
- Some kind of reward system for active users who contribute consistently to the site. They would receive special badges etc.
- User admins as well as site admins. These would be active users who constantly use the site who would have certain privileges above not users but below site admins.
- A live chat feature for users to directly message with admins.

## Technologies Used

Languages:
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python 3](https://www.python.org/download/releases/3.0/)
- [SQL](https://en.wikipedia.org/wiki/SQL)

Framework / Libraries
- [jQuery](https://jquery.com/)
- [Django](https://docs.djangoproject.com/en/2.2/)
- [Font Awesome](https://fontawesome.com/)
- [Stripe](https://stripe.com/gb)
- [Bootstrap](https://getbootstrap.com/)

Tools:
- [Whitenoise](http://whitenoise.evans.io/en/stable/)
- [Pygal](http://pygal.org/en/stable/)
- [Git](https://en.wikipedia.org/wiki/Git)

Databases:
- [SQLite](https://www.sqlite.org/docs.html)
- [PostgreSQL](https://www.postgresql.org/docs/)


## Automated tests
### Validation services
- I used [This HTML validator](https://validator.w3.org/) to ensure my code was legal.
- I used [This CSS validator](https://jigsaw.w3.org/css-validator/) to ensure my CSS was legal.
- I used [This Python validator](http://pep8online.com/) to ensure my Python was legal.
    - I also used [autopep](https://pypi.org/project/autopep8/) to format my python code systematically.
- I used a number of automated tests which can be found in the test.py files in each applications folders.

### Stripe payment testing
Please use the below information to test payments.
- Card number - 4242424242424242
- CVC - 111
- Expiry date - Any date in the future.

Due to the below statement payments with be successful if a use provides a blank CVC. I have however added validation if a user was to enter an incorrect CVC.
By default, passing address or CVC data with the card number causes the address and CVC checks to succeed. If this information isn't specified, the value of the checks is null. Any expiration date in the future is considered valid.
You can also provide invalid card details to test specific error codes resulting from incorrect information being provided. For example:
invalid_expiry_month: Use an invalid month (e.g., 13)
invalid_expiry_year: Use a year in the past (e.g., 1970)
invalid_cvc: Use a two digit number (e.g., 99).

## Manual tests

- Bugs, Features and Posts applications
1. If comment form is valid, comment displays in detailed view and also increments comment count by 1 so i am able to display how many comments each item has.
2. User is only able to upvote the same item once, if user attempts to upvote a second time an error message is displayed.
3. Added @login_required across the site to ensure only registered users can submit etc.
4. Updated views to validate if the user who created the bug is the same one viewing it. This is to ensure only the creator can edit/delete those items.
 
- Accounts application

1. If a contact form is submitted, the information is emailed to myself as well as redirecting the user to the index page and displaying a confirmation message.
2. A confirmation message is displayed when a user logs in or out.
3. Error message is displayed correctly if user inputs incorrect details at login.
4. Correct error messages display if user is attempting to register with existing details, also success message appears on successful registration.

- Cart application

1. A user can only add 1 unique feature to their cart at a time, error message is displayed if same feature is already in basket.
2. Deleting an item removes it from the cart.

- Checkout application

1. Check that customer data form validates correctly.
2. Check that customer payment form validates correctly.
3. Display error messages for incorrect payment details.
4. Provide success message for successful payment.
5. Feature upvote is incremented by 1 on successful payment.

- Graphs application

1. Information on graphs reflects number of bugs and features on site.


- Viewport and responsive testing

1. Desktops & Laptops. 1024×768
    1. Displays as intended

2. Tablet. 800 x 1280
    1. Displays as intended.

3. Mobile Galaxy S5 - 360 X 640, Pixel 2 - 411 x 731, Pixel 2 xl - 411 x 823, iPhone 5 - 320 x 568, iPhone 6,7,8 - 375 x 667, iPhone 6,7,8 Plus - 414 x 736, iPhone x - 375 x 812.
    1. Displays as intended

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [AWS C9](https://aws.amazon.com/cloud9/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

### Instructions
1. Save a copy of the github repository located at https://github.com/JordenCI/UnicornAttractor---Milestone-4 by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/JordenCI/UnicornAttractor---Milestone-4
```
2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. Install all required modules with the command 
```
pip -r requirements.txt.
```
4. Attempt to run project where you will get an error message displaying your host name.
```
python3 manage.py runserver $IP:$PORT
```
5. In your settings.py file add your hostname under 'ALLOWED_HOSTS'.

6. Create a [stripe](https://stripe.com/gb) account and get your API keys.

7. In your local IDE create a file called `env.py`.

8. Inside the env.py file create the below variables.
    - SECRET_KEY
    - STRIPE_PUBLISHABLE
    - STRIPE_SECRET
    - DEFAULT_FROM_EMAIL
    - SERVER_EMAIL
    - EMAIL_HOST
    - EMAIL_HOST_USER
    - EMAIL_HOST_PASSWORD

9. You can now re-run the runserver command to view local project.
```
python3 manage.py runserver $IP:$PORT
```


## Heroku Deployment

To deploy Family Hub to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
SECRET_KEY | `<your_secret_key>`
STRIPE_PUBLISHABLE | `<your_stripe_publishable>`
STRIPE_SECRET | `<your_stripe_secret>`
DEFAULT_FROM_EMAIL | `<your_from_email>`
SERVER_EMAIL | `<your_server_email>`
EMAIL_HOST | `<your_email_host>`
EMAIL_HOST_USER | `<your_host_user>`
EMAIL_HOST_PASSWORD | `<your_host_password>`

8. In the Heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

## Content
- The images used on the page headers were sourced from (https://www.pexels.com/)
  
## Acknowledgements

- I received inspiration for this project from a combination of the mini projects leading up to this.
- The Slack community have been great on giving me feedback on my project (Shane Muirhead in particular has been very helpful, even to go as far as to setup an email for me on his personal server!).
- The tutors at code institute have also been helpful.
- My mentor Jim Richmond has supported with feedback on the project.