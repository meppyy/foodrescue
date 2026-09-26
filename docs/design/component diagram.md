# FoodRescue — Component Diagram

## 4.6 Component Diagram

The Component Diagram represents the major software components of the FoodRescue system and the dependencies between them.

The components are organized according to the system architecture and module structure defined during system design.

## 4.6.1 Major Components

### Frontend Component

Provides the web interface through which users interact with FoodRescue.

### Authentication and Authorization Component

Handles user authentication, sessions, role-based access control, and protected functionality.

### Food Listing Component

Handles creation, validation, modification, cancellation, and status management of food listings.

### Search and Filtering Component

Provides browsing, searching, filtering, and sorting of available food listings.

### Prioritization Component

Calculates food priority using predefined rule-based criteria.

### Recipient Matching Component

Identifies and ranks potentially suitable recipients using predefined matching criteria.

### Request and Allocation Component

Handles food requests, request validation, approval or rejection, and allocation creation.

### Pickup and Delivery Component

Handles volunteer assignment, pickup scheduling, pickup confirmation, delivery tracking, and delivery confirmation.

### Expiry Management Component

Checks active food listings and handles urgency classification and expiry processing.

### Notification Component

Generates and stores in-app notifications associated with system events.

### Dashboard and Impact Component

Provides role-specific dashboards, system statistics, and impact information.

### Administration Component

Provides administrative functions for users, listings, requests, deliveries, disputes, categories, reports, and system management.

### Data Access Component

Provides database access through SQLAlchemy and PyMySQL.

### MySQL Database Component

Provides persistent storage for FoodRescue data.

## 4.6.2 Component Dependencies

The primary dependency flow is:

Frontend
→ Application Components
→ Business Services
→ Data Access
→ MySQL Database

The Notification component is used by workflow components when system events require notifications.

The Dashboard and Impact component consumes relevant operational and transaction data.

The Administration component interacts with the components it is authorized to monitor or manage.