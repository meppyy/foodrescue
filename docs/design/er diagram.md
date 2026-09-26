# FoodRescue — ER Diagram

## 4.4 ER Diagram

The Entity Relationship Diagram represents the logical structure of the FoodRescue database by showing its major entities, attributes, primary keys, foreign keys, and relationships.

The ER diagram is derived from the database design and represents how information is related across the major FoodRescue workflows.

## 4.4.1 Main Entities

The ER diagram contains the following entities:

- User
- Donor
- Recipient
- Volunteer
- FoodListing
- FoodRequest
- Allocation
- Notification

## 4.4.2 Key Relationships

### User — Donor

A user account may be associated with a donor profile.

### User — Recipient

A user account may be associated with a recipient profile.

### User — Volunteer

A user account may be associated with a volunteer profile.

### Donor — FoodListing

A donor can create multiple food listings.

### FoodListing — FoodRequest

A food listing can receive multiple food requests.

### Recipient — FoodRequest

A recipient can submit multiple food requests.

### FoodRequest — Allocation

An approved food request may result in an allocation.

### Volunteer — Allocation

A volunteer can handle multiple pickup and delivery allocations over time.

### User — Notification

A user can receive multiple system notifications.

## 4.4.3 Keys

Primary keys uniquely identify records within each entity.

Foreign keys establish references between related entities and maintain referential relationships within the database.

Source:
`er diagram.puml`