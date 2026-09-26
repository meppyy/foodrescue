# FoodRescue — Activity Diagrams

## 3.3 Activity Diagrams

Activity diagrams represent the flow of major workflows within the FoodRescue system.

### 3.3.1 Donor Food Listing

The Donor Food Listing activity diagram represents the process of creating and validating a surplus-food listing.

Source:
`activity donor listing.puml`

### 3.3.2 Recipient Food Request

The Recipient Food Request activity diagram represents the process through which an eligible recipient browses available surplus food, selects a listing, specifies the required quantity, and submits a food request.

The system validates the listing availability and requested quantity before creating the request with a `Pending` status.

Source:
`recipient request.puml`

### 3.3.3 Request Approval and Allocation

The Request Approval and Allocation activity diagram represents the process through which a submitted food request is reviewed by an authorized donor or administrator.

An approved request is checked against the available food quantity before an allocation is created. Once the allocation is created, the request proceeds to pickup coordination.

Source:
`request allocation.puml`

### 3.3.4 Pickup and Delivery

The Pickup and Delivery activity diagram represents the physical-transfer workflow after a food allocation has been approved.

The system assigns an available volunteer, schedules the pickup, records food collection, tracks the delivery process, and records recipient confirmation after successful delivery.

The workflow also accounts for volunteer rejection or unavailability, food becoming unavailable before pickup, and failed delivery.

Source:
`pickup delivery.puml`