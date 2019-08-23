[![Build Status](https://travis-ci.org/JordenCI/UnicornAttractor---Milestone-4.svg?branch=master)](https://travis-ci.org/JordenCI/UnicornAttractor---Milestone-4)

# Solutions iO

The purpose of this project was to create a website that users can store and easily access cooking recipes.

The purpose of this project was to build a full-stack site based around business logic used to control a centrally-owned dataset.
I set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the ability to pay to upvote features.


Deployed project below:

[Solutions iO](https://unicornattractor-msp.herokuapp.com/)

## UX

The website was designed for users of the fictional 'Unicorn Attractor' site to submit bugs, feature requests and general discussion posts
as well as to view statistics on how we handle these requests. On the homepage I have immediately provided links for users to navigate around the
site for ease of use. Users are able to navigate the site and view the resources without being registered however need to sign up to be able to
submit any bugs, feature requests or forum posts.

### User stories

- A user notices a bug on the Unicorn Attractor website and wants to submit it to be fixed.
- A user believes a certain feature would be a good addition to the Unicorn Attractor site and wants to submit that feature request.
- A user is interested in how many bugs/feature requests are being submited via our site.
- A user notices a bug and wants to check if this has already been submitted (via the search function).
- A has an idea for a feature however wants to check if something the same or similar has already been requested (via the search function).
- A user wants a general discussion with fellow users therefore visists our forum section.

## Wireframes


1. [Homepage - Desktop wireframe]()

- Initially on the homepage I planned to display features and bugs however opted to move these to their own page.

2. [Homepage - Mobile wireframe]()

- Mobile view is the same as desktop view.

3. [Base template - Desktop & Mobile wireframe(no difference other than navbar collapsable)]()

- I planned to display a Navbar and Footer in my base.html with the option to view/hide elements depending on if the user was logged in or not.
- Since then i decided to show all to non registred users but restricted their ability to interact throughout the site.

4. [Bugs, Features and Forum post - Desktop Wireframe]()

- This remained similar to my origial wireframe with the exception of displaying the items in rows instead of blocks. I also opted to add the image headers on each page.

5. [Bugs, Features and Forum post - Mobile Wireframe]()

- Again this remained similar to the original wireframe.

6. [Bugs, Features and Forum post detail - Desktop & Mobile Wireframe]()

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
- Icons which link to differnt parts of the site.

3. Bugs, features & forum pages.
- Submit item button allowing users to submit requests if registered.
- Completed item button which displays completed items (archive).
- Pagination to only display the 1st 5 items per page.
- Ability to see views, feature upvotes and amount of comments per item as well as when it was posted and sorts by most recent.
- Progress bars displaying the status of the item.

4. Detailed bugs, features & forum pages.
- As well as all the above features users can also comment on the item within the detail page.

5. Features pages.
- If the user is to upvote a feature the item is added to their cart where they can pay to upvote it at their convienece.

6. Profile page.
- Users can view all their submitted items here as well as submit new items or edit and delete existing ones.


### Features Left to Implement

In the future I would like to implement the below features.
- The ability for users to visit other peoples profiles to see what they have posted, upvoted and commented on.
- Some kind of reward system for active users who contribute consistantly to the site. They would recieve special badges etc.
- User admins as well as site admins. These would be active users who contantly use the site who would have certain privilages above not users but below site admins.

## Technologies Used

- [Bootstrap](https://getbootstrap.com/)
     - This was used for a basic HTML templates and styling.

- [Python 3](https://www.python.org/download/releases/3.0/)
    - The back end functionality of the application was written in python.

- [Django](https://docs.djangoproject.com/en/2.2/)
     - This project uses Django framework to provide a useful and comprehensible toolkit to a  build an effective web application. 

- [Stripe](https://stripe.com/gb)
     - This project uses Stripe as a payment service for users and to ensure that all security checks are dealt with. 

- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
     - JavaScript was used to impliment the stripe payment system.

- [jQuery](https://jquery.com/)
     - This was used in conjunction with stripe.

- [Font Awesome](https://fontawesome.com/)
     - This was used for social icons in the footer.

- [Pygal](https://fontawesome.com/)
     - This was used for social icons in the footer.

- [Whitenoise](http://whitenoise.evans.io/en/stable/)
     - This project uses Whitenoise as a means of storing static files. 

- [SQLite](https://www.sqlite.org/docs.html)
     - This project uses SQLite as database to use locally.

- [PostgreSQL](https://www.postgresql.org/docs/)
     - This project uses PostgreSQL as a database to use globally.

## Testing

- I used [This HTML validator](https://validator.w3.org/) to ensure my code was legal.
- I used [This CSS validator](https://jigsaw.w3.org/css-validator/) to ensure my CSS was legal.
- I used [This Python validator](http://pep8online.com/) to ensure my Python was legal.

- I used a number of automated tests in conjunction with coverage and manually tested the areas not covered. Below I have documented the manual tests.

- Bugs, Features and Posts applications
1. If comment form is valid, comment displays in detailed view and also increments comment count by 1 so i am able to display how many comments each item has.
2. User is only able to upvote the same item once, if user attempts to upvote a second time an error message is displayed.
3. Added @login_required across the site to ensure only registered users can submit etc.
4. Updated views to validate if the user who created the bug is the same one viewing it. This is to ensure only the creator can edit/delete those items.
 
- Accounts application

1. If a contact form is submitted, the information is emailed to myself as well as redirecting the user to the index page and displaying a confirmaton message.
2. A confirmation message is displayed when a user logs in or out.
3. Error message is displayed correctly if user inputs incorrect details at login.
4. Correct error messages display if user is attempting to register with existing details, also success message appears on succesful reigstration.

- Cart application

1. A user can only add 1 unique feature to their cart at a time, error message is displayed if same feature is already in basket.
2. Deleting an item removes it from the cart.

- Checkout application

1. 

- Graphs application

1. Information on graphs reflects number of bugs and features on site.


- Viewport and responsive testing

1. Desktops & Laptops. 1024×768
    1. Displays as intended

2. Tablet. 800 x 1280
    1. Displays as intended.

3. Mobile Galaxy S5 - 360 X 640, Pixel 2 - 411 x 731, Pixel 2 xl - 411 x 823, iPhone 5 - 320 x 568, iPhone 6,7,8 - 375 x 667, iPhone 6,7,8 Plus - 414 x 736, iPhone x - 375 x 812.
    1. Displays as intended

## Deployment

1. New Heroku Python App created.
2. Launched Heroku in the C9 environment.
3. Initiate new Git repository and run git remote add Heroku https://git.heroku.com/recipe-milestone-project.git to allow a push to the Heroku server.
4. To prevent a "push fail", the requirements.txt was updated using the following command sudo pip3 freeze --local >requirements.txt to keep track of dependancies.
5. A Procfile was created using the following code: echo web: python run.py > Procfile to inform Heroku which file to run for initiating the app.
6. To ensure that Web Processes are running the following command line was run in C9: Heroku ps:scale web=1.
7. Config Vars set as follows: IP=0.0.0.0 and PORT=5000.
8. Lastly, dynos were restarted in Heroku app.
9. Code added, committed and pushed to both GitHub and Heroku.
10. App launched successfully.
11. In addition, you can clone or download the code from this GitHub repository.


### Content
- The image URLs and recipe content were sourced from the [BBC site](https://www.bbcgoodfood.com/recipes).
- The main banners were sourced from [Pexels](https://www.pexels.com/) who advise all photos can be used for [free](https://www.pexels.com/photo-license/).
  
### Acknowledgements

- I received inspiration for this project from a combination of the mini projects leading up to this.
- The Slack community have been great on giving me feedback on my project (Shane Muirhead in particular has been very helpful).
- The tutors at code institute have also been helpful.
- My mentor Jim Richmond has supported with feedback on the project.