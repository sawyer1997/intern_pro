# intern_pro
The idea behind the project is to build a simple competition webpage that encourages people to spread the news about a new product. Users arrive at the page and sign up a form. After a successful sign up, they get one entry for the competition. At that point, they also have an option to share the sign up link. Every successful sign up referred via the link will give extra competition entries to the original link poster. There is no limit to the number of entries that a person can have. So the idea is: The more entries you have, the higher your chance to win the prize. The prize is 100 bottles of Honeymint. The top 10 persons with the most entries will win the prize.   

## Requirements: 
1. The duration of the competition will be 1 month from the day it is launched. After that, the webpage will be removed. 
3. The webpage will consist of text, graphical elements and a sign up form. 
4. The sign up form will consist of the following compulsory fields: First name, Last name, Mobile Number and Email Address. 
5. When the form is submitted, the user will receive an EDM (Electronic Direct Mail) with an option to post a special link to the competition page from his/her Facebook or twitter account. 
6. When people arrive to the competition page via the special link and signs up the form. The original poster will get one more extra entry for the competition. 
7. After the competition has expired, provide a list of winners to the client. Please develop the code for this scenario as per your understanding.


## How to run the project:
   Back-end has been done in Django (Python) and Front-end has been done in ReactJS. Since the major focus was on back-end, so a very basic form has been created in React, with redirects and all.
   
   1. We need to create virutal environment for the Django project to run in, and that can be done by using `python -m venv my_env`, but please make sure to have `Python 3.7.5` or higher version.
   2. After that we need to install dependencies needed to run the project, and that can be done by using `pip install -r requirement.txt`.
   3. Then we need to activate the environment, using `source my_env/bin/activate`, we can deactivate also using `deactivate`.
   4. Now clone the project, and change the directory inside it.
   5. Run the local server using `python manage.py runserver`, please kill the process, if it's already using `port:8000`.
   6. Now, our local backend server has been started, we can check the databases, using link `localhost:8000/admin`
   
Now, we need to run the front-end server as well.

  1. Please make sure to have `npm` installed already.
  2. Now run `npm start`, the local server will get start to `port:3000`, if it's occupied kill the process, and the try again.
  If everything is fine so far, then we can see a very basic form in the browser. We can fill the form, and can check the database that entry has been done or not, and there will be a message appear on the browser, that `Congrats! You've been registered!`.
