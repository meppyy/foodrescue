# FoodRescue — Class Diagram

## 4.5 Class Diagram

The Class Diagram represents the major software classes of the FoodRescue system, their important attributes, operations, and relationships.

The diagram is designed around the major domain entities and business services defined during requirements and system design.

## 4.5.1 Main Domain Classes

### User

Represents a registered system user and contains common authentication and account information.

### Donor

Represents a user who provides surplus food.

### Recipient

Represents a user or organization that can receive surplus food.

### Volunteer

Represents a user who assists with pickup and delivery.

### FoodListing

Represents a surplus-food listing created by a donor.

### FoodRequest

Represents a request submitted by a recipient for a food listing.

### Allocation

Represents the allocation of an approved food request and its associated pickup/delivery coordination.

### Notification

Represents an in-app notification generated for a user.

## 4.5.2 Service Classes

### AuthenticationService

Handles authentication, user access, and authorization-related operations.

### FoodListingService

Handles creation, validation, updating, cancellation, and status management of food listings.

### PrioritizationService

Calculates food priority using predefined rule-based criteria.

### MatchingService

Identifies and ranks suitable recipients using predefined matching criteria.

### RequestService

Handles food requests, request validation, approval/rejection, and allocation creation.

### DeliveryService

Handles volunteer assignment, pickup, delivery, and related status transitions.

### ExpiryService

Monitors food listings and processes expiry-related events.

### NotificationService

Creates and manages system notifications.

### ImpactService

Calculates and provides redistribution and impact statistics.

## 4.5.3 Design Principle

Domain classes represent persistent business data, while service classes contain reusable business operations.

This separation keeps business logic out of the presentation layer and supports modularity, maintainability, and testing.