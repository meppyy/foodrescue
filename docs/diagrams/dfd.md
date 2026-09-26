# FoodRescue — Data Flow Diagrams

## 3.4 Data Flow Diagrams

Data Flow Diagrams represent the movement of information between external actors, system processes, and data stores within the FoodRescue system.

## 3.4.1 Level 0 DFD

The Level 0 DFD provides a high-level representation of the FoodRescue system and shows the major data exchanged between the system and its four primary external actors:

- Donor
- Recipient
- Volunteer
- Administrator

Source:
`dfd level 0.puml`

## 3.4.2 Level 1 DFD

The Level 1 DFD decomposes the FoodRescue system into major functional processes and shows the movement of data between external actors, internal processes, and persistent data stores.

### Major Processes

1. Authentication and User Management
2. Food Listing Management
3. Request and Allocation Management
4. Pickup and Delivery Management
5. Notification Management
6. Monitoring and Impact Management

### Major Data Stores

- D1 — User Data
- D2 — Food Listing Data
- D3 — Request and Allocation Data
- D4 — Delivery and Assignment Data
- D5 — Notification Data

The Level 1 DFD represents the major information flows involved in the FoodRescue lifecycle from food listing and requesting through allocation, pickup, delivery, notification, and impact tracking.

Source:
`dfd level 1.puml`