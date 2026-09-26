# FoodRescue — System Requirements

## 2.5 System Requirements

### 2.5.1 Hardware Requirements

The following hardware is recommended for local development and execution of the FoodRescue system:

- Processor: Dual-core processor or better
- RAM: Minimum 4 GB, with 8 GB or more recommended for development
- Storage: At least 5 GB of available space for the project, development tools, dependencies, and database
- Network: Internet connectivity for package installation, GitHub access, and other online development activities

### 2.5.2 Software Requirements

The FoodRescue system requires the following software:

- OS: Windows, Linux, or macOS
- Code Editor / IDE: Visual Studio Code
- Programming Language: Python
- Backend Framework: Flask
- Frontend Technologies: HTML, CSS, JavaScript
- UI Framework: Bootstrap
- Database Management System: MySQL
- Database ORM: SQLAlchemy
- Database Driver: PyMySQL
- API Testing Tool: Postman
- Version Control: Git
- Remote Repository: GitHub
- Web Browser: A modern web browser such as Google Chrome, Mozilla Firefox, or Microsoft Edge

### 2.5.3 Python Environment

The backend shall use a dedicated Python virtual environment to isolate project dependencies from the system-wide Python installation.

The project shall maintain its Python dependencies in a `requirements.txt` file.

### 2.5.4 Database Requirements

The system shall use a MySQL relational database for persistent storage.

The database shall store information required for system entities and transactions, including:

- Users
- Donors
- Recipients
- Volunteers
- Food listings
- Food requests
- Allocations
- Notifications
- Relevant transaction and history data

### 2.5.5 Development Environment

The project shall be developed and maintained using Git for version control and GitHub for remote repository management.

The source code, documentation, diagrams, tests, and other project artifacts shall be organized within the FoodRescue repository.

### 2.5.6 Application Runtime Requirements

The application shall require:

- A running Flask backend
- A running MySQL server
- A configured FoodRescue database
- A supported web browser
- Network access where required by the application environment