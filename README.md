# Simple Notes Application

## Overview

Simple Notes is a Flask-based web application that allows users to create, store, and manage notes. It's designed as a demonstration project showcasing various aspects of modern web application development, including Docker containerization, database interactions, and security considerations.

## Features

- Create and view notes
- Support for both MariaDB and SQLite databases
- Dockerized for easy deployment
- Admin interface for note management
- API for programmatic interaction
- Authentication for protected routes
- Configurable via environment variables
- Comprehensive logging

## Technologies Used

- Python 3.12
- Flask web framework
- Mariadb for database interactions
- Docker for containerization
- SQLite (optional) for local development

## Getting Started

### Prerequisites

- Docker
- Git

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/python-demo-app.git
   cd $_
   ```

2. Build the Docker image:
   ```
   docker build -t python-demo-app .
   ```

3. Run the container:
   ```
   docker run -p 5000:5000 python-demo-app
   ```

4. Access the application at `http://localhost:5000`

## Configuration

The application can be configured using the following environment variables:

- `DB_ROOT_PWD`: Database root password
- `NOTES_DB_DATABASE`: Name of the database to use
- `NOTES_DB_BACKEND`: Choose between 'mariadb' or 'local' (SQLite)
- `NOTES_ING_PATH`: Ingress path for the application

## Development

To set up a development environment:

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python run.py
   ```

## Testing

1. Run the unit tests with:
   ```
   python -m unittest tests/test_db.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flask community for the excellent web framework
- Docker for containerization technology
- All contributors who have helped shape this project