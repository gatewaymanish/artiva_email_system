# artiva_email_system

- Before running this code ensure you have python3 in your machine.
- Checkout the code from github repo from below url:
    https://github.com/gatewaymanish/artiva_email_system.git
- Open cmd/bash and get inside the project directory where manage.py file consist.
- Run "pip install -r requirements.txt" to install third-party libraries.
- Run "python manage.py createsuperuser" and follow steps to add your email for testing admin reporting feature.
- Run "python manage.py runserver --noreload" to run the application.
- After running the application, open your browser open below url:
    "http://localhost:8000/email/sendemail"
- The browser will display basic email interface where a user can enter email fileds like to, subject, message etc.
- The UI also incorporates uploading a csv file for adding list of recipients.
- The "send" button sends an email and redirect to the acknowledge page.
- The UI gives error if you will try to upload a non-csv file or a larger csv file.


