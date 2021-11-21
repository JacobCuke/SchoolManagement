# SchoolManagement

Web Application and API for the management of a high school database.

## API Documentation

View the full API documentation here: [Postman Documentation](https://documenter.getpostman.com/view/15328019/TzJrBeLq)

## Relational Model
<img src="https://raw.githubusercontent.com/JacobCuke/SchoolManagement/master/schema/relational_model.png"></img>

## Database Schema
<img src="https://raw.githubusercontent.com/JacobCuke/SchoolManagement/master/schema/database_schema.png"></img>

## Fork Instructions

[Video tutorial](https://www.youtube.com/watch?v=HbSjyU2vf6Y&ab_channel=TheNetNinja)

1. Click the 'Fork' button in the top right corner of the page to make a copy of this repo on your account

2. Head over to your copy of the repo and click the green 'Code' button and copy the repo URL

3. Open up your terminal and type `git clone <paste URL here>`

4. Move into the project folder with `cd SchoolManagement`


## Run Instructions

1. Make sure you have Python and pip installed on your machine. Check that it installed correctly by typing `pip --version`<br><br>
*I recommend using a virtual environment for Django but it's not necessary*<br>
[Virtual Environment Setup (Windows)](https://www.youtube.com/watch?v=APOPm01BVrk&ab_channel=CoreySchafer)<br>
[Virtual Environment Setup (MacOS/Linux)](https://www.youtube.com/watch?v=N5vscPTWKOk&ab_channel=CoreySchafer)<br><br>
  
  
2. Inside the project folder there will be a `requirements.txt` file containing all the packages that need to be installed to run the Django app.
This is based on a previous project I did, and we may not end up using them all<br><br>
Install them using the command: `pip install -r requirements.txt`<br><br>


3. Finally, run the server with: `python manage.py runserver`<br><br>
Type in `localhost:8000` in your browser to access the site<br>
Quit the server with CONTROL-C (COMMAND-C on MacOS) in the terminal


## Access the Admin Page

**First thing you'll want to do once you get the program running is create a superuser for yourself**

1. Stop the server and run the command: `python manage.py createsuperuser`

2. Follow the instructions and enter your username, email and password (these are stored securely so feel free to use whatever password you want)

3. Run the server again and navigate to `localhost:8000/admin` and login with your new credentials


## Make Contributions

**Before pushing your code make sure it's up to date with the original repo.**

1. Add the original repo as a remote, call it "upstream"<br><br>
`git remote add upstream https://github.com/JacobCuke/SchoolManagement.git`

2. Fetch to update your remote-tracking branches<br><br>
`git fetch upstream`

3. Make sure that you're on your master branch<br><br>
`git checkout master`

4. Update your local repo with the original master<br><br>
`git rebase upstream/master`<br><br>

**Now you can commit and push as normal**

5. Add your changes to the staging area<br><br>
`git add .`

6. Commit them to your local repo<br><br>
`git commit -m "Meaningful commit message"`

7. Push them to your remote repo<br><br>
`git push origin master`<br><br>

**Now all you need to do is go create a Pull Request**

8. Go to you GitHub profile and navigate to the repo containing your version of the project

9. Create a new pull request, and leave a short description of the modifications you made

10. I will see the pull request and after confirming there are no conflicts I will merge your changes into the original repo




