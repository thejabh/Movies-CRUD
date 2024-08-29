Here's the revised `README.md` file content, reflecting the use of MySQL and the absence of Jinja2:

---

markdown
# Movie Management Application

This is a Flask-based web application for managing a collection of movies. The application allows users to add, edit, delete, and filter movies based on various criteria like genres, actors, and technicians.

## Features

### 1. Add Movie
- Users can add a new movie by entering details such as the movie's name, release year, rating, genres, actors, and technicians (e.g., director, producer).

### 2. Edit Movie
- Users can edit an existing movie's details including the movie's name, release year, rating, genres, actors, and technicians.

### 3. Delete Movie
- Users can delete a movie from the collection. A confirmation prompt is shown before deletion.

### 4. Filter Movies
- Users can filter the list of movies based on specific genres, actors, or technicians to find movies matching their criteria.

### 5. Delete Unassociated Actors
- A special operation to delete actors from the database who are not associated with any movie. This helps in keeping the database clean from unnecessary entries.

## Technologies Used

- **Flask:** Web framework used to develop the application.
- **SQLAlchemy:** ORM (Object Relational Mapper) used for database operations.
- **MySQL:** Database used for storing movies, actors, genres, and technicians.
- **Bootstrap:** CSS framework used for styling the web pages.

## Setup Instructions

### Prerequisites

- Python 3.x
- Flask
- SQLAlchemy
- MySQL

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/moviemanagementapp.git
   ```
2. Navigate to the project directory:
   ```bash
   cd moviemanagementapp
   ```
3. Install the required Python packages:
   ```bash
   pip install Flask Flask-SQLAlachemy sqlalchemy mysqlclient==1.4.6
   ```
4. Set up your MySQL database and update the `SQLALCHEMY_DATABASE_URI` in the Flask app configuration to match your MySQL database credentials.
5. Run the application:
   ```bash
   flask run
   ```
   The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

### Adding a Movie
- Click on the **Add Movie** button, fill in the details, and click **Save**.

### Editing a Movie
- Click the **Edit** button next to the movie you want to update, modify the details, and click **Update**.

### Deleting a Movie
- Click the **Delete** button next to the movie you want to remove. Confirm the deletion when prompted.

### Filtering Movies
- Use the filter options available on the page to filter movies by genre, actors, or technicians.

### Deleting Unassociated Actors
- Click the **Delete Unassociated Actors** button to remove actors who are not linked to any movies.

## Deployment

The application is hosted on PythonAnywhere and can be accessed at the following URL:

https://thejabh.pythonanywhere.com/

To deploy this application on PythonAnywhere, follow these steps:

1. Sign up or log in to PythonAnywhere.
2. Upload your project files.
3. Set up a virtual environment and install the required dependencies using the requirements.txt file.
4. Configure the web application with the correct Flask and MySQL settings.
5. Reload the web app to apply the changes.

## Acknowledgements

- Flask documentation
- Bootstrap documentation
- SQLAlchemy documentation
