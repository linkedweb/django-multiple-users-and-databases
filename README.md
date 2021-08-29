# Django Real Estate App With Multiple Users And Databases

This is a project that demonstrates how you can use multiple user types and multiple databases in Django. This is strictly a Django backend REST API using the Django REST Framework.

In order to test out this project, follow these steps:

-   clone the repository

Then create 2 databases in postgreSQL, one called **listingz_users** and one called **listingz_listings**

Then under core/settings.py:

-   find the DATABASES setting, set the PASSWORD field to both your databases password to your postgreSQL user password

Once you have your databases setup, proceed to the following steps:

-   create a virtual environment by running: python3 -m venv venv
-   then activate the virtual environment: source venv/bin/activate (MacOS) or .\venv\Scripts\activate (Windows)
-   then run the following commands:
-   pip install -r requirements.txt
-   python manage.py makemigrations
-   python manage.py migrate user --database=users
-   python manage.py migrate --database=users
-   then run the following to create a superuser:
-   python manage.py createsuperuser --database=users
-   then you can run the server by running: python manage.py runserver
