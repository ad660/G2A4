## Welcome to our Hogwarts Librarian API! 

In order to use this you will need to first update the placeholders in the config.py file with your user and password details for the SQL database.
You can find/update these in the Administration panel of SQL Workbench under 'Users and Privileges'.

After this you will need to ensure that you have mysql, mysql.connector and flask installed. You can do this in PyCharm by hovering over the import and clicking install or by 
going into your terminal and running pip install mysql.connector, pip install mysql and pip install Flask.

You will also need to run the database on your mysql_workbench, the sql file is named 'Hogwarts_Library.sql'.

Once these steps have been completed, you will then need to run the dub_utils.py, app.py, to define the functions and start the server.
After this you can run the main.py file.
Once you run the main.py file your app will begin, and you will be able to use our API. 

1. It will ask you for your name to sign in as the Hogwartian Librarian.
2. It will ask if you'd like to see the options available to you to choose from as the Librarian, select [y] to view options.
3. It will give you a selection of options to choose from:
   - View all books.
   - View all students.
   - Select a student by student ID to view the books they have on loan.
   - Add a new book (feel free to get creative with the name etc!)
   - Add a new student

We hope you enjoy using our Hogwarts Library API!

### Happy Hogwarting! 