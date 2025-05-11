# Project 1: Recipe Book

This is a Django project for a Recipe Book app where users can create recipe categories and add recipes with ingredients, instructions, and cooking time.

## Project Setup

1. Create a virtual environment:
   ```
   python -m venv env
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     .\\env\\Scripts\\activate
     ```
   - On macOS/Linux:
     ```
     source env/bin/activate
     ```

3. Install Django:
   ```
   pip install django
   ```

4. Create a new Django project:
   ```
   django-admin startproject recipe_book .
   ```

5. Run initial migrations:
   ```
   python manage.py migrate
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

The project is now set up and ready for app creation.
