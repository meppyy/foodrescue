# FoodRescue — Context Diagram

## 3.1 Context Diagram

The Context Diagram provides a high-level view of the FoodRescue system by representing the system as a single process and identifying the external actors that interact with it.

### External Actors

- Donor
- Recipient
- Volunteer
- Administrator

### Primary Information Flows

#### Donor ↔ FoodRescue
- Registration and authentication information
- Food listing information
- Request decisions
- Handover confirmation
- Listing and donation status
- Notifications
- Impact statistics

#### Recipient ↔ FoodRescue
- Registration and profile information
- Search and filtering requests
- Food requests
- Cancellation and receipt confirmation
- Available food information
- Request and allocation status
- Notifications

#### Volunteer ↔ FoodRescue
- Availability information
- Assignment acceptance/rejection
- Pickup and delivery status
- Pickup and delivery confirmation
- Assignment information
- Notifications

#### Administrator ↔ FoodRescue
- User management actions
- Recipient verification decisions
- Listing and request management
- Issue and dispute management
- Category and system management
- User, transaction, and impact information
- Reports and statistics