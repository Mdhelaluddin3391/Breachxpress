# BreachXpress
**BreachXpress** is a web application developed as the final project for CS50x 2025, built using Django. It provides a secure, anonymous platform for users to expose corruption and share stories in the pursuit of justice and transparency, without fear of identity disclosure.

**Author**: Md. Helal Uddin, Dharmanagar, INDIA  
**Video Demo**: [https://youtube.com/watch?v=VjofDCMohfQ](https://youtube.com/watch?v=VjofDCMohfQ)  
**Live Demo**: [https://breachxpress-8jag.onrender.com](https://breachxpress-8jag.onrender.com)

## Motivation
In many parts of the world, individuals hesitate to report corruption due to fear of retaliation. BreachXpress addresses this critical issue by offering a platform where users can submit stories anonymously, without any login system or tracking mechanisms. The goal is to empower whistleblowers and foster transparency in communities where speaking out is risky. The project leverages Django’s robust security features to ensure user privacy and a mobile-friendly interface to make it accessible to all. Developing BreachXpress was both challenging and rewarding—integrating CKEditor for rich text editing required optimizing performance for mobile devices, which I achieved through careful CSS and JavaScript adjustments. This project reflects my passion for using technology to drive social good, inspired by CS50’s emphasis on impactful programming.

## Features
- **Anonymous Story Submission**: Users can submit stories using a rich text editor (CKEditor) without providing any personal information.
- **Admin Review System**: Administrators can review submissions in a secure dashboard and choose to publish them publicly.
- **Responsive Design**: The platform is optimized for both desktop and mobile devices, ensuring accessibility.
- **No Cookies or Tracking**: No user data is stored, prioritizing anonymity.
- **File Upload Protection**: Limits large file uploads to maintain performance and security.
- **Community Section** (in development): A planned feature to allow users to collaborate and support each other’s stories.

## Project Structure
- **Breach/**: Core Django application directory.
  - **models.py**: Defines the `Story` model with fields for content (text), submission_date (timestamp), and is_published (boolean for admin approval).
  - **views.py**: Handles HTTP requests for the homepage, story submission, admin dashboard, and public story display.
  - **urls.py**: Maps URL routes to corresponding views (e.g., `/submit/` for story submission, `/admin/` for the dashboard).
  - **templates/**: Contains HTML templates:
    - `index.html`: Homepage with project overview and navigation.
    - `submit.html`: Form with CKEditor for story submission.
    - `admin.html`: Admin dashboard for reviewing and publishing stories.
    - `stories.html`: Public page displaying approved stories.
  - **static/**: Stores CSS, JavaScript, and CKEditor files for styling and functionality.
- **manage.py**: Django’s command-line utility for running migrations and the development server.
- **db.sqlite3**: SQLite database for local development, storing stories and admin data.
- **requirements.txt**: Lists dependencies, including Django, django-ckeditor, and WhiteNoise.

## Technologies Used
- **Django**: Backend framework for secure and scalable web development.
- **HTML/CSS/JavaScript**: Frontend structure, styling, and interactivity.
- **SQLite**: Lightweight database for local development (PostgreSQL planned for production).
- **CKEditor**: Rich text editor for user-friendly story submission.
- **Render**: Cloud platform for deploying the live demo.

## Design Choices
Several design decisions shaped BreachXpress:
- **Anonymity Over Authentication**: I chose not to implement a login system to prioritize user privacy, even though it meant forgoing features like user-specific story tracking. This aligns with the project’s mission to protect whistleblowers.
- **SQLite vs. PostgreSQL**: SQLite was used for local development due to its simplicity and zero-configuration setup. For production, I plan to upgrade to PostgreSQL for better scalability and concurrent access, as SQLite may struggle with high traffic.
- **CKEditor Integration**: I debated using a simple textarea to reduce dependencies but opted for CKEditor to provide users with formatting options (e.g., bold, lists). To address performance concerns, I minimized CKEditor’s bundle size and optimized static file delivery with WhiteNoise.
- **Mobile-First Design**: Ensuring responsiveness was critical, as many users may access the platform on mobile devices. I used CSS media queries and tested extensively on various screen sizes.

## How to Submit a Story
1. Navigate to the **Submit Story** page via the website’s navigation bar.
2. Use the **CKEditor** interface to write or format your story (e.g., bold, italics, bullet points).
3. Click the **Submit** button to send your story anonymously. No personal information is collected, ensuring complete privacy.

## Setup Instructions
To run BreachXpress locally, ensure you have **Python 3.8+**, **Git**, and a virtual environment tool installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/Mdhelaluddin3391/BreachXpress.git
   cd BreachXpress
```

### Install dependencies:
```python
   pip install -r requirements.txt
```

### Apply database migrations:
```python
   python manage.py makemigrations
   python manage.py migrate
```

### Start the development server:
```
   python manage.py runserver
```

Open http://localhost:8000 in your browse

If static files (e.g., CSS, JavaScript) don’t load, ensure DEBUG = True in settings.py and run:

### Settings Configuration
## Local Development
```python
   SECRET_KEY = 'your-secret-key'
   DEBUG = True
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Comment out production-specific settings (e.g., decouple, PostgreSQL, WhiteNoise):

```python
   # from decouple import config
   # SECRET_KEY = config('SECRET_KEY')
   # DEBUG = config('DEBUG', default=True, cast=bool)
   # DATABASES = {
   #     'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
   # }
   # 'whitenoise.middleware.WhiteNoiseMiddleware',

```

### Contact
For contributions, issues, or questions, 
contact:Email: mdhelaluddin3391@gmail.com
GitHub: Mdhelaluddin3391

### Acknowledgments
CS50x: For providing an incredible learning experience and inspiring this project.
Django Community: For comprehensive documentation and support.
CKEditor: For the open-source rich text editor.
Render: For reliable deployment hosting.



