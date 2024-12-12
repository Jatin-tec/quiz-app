# Quiz App

This is a simple Django-based quiz application where authenticated users can take a quiz by answering multiple-choice questions. It ensures that no question is repeated during a session, allows skipping questions and provides a detailed result showing correct, incorrect and unanswered questions.

## Features

- User authentication.
- Start a new quiz session.
- Fetch random multiple-choice questions from the database.
- Prevent repetition of questions in a session.
- Option to skip questions.
- View detailed results including:
  - Total questions answered.
  - Correct and incorrect submissions.
  - Unanswered questions.
- User-friendly Bootstrap-based UI.

## Deployed Link

The application is deployed and can be accessed [here](https://quiz-app-0tzb.onrender.com/).

### Demo User

- **Username:** `jatin`
- **Password:** `1234`

## Screenshots

### Login Page
![Login Page](/assets/login.png)

### Quiz Question
![Quiz Question](/assets/questions.png)

### Results Page
![Results Page](/assets/result.png)

## Setup Instructions

Follow the steps below to run the application locally.

### Prerequisites

- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Installation Steps

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Jatin-tec/quiz-app.git
    cd quiz-app

2. **Create and Activate a Virtual Environment:**
    ```python
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install Dependencies:**
    ```python
    pip install -r requirements.txt

4. **Apply Migrations:**
    ```python
    python manage.py makemigrations
    python manage.py migrate

5. **Run the Development Server:**
    ```python
    python manage.py runserver

### Sample Data

A demo user and some questions have already been added to the deployed link. To add more questions locally:

    Log in to the Django admin interface at http://127.0.0.1:8000/admin/.
    Add new questions under the Question model.
