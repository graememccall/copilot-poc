# Retro Gaming Collection

This project is a Python application that allows users to create, edit, and delete records in a MariaDB database related to a retro gaming collection. It provides a simple API built with Flask to manage game records.

## Project Structure

```
retro-gaming-collection
├── src
│   ├── app.py          # Entry point of the application
│   ├── db.py           # Database connection handling
│   ├── models.py       # Data models for the gaming collection
│   └── routes.py       # API routes for managing game records
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .env                 # Environment variables
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/retro-gaming-collection.git
   cd retro-gaming-collection
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   - Create a `.env` file in the root directory and add your MariaDB connection details:
     ```
     DB_HOST=your_host
     DB_USER=your_username
     DB_PASSWORD=your_password
     DB_NAME=your_database
     ```

5. **Run the application:**
   ```
   python src/app.py
   ```

## Usage Examples

- **Create a new game record:**
  Send a POST request to `/games` with the game details in JSON format.

- **Edit an existing game record:**
  Send a PUT request to `/games/<id>` with the updated game details.

- **Delete a game record:**
  Send a DELETE request to `/games/<id>`.

- **Retrieve the list of games:**
  Send a GET request to `/games`.

## Contributing

Feel free to submit issues or pull requests to improve the project.