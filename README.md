# ChemLab50
#### Video Demo:  <[URL HERE](https://www.youtube.com/watch?v=X91SB5OZHDk)>
#### Description:

# Tools 
I developed ChemLab50 locally on my pc instead of using my github codespace. I built ChemLab50 with Python and the Flask Framework, I used javascript to make the app more interactive and fun and I made use of sqlite3 to store users data in databases. This includes information such as; log in information and lab book entries.

# About
When designing ChemLab50 my main thought was to help school students like myself find a interest in chemistry and make learning chemistry a fun process. The app has a secure register and a log in and log out system to allow for features such as, a personal lab book. The two main features of the site are an interactive peridodic table and an online lab book. The periodic table contains all the known chemical elements. Hovering over an element will enlarge it and clicking on it will display the atomic number, the atomic mass and the chemical group. Elements from the same element group are displayed with the same chemical number. For the lab book feature, I created 3 distinct templates. The first displayed all the user's previous entries as well as a button to add a new entry. Upon clicking on one of a previous entry the user can edit it and then save the edited copy. Similarly, by pressing on the button to add a new entry, the user can fill in a new lab book entry and save it. Finally, the homepage of the app displays a welcoming message and a random quote about chemistry.

# Static Files
## logo.jpg
The file logo.jpg is my web app's logo. I designed it using the free features of canva. The colours have been carefully chosen to suit the colours of the web app interface.

## script.js
The script.js contains two javascript functions and two further lines of code that don't belong to a function. The first called expand is in charge of expanding the elements when the users click on them to view information about the specific element. It takes one parameter named id so as to identify the html element that needs to be expanded. This function is called for each of the 118 periodic elements, each time with a different parameter referring to the periodic element's unique id. I tried to find a way to access the expand the element that was clicked without using a parameter, and, therefore, without having to assign each periodic element a unique id, but the approach I took in the end looked most straightforward to me. The function expand initially loops through all of the periodic elements removing the expanded class from any element that is expanded to return all the elements to the original size and adding the hover class so that the user can enlarge them by hovering on them. Next up, the function checks whether the element that has been clicked on is already expanded or not. If the element is already expanded the function adds the hover class and removes the expanded class to close the expanded element. If the element the user clicks on is not expanded, the function adds the expanded class and removes the hover class so the user can view additional information about the periodic element without the size of the text changing upon being hovered over. The second function takes as input from the user the moles of two reagents and calculates the equivalence before inserting it automatically into the lab book entry. Lastly, the two lines of code at the end of the function generate random quotes for the web app to display. The first line is an array of quotes. Inserts a random quote into the html template using the functions math.floor() and math.random() to generate a random integer from 0 to 2 to pick a random element from the array.

## style.css
Except for making minor changes to various elements the style.css file plays an important role in the arrangement of the periodic table. First of all, it classifies the div that containts the periodic table as grid. Furthermore, the gaps in the periodic table are made possible by the style.css file that indicates how long they should span. Lastly, the style.css file makes expanding the elements possible with the expandable and expanded classes and gives the periodic elements their colour that corresponds to their chemical group. Moreover, the style.css file styles the navigation bar. The main font I used in this project is Brush Script MT.

# helpers.py
The code in helpers.py includes only the login required function that is used to indicate which app routes need the user to log in to access.

# app.py
The app.py file handles what happens in every route of the app. It is in charge of rendering all the html templates with the necessary database data including the apology.html template in case of an error. It hashes the password upon registering, it handles input from forms and inserts it into the database. 

# Templates

## layout.html
Layout.html is the html template that all the other templates extend. This file imports the css and javascript files. Two different navigation bars are shown based on whether the user is signed in or not. If the user is not signed in the navigation bar will include the web app's logo and two navigation links, one to login and one to register. Otherwise, if the user is signed in the navigation bar contains the log, a navigation link to the welcome page named 'Home', a navigation link to the interactive periodic table named 'Periodic Table', a navigation link to the lab book named 'Lab Book' and a navigation link to logout named 'Logout'.

## register.html
The register.html template contains a form requesting the necessary information to register a user. In the app.py file the password is hashed and the username and password are store in the sql users table.

## login.html
This template also contains a form, the information submitted from the form is checked in the app.py file. By logging in the user gains access to the main features of the page.

## apology.html
Apology.html is the template that is rendered when the user makes a mistake, mainly when the user doesn't provide all the information for a form. This template simply renders an apology message. 

## welcome.html
The welcome.html template displays a welcome message together with a randomly picked quote about chemistry. The quote is picked randomly using the javascript code mentioned beforehand. Reloading the site will most probably show a different random quote.

## index.html
The index.html file is the file that displays the periodic elements which are styled to look like a periodic table by the styl.css file. Each periodic element is represented by a div tag which contains a unique id for every periodic element, the classes element hover expandable and one more depending on the chemical group and some code so that it can be expanded upon being clicked on. I contemplated trying to write a loop with javascript so as to avoid the many repetitions in the index.html file. However, I would stil have had to write a massive array which would include all the periodic elements. Despite this fact, it would still probably have been a better decision to use a loop.

## labbook.html
The labbook.html file displays a list of all the users entries with their title(the user can click on them to edit them) and the date they were created and a button to add a new entry that leads to new route in the web app.


## entry.html
In entry.html file the user can write a lab book entry that upon clicking the save entry button gets saved to the database. The user doesn't need to write the date since it is entered and saved automatically. Furthermore, when the user writes the moles of the reagents the equivalence is calculated automatically from the script.js file.

## edit.html
This template is very similar to the entry.html template except that it is used to edit entries. All fields are filled in with the previous values of the entry and upon saving the entry, instead of adding a new row to the database the row of the entry being edited is updated with new values.

# Improvement
Every project can definitely be improved endlessly. I have some ideas to improve my project which I will definitely try to make. Here is the list:
- Improve the interface perhaps by incorparating bootstrap into the project
- Give the user the option to download his lab book entries as pdf file
- Allow the user to upload photos to the lab book. I had written some code for this feature, but didn't use it because of security issues with the photos getting intercepted and i didn't want to create a web app that is practically useless due to glaring security flaws.
- New features:
    - Chemical equation balancer
    - Fun learning features such as, flashcards 