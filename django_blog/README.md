# Django Blog Project - Alx_DjangoLearnLab

A comprehensive blogging platform built with Django that supports user authentication, profile management, and full CRUD (Create, Read, Update, Delete) operations for blog posts.

## Features

### 1. User Authentication System
*   **User Registration:** New users can create an account with a username and email.
*   **User Login/Logout:** Secure authentication using Django's built-in auth system.
*   **Profile Management:** Users have a personalized profile where they can update their bio and profile picture.
*   **Automatic Profile Creation:** Uses Django Signals to create a Profile instance automatically whenever a new User is registered.

### 2. Blog Post Management (CRUD)
*   **List View:** View all blog posts on the home page in reverse chronological order.
*   **Detail View:** Read the full content of individual blog posts.
*   **Create Post:** Authenticated users can write and publish new blog posts.
*   **Update Post:** Authors can edit the title and content of their own posts.
*   **Delete Post:** Authors can remove their own posts after a confirmation step.

## Permissions and Security
*   **CSRF Protection:** All forms include `{% csrf_token %}` to prevent Cross-Site Request Forgery.
*   **Authentication Mixins:** 
    *   `LoginRequiredMixin` ensures only logged-in users can create, edit, or delete posts.
    *   `UserPassesTestMixin` ensures that only the **original author** of a post has permission to update or delete it.
*   **Public Access:** Anyone (including anonymous guests) can view the list of posts and individual post details.

## Setup Instructions

### Prerequisites
*   Python 3.7+
*   MySQL Server

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Obinna32/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/django_blog

2. Set up a virtual environment and install dependencies:
code
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
pip install django pymysql
```

3. Database Configuration:
Update django_blog/settings.py with your MySQL credentials. Ensure you have created a database named django_blog in MySQL.
Apply migrations:
code
```Bash
python manage.py makemigrations
python manage.py migrate
```
Run the development server:
code
```Bash
python manage.py runserver
```
