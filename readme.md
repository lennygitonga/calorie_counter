# Calorie Counter

A Django web application that allows users to track their daily calorie intake.

## Features
- Add food items with name, serving size, calories and meal type
- AI-powered calorie lookup using Groq API
- View total calories consumed today
- Meal breakdown by type (Breakfast, Lunch, Dinner, Snack)
- Remove individual food items
- Reset the daily calorie count

## Tech Stack
- Python 3.14
- Django 6.0.5
- PostgreSQL
- Tailwind CSS
- Groq AI API

## Local Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd calorie_counter
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/Scripts/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a .env file in the root folder
```
GROQ_API_KEY=your_groq_api_key_here
SECRET_KEY=your_secret_key_here
```

### 5. Configure PostgreSQL
Create a database called `calorie_db` in PostgreSQL, then update the `DATABASES` setting in `calorie_project/settings.py` with your local credentials.

### 6. Run migrations
```bash
python manage.py migrate
```

### 7. Start the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Deployment

The project is deployed on Render. The following environment variables are required on the hosting platform:

- `SECRET_KEY` - A secure random string
- `DATABASE_URL` - PostgreSQL connection URL
- `GROQ_API_KEY` - Your Groq API key
- `PYTHON_VERSION` - Python version to use

## Security Notes
- Secret keys and API keys are stored in environment variables and never committed to version control
- The `.env` file is listed in `.gitignore`
- Django CSRF protection is enabled on all forms