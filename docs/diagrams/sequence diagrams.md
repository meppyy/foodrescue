# FoodRescue — Sequence Diagrams

## 3.5 Sequence Diagrams

Sequence diagrams represent the chronological interactions between FoodRescue users, application components, services, and the database during important system workflows.

### 3.5.1 Donor Creates Food Listing

Represents the process of entering, validating, storing, and prioritizing a new surplus-food listing.

Source:
`seq donor listing.puml`

### 3.5.2 Recipient Requests Food

Represents the process of browsing available food, validating a requested quantity, creating a request, and notifying the donor.

Source:
`seq recipient request.puml`

### 3.5.3 Request Approval and Allocation

Represents the review of a pending request, validation of available quantity, creation of an allocation, and notification of the recipient.

Source:
`seq request allocation.puml`

### 3.5.4 Pickup and Delivery

Represents volunteer assignment, pickup confirmation, transit, delivery, and recipient receipt confirmation.

Source:
`seq pickup delivery.puml`

### 3.5.5 Food Expiry Handling

Represents periodic expiry checks, urgency classification, expiration of listings, cancellation of affected requests, and notifications.

Source:
`seq expiry handling.puml`