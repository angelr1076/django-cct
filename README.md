# CS50 Web with Python and JavaScript Capstone Project

Designing and implementing a web application of your own with Python and JavaScript.

## Case Crime Trace (CCT)

### Requirements

In this project, you are asked to build a web application of your own. The nature of the application is up to you, subject to a few requirements:

- Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza project), and more complex than those.
  - A project that appears to be a social network is a priori deemed by the staff to be indistinct from Project 4, and should not be submitted; it will be rejected.
  - A project that appears to be an e-commerce site is strongly suspected to be indistinct from Project 2, and your README.md file should be very clear as to why it’s not. Failing that, it should not be submitted; it will be rejected.
- Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
- Your web application must be mobile-responsive.

### The Project

CCT utilizes Django on the back-end, and HTML, CSS and JavaScript on the front-end. The site is mobile responsive and fits all screen sizes from small mobile to wide-screen desktop presentations.

Case Crime Trace allows users to report crimes and suspects in any given area of the U.S. The app presents the user with several options to report both crimes and suspects whether they are logged in or acting as an anonymous user. The benefits of registering and using the app while logged in (this is explained via a navbar JavaScript modal) is that the crime or suspect record attaches to that user ID via a one-to-one relationship to that user. Reporting while logged in allows the user to track crimes and suspects along with being able to edit the description sections of crime or suspect records they reported. Registering also allows the user to create a profile and "Spot" suspects, populating a list of users that have spotted a given suspect.

If the user is a staff member, they are considered an officer (denoted in all of the user's profile screens). Officers can update any crime or suspect record, so long as it is not a solved crime or an apprehended suspect. There are separate screens for all active crimes, all solved crimes and all crimes that the logged in user has reported. The same goes for suspects since there is an individual screen for suspects that are on the run, suspects that have been apprehended, and suspects that the logged in user has reported.

CCT also utilizes Django's built in messages framework, giving the user feedback when certain actions are taken and also when errors happen. On the Crimes, Crimelist (user's own reported crimes), Suspects and Suspectlist (user's own reported suspects) pages, users can update the description of either a crime or suspect and are given feedback via JavaScript, without a page refresh that a record has been updated. This is done via the fetch API through PUT requests. JavaScript also drives the modals used to inform users about the project and through Crime and Suspect submission forms. The project uses the Paginator class and Bootstrap's pagination for indexed page displays. There is also a page that lists all users that are officers (only logged in users can see this), along with the officer's email address.

This app deviates from the Django projects assigned throughout the course since it uses a better separation between models, templates and static files. It is more complex in separating models and views via their own folders, but also makes it easier to track between models, templates and views for a given application model by separating these folders by name.

The project consists of a static folder to house all static css, JavaScript and image files. There is also a separate webfonts folder for special icons used throughout CCT. Again, each model (Crime, Member, Suspects) has its own separate set of folders including URLS, models, admin, context processors, multiple-choice and views files. Templates are housed in their own individual folders with subfolders for each model representation.

A requirements.txt file is included with the project and includes all required packages. Prior to starting the server, you will want to go to the root folder 'casecrimetrace' and be sure you are in the same folder that contains the manage.py file and run 'pip install -r requirements.txt' in the terminal. Once that's done, call 'python manage.py runserver' in the terminal to view the project. When logged in, users have the option to create a profile, but this is not mandatory. There is also a guest login if you choose not to register as a new user. The login name is guestuser and the password is guestpass.
