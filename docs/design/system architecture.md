# FoodRescue — System Architecture

## 4.1 System Architecture

FoodRescue will use a layered web application architecture in which presentation, application logic, data access, and persistent storage are separated into distinct layers.

The architecture is designed to support modularity, maintainability, role-based access control, and future expansion.

## 4.1.1 Architecture Layers

### 1. Presentation Layer

The Presentation Layer provides the user interface through which donors, recipients, volunteers, and administrators interact with the system.

Technologies:

- HTML
- CSS
- JavaScript
- Bootstrap

Responsibilities:

- Display pages and dashboards
- Collect user input
- Display validation and system messages
- Submit requests to the backend
- Display system responses

### 2. Application Layer

The Application Layer contains the main application functionality and business logic of FoodRescue.

Technology:

- Python Flask

Responsibilities:

- Process incoming requests
- Authenticate users
- Enforce role-based authorization
- Execute business rules
- Manage food listings
- Process food requests
- Handle allocations
- Coordinate pickup and delivery workflows
- Generate notifications
- Apply prioritization and matching rules
- Handle expiry-related operations

### 3. Data Access Layer

The Data Access Layer manages communication between the application and the database.

Technologies:

- SQLAlchemy
- PyMySQL

Responsibilities:

- Create, read, update, and delete persistent data
- Execute database queries
- Manage database transactions
- Map application objects to database entities
- Maintain consistent access to stored data

### 4. Database Layer

The Database Layer provides persistent storage for FoodRescue.

Technology:

- MySQL

The database will store information related to:

- Users
- Donors
- Recipients
- Volunteers
- Food listings
- Food requests
- Allocations
- Notifications
- Transaction and history data

## 4.1.2 Supporting Components

### Authentication and Authorization

Responsible for:

- User authentication
- Session management
- Role-based access control
- Protected routes

### Business Services

Responsible for reusable application logic such as:

- Food prioritization
- Recipient matching
- Expiry processing
- Allocation validation
- Notification generation

### API / Route Layer

Responsible for receiving requests from the frontend and returning appropriate responses.

### Database

Responsible for persistent storage and retrieval of application data.

## 4.1.3 High-Level Data Flow

The general request flow is:

User
→ Frontend
→ Flask Route / Controller
→ Business Service
→ Data Access Layer
→ MySQL

The response follows the reverse path:

MySQL
→ Data Access Layer
→ Business Service
→ Flask Route / Controller
→ Frontend
→ User

## 4.1.4 Architecture Principles

The architecture shall follow these principles:

1. Separation of concerns
2. Modular design
3. Role-based access control
4. Reusable business services
5. Centralized database access
6. Maintainability
7. Extensibility