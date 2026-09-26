# FoodRescue — Deployment Diagram

## 4.7 Deployment Diagram

The Deployment Diagram represents the runtime environment of the FoodRescue system and shows where the major software components are executed.

The initial implementation is designed as a web-based application consisting of a client browser, a Flask application server, and a MySQL database server.

## 4.7.1 Deployment Nodes

### Client Device

The client device runs a modern web browser through which donors, recipients, volunteers, and administrators access FoodRescue.

### Application Server

The application server runs the FoodRescue Flask application.

It contains:

- Flask application
- Authentication and authorization
- Route/controller layer
- Business services
- SQLAlchemy data-access layer
- PyMySQL database driver

### Database Server

The database server runs MySQL and stores persistent FoodRescue data.

The database contains information related to:

- Users
- Donors
- Recipients
- Volunteers
- Food listings
- Food requests
- Allocations
- Notifications
- Transaction and history data

## 4.7.2 Communication

The client browser communicates with the Flask application through HTTP.

The Flask application communicates with the MySQL database through the configured database connection using SQLAlchemy and PyMySQL.

## 4.7.3 Initial Deployment Environment

For the initial college-project implementation, the application and database may run on the same development computer.

The logical deployment remains:

Client Browser
→ Flask Application
→ MySQL Database

The architecture can later be deployed across separate machines or cloud infrastructure without changing the core logical structure.