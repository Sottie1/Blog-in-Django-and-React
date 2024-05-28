# Blog in Django and React

## Overview
This project is a full-stack web application combining Django for the backend and React for the frontend. It allows users to create, read, update, and delete blog posts. The application features a modern web interface and robust backend services.

**Note:** This project is currently in development. Features and functionality are subject to change.

## Features
- **Blog Management:** Create, update, delete, and view blog posts.
- **User Authentication:** Secure login and registration system.
- **Responsive Design:** Mobile-friendly layout using React.

## Installation

### Prerequisites
- Python 3.x
- Node.js
- Django
- React

### Backend Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/Sottie1/Blog-in-Django-and-React.git
    ```
2. Navigate to the backend directory:
    ```bash
    cd Blog-in-Django-and-React/Backend
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv myvenv
    ```
4. Activate the virtual environment:
    ```bash
    # On Windows
    myvenv\Scripts\activate

    # On Mac/Linux
    source myvenv/bin/activate
    ```
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
6. Run database migrations:
    ```bash
    python manage.py migrate
    ```
7. Start the development server:
    ```bash
    python manage.py runserver
    ```

### Frontend Setup
1. Navigate to the frontend directory:
    ```bash
    cd ../Frontend
    ```
2. Install the required packages:
    ```bash
    npm install
    ```
3. Start the development server:
    ```bash
    npm start
    ```

## Usage
1. Backend server runs at `http://127.0.0.1:8000/`.
2. Frontend server runs at `http://localhost:3000/`.
3. Register a new user or log in with an existing account.
4. Start creating and managing blog posts.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- Django Documentation
- React Documentation
- Bootstrap for front-end components
