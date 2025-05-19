# BreachXpress

## Description
BreachXpress is a web application developed as the final project for CS50’s Introduction to Computer Science. It serves as a platform for individuals to anonymously expose corruption and injustices, promoting transparency and justice for humanity. Users can submit stories of corruption or misconduct through the "Submit Story" page without revealing their identity, ensuring their safety and privacy. To maintain anonymity, the application avoids user authentication, cookies, or any form of tracking. Submitted stories are stored on the server and published for public viewing. A community section, currently under development, will allow users to collaborate and discuss submissions.

## Features
- Anonymous story submission through the "Submit Story" page
- Rich text editing for submissions using CKEditor
- Server-side storage and publication of submitted stories
- Community section (in development) for user collaboration and discussion
- No login, cookies, or tracking to prioritize user anonymity

## Technologies Used
- **Backend**: Python, Django
- **Database**: SQLite (with plans to upgrade to PostgreSQL)
- **Frontend**: HTML, CSS, JavaScript
- **Editor**: CKEditor for rich text input
- **Version Control**: Git, GitHub

## Installation and Setup
To run BreachXpress locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Mdhelaluddin3391/Breachxpress.git



Navigate to the project directory:
   cd Breachxpress

Install dependencies:
   pip install -r requirements.txt

Apply database migrations:
   python manage.py migrate

Run the development server:
   python manage.py runserver

Open http://127.0.0.1:8000 in your browser to access the application.


Project Structure:
Breachxpress/: Main project directory
   Breach/: Django app containing core logic (views, URLs, models, templates, etc.)
   manage.py: Django management script
      templates/: HTML templates for rendering pages
      static/: CSS, JavaScript, and other static assets
   db.sqlite3: SQLite database file
   requirements.txt: List of Python dependencies

usage:
Visit the "Submit Story" page to compose and submit a story using the CKEditor interface.
Submitted stories are saved on the server and made publicly accessible.
The community section (under development) will allow users to engage with others and discuss published stories.


Challenges Faced:
Integrating CKEditor for rich text editing was initially challenging but resolved by following the official CKEditor documentation.
Ensuring complete user anonymity while maintaining functionality required careful design, achieved by eliminating authentication and tracking mechanisms.
Minor issues during development, such as configuring Django models, were addressed using Google searches and Django’s official documentation.

Future Improvements:
Upgrade the database to PostgreSQL for better performance and scalability
Complete the community section to enable user collaboration and discussion
Implement moderation tools to review stories before publication
Enhance the user interface with advanced CSS and JavaScript features
Add multilingual support to make the platform accessible to a global audience

Credits:
CS50 for providing an outstanding learning experience
Django documentation for guiding backend development
CKEditor for enabling rich text editing
GitHub for hosting the project repository


