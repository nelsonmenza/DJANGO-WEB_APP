# Merchex - Django CRUD Practice Project

**Project Name:** Merchex

**App:** Listings

Merchex is a Django project developed as a practice exercise to understand and implement CRUD (Create, Read, Update, Delete) operations in Django. The project includes an app named "listings" that allows you to perform CRUD operations on Bands and Listings. Please note that this project doesn't have any styling and is intended to be enhanced in the future.

## Installation

To get Merchex up and running, follow these simple steps:

1. **Clone the Repository**:

   ```
   git clone https://github.com/nelsonmenza/DJANGO-WEB_APP.git
   ```

2. **Create a Virtual Environment** (recommended):

   It's a good practice to work within a virtual environment to isolate project dependencies.

   ```
   python -m venv merchex-env
   ```

3. **Activate the Virtual Environment**:

   - On Windows:

     ```
     merchex-env\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source merchex-env/bin/activate
     ```

4. **Navigate to the Project Directory**:

   ```
   cd merchex
   ```

5. **Install Project Dependencies**:

   ```
   pip install -r requirements.txt
   ```

6. **Migrate the Database**:

   ```
   python manage.py migrate
   ```

7. **Create a Superuser** (for admin access):

   ```
   python manage.py createsuperuser
   ```

## Usage

To use the Merchex project for CRUD operations on Bands and Listings, follow these steps:

1. Start the Django development server:

   ```
   python manage.py runserver
   ```

2. Open your web browser and navigate to `http://localhost:8000/` to access the Merchex project.

3. You can perform Create, Read, Update, and Delete operations on Bands and Listings through the web interface.

## Roadmap

This project currently lacks any styling and is in its early stages. Future enhancements may include:

- Adding a user authentication system
- Improving the user interface and styling
- Implementing additional features and functionality

Feel free to contribute to the project or use it as a starting point for your Django CRUD projects!

## License

This project is licensed under the [MIT License](LICENSE).

---

*Please note that this README is a template and should be customized to suit your project's specific details.*