# Nurturelabs-Intern-Assignment
Assingment 1


NurtureLabs Intern Assignments
Deadline: There is no deadline just submit the assignment as soon as possible since we will be accepting submissions until the vacant slots fill up.

Here is a video showing the kind of work we do here and our process in breaking down a task (it has nothing to do this the assignment task below) https://drive.google.com/file/d/116NKfLqFEkI0nyQRPEOpshw3qj_3pXUR/view?usp=sharing
Currently there are 4 out of 6 slots available
We’ll update the above number as the slots fill up

If you wish to be notified of more roles opening up at Nurture Labs please join this google group
Internship Assignment (Python/Django)
Make APIs using Django for an advisor network where users can come and book an advisor for a call.
The following roles should be allowed
Admin
API: Add an advisor
Method:
POST
Authentication
Not needed for this assignment
Endpoint: 
/admin/advisor/
Request:
Advisor name
Advisor Photo URL
Response:
No Response
Just return 200_OK if the request is successful
Return 400_BAD_REQUEST if any of the above fields are missing
User
API: Can register as a user
Method:
POST
Endpoint: 
/user/register/
Request:
Name
Email
Password
Response:
Body:
JWT Authentication Token
User id
Status
200_OK if the request is successful
400_BAD_REQUEST if any of the above fields are missing
API: Can log in as a user
Method:
POST
Endpoint: 
/user/login/
Request:
Email
Password
Response:
Body:
JWT Authentication Token
User id
Status
200_OK if the request is successful
400_BAD_REQUEST if any of the above fields are missing
Return 401_AUTHENTICATION_ERROR if the email/password combination was wrong
API: Get the list of advisors
Method:
GET
Endpoint: 
/user/<user-id>/advisor
Request:
None
Response:
Body:
An array of advisor objects with each object having
Advisor Name
Advisor Profile Pic
Advisor Id
Status
200_OK if the request is successful
API: Can book call with an advisor
Method:
POST
Endpoint: 
/user/<user-id>/advisor/<advisor-id>/
Request:
Booking time (a DateTime string)
Response:
Body:
None
Status
200_OK if the request is successful
API: Can get all the booked calls
Method:
GET
Endpoint: 
/user/<user-id>/advisor/booking/
Request:
None
Response:
Body:
An array of advisor objects with each object having
Advisor Name
Advisor Profile Pic
Advisor Id
Booking time
Booking id
Status
200_OK if the request is successful
There is no need to make the UI or any pages for this. We only need the APIs to perform the above functions as our internal team is decoupled into backend and frontend roles, and you’ll be only working on the backend side
Add the dummy data to test the APIs accordingly
Take the necessary assumptions from your end to complete the above APIs
Put this code in a public repo on Github
Deploy the above made Django code base on Heroku on a free tier server
You can test your APIs using Postman
If you don’t know any concept or part of this, try to learn things from the numerous tutorials available online. Learning things on the go and just enough to get the job done is a highly coveted skill in this industry.
No doubts will be entertained regarding this test. That being said, partial submissions are better than no submissions.
Structure your submission like this and send it to tech@nurturelabs.co with the subject “Backend Dev Intern Application Django”.
Your Name
The location you’re currently at
Github Link
Heroku Deployment Link
Postman link to import collection 
Specify the earliest date you can join from if you do get selected. We’ll need you to work for at least 9 hrs a day from Monday to Friday, so if you’ll not be available for that please let us know that too
Attach your resume or link your updated linkedin profile

If you wish to be notified of more roles opening up at Nurture Labs please join this google group

