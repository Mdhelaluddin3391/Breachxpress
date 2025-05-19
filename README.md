# BreachXpress

**BreachXpress** is a web application built using Django as a final project for [CS50x](https://cs50.harvard.edu/x). It is a platform that empowers users to **anonymously expose corruption** and share stories for the sake of **justice** and **humanity** without fear of identity disclosure.

---

## Motivation

In many parts of the world, people hesitate to report corruption due to fear of retaliation. BreachXpress was developed to solve this problem by giving people a **safe, anonymous platform** to submit their stories without any login or tracking system.

---

##  Live Demo

 [https://breachxpress.onrender.com](https://breachxpress.onrender.com)

---

##  Features

-  Submit stories anonymously using a rich text editor (CKEditor).
-  No login system or cookies — your identity is never stored.
-  Admin can review and publish submitted stories to the public.
-  Community section (under development) where users will collaborate and support each other.
-  Mobile-friendly and responsive design.
-  Built-in protection for large file uploads.

---

## Project Structure

BreachXpress/
├── Breach/ # Main Django app (views, URLs,
│      └── models, templates, static etc.
├── manage.py # Django entry point
├── db.sqlite3 # Default local database
├── requirements.txt # Python dependencies
etc.


---

##  Technologies Used

- **Django**
- **HTML / CSS / JavaScript**
- **SQLite** (will be upgraded to PostgreSQL later)
- **CKEditor** for story submission
- **Render** for deployment

---

##  How to Submit a Story

Go to the [Submit Story](https://breachxpress.onrender.com/submit/) page and use the editor to write your content. Click **Submit** — that’s it. No login, no identity exposure.

---

##  Settings Configuration Notes

This project supports both **local development** and **production deployment** (e.g., Render). Follow these steps accordingly.

###  For Local Development:

1. **Comment out** these production-specific lines in `settings.py`:

```python
from decouple import config
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)


#Uncomment the local settings
SECRET_KEY = 'your-secret-key'
DEBUG = True

##Use SQLite for local testing (already configured by default):

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

##Comment out PostgreSQL deployment code:

# DATABASES = {
#     'default': dj_database_url.config(
#         conn_max_age=600,
#         ssl_require=True
#     )
# }

##Disable WhiteNoise if you face static file issues during development:

# 'whitenoise.middleware.WhiteNoiseMiddleware',

##Setup Instructions
Clone the repository:
#git clone https://github.com/Mdhelaluddin3391/Breachxpress.git
#cd Breachxpress
#pip install -r requirements.txt
#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver

Feel free to reach out if you want to contribute, face any issues, or need guidance:
Md. Helal Uddin
Email: mdhelaluddin3391@gmail.com
GitHub: @Mdhelaluddin3391


##Acknowledgments
CS50x — for the opportunity and knowledge.
Django documentation and community.
Open-source contributors who built CKEditor and other tools.









