# FoodRescue — State Diagrams

## 3.6 State Diagrams

State diagrams represent the lifecycle of important FoodRescue entities and the transitions that occur when specific system or user events take place.

### 3.6.1 Food Listing State

The Food Listing State Diagram represents the lifecycle of a surplus-food listing from creation through availability, request, allocation, collection, delivery, expiry, or cancellation.

Source:
`stae food listing.puml`

### 3.6.2 Food Request State

The Food Request State Diagram represents the lifecycle of a recipient's request from submission through approval, allocation, completion, rejection, cancellation, or expiry.

Source:
`stae food request.puml`

### 3.6.3 Pickup / Delivery Assignment State

The Pickup / Delivery Assignment State Diagram represents the lifecycle of a volunteer assignment from assignment creation through scheduled pickup, collection, transit, delivery, failure, reassignment, or cancellation.

Source:
`state delivery assignment.puml`