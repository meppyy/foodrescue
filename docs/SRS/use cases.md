# FoodRescue — Use Cases

## 2.6 Use Cases

### 2.6.1 Donor Use Cases

| ID | Use Case | Actor | Purpose |
|---|---|---|---|
| UC-D01 | Register Account | Donor | Create a donor account |
| UC-D02 | Login | Donor | Access the donor functions |
| UC-D03 | Manage Profile | Donor | View and update donor information |
| UC-D04 | Create Food Listing | Donor | Register available surplus food |
| UC-D05 | Edit Food Listing | Donor | Modify eligible listing information |
| UC-D06 | Cancel Food Listing | Donor | Cancel an available listing |
| UC-D07 | View Active Listings | Donor | View currently managed listings |
| UC-D08 | View Requests | Donor | View requests submitted for listings |
| UC-D09 | Approve Request | Donor | Approve a suitable food request |
| UC-D10 | Reject Request | Donor | Reject a food request |
| UC-D11 | Confirm Handover | Donor | Confirm that food has been handed over |
| UC-D12 | View Donation History | Donor | Review completed donation activity |
| UC-D13 | View Impact Statistics | Donor | View relevant redistribution statistics |

### 2.6.2 Recipient Use Cases

| ID | Use Case | Actor | Purpose |
|---|---|---|---|
| UC-R01 | Register Account | Recipient | Create a recipient account |
| UC-R02 | Login | Recipient | Access recipient functions |
| UC-R03 | Manage Profile | Recipient | View and update recipient information |
| UC-R04 | Browse Food | Recipient | View available surplus food |
| UC-R05 | Search Food | Recipient | Find suitable food listings |
| UC-R06 | Filter Food | Recipient | Narrow listings using available criteria |
| UC-R07 | View Food Details | Recipient | View detailed listing information |
| UC-R08 | Request Food | Recipient | Submit a request for available food |
| UC-R09 | Cancel Request | Recipient | Cancel an eligible request |
| UC-R10 | Track Request | Recipient | View the current status of a request |
| UC-R11 | View Allocation | Recipient | View approved food allocations |
| UC-R12 | Confirm Receipt | Recipient | Confirm delivered food was received |
| UC-R13 | View Request History | Recipient | Review previous requests and receipts |

### 2.6.3 Volunteer Use Cases

| ID | Use Case | Actor | Purpose |
|---|---|---|---|
| UC-V01 | Register Account | Volunteer | Create a volunteer account |
| UC-V02 | Login | Volunteer | Access volunteer functions |
| UC-V03 | Manage Availability | Volunteer | Provide availability information |
| UC-V04 | View Assignments | Volunteer | View assigned pickup and delivery tasks |
| UC-V05 | Accept Assignment | Volunteer | Accept an available assignment |
| UC-V06 | Reject Assignment | Volunteer | Reject an assignment where permitted |
| UC-V07 | View Pickup Details | Volunteer | View pickup information |
| UC-V08 | Update Pickup Status | Volunteer | Update the progress of a pickup |
| UC-V09 | Confirm Pickup | Volunteer | Confirm food collection |
| UC-V10 | View Delivery Details | Volunteer | View delivery information |
| UC-V11 | Update Delivery Status | Volunteer | Update delivery progress |
| UC-V12 | Confirm Delivery | Volunteer | Confirm food delivery |
| UC-V13 | View Assignment History | Volunteer | Review completed assignments |

### 2.6.4 Administrator Use Cases

| ID | Use Case | Actor | Purpose |
|---|---|---|---|
| UC-A01 | Login | Administrator | Access administrative functions |
| UC-A02 | Manage Users | Administrator | View and manage system users |
| UC-A03 | Verify Recipient | Administrator | Approve or reject recipient registration |
| UC-A04 | Manage Donor Accounts | Administrator | Manage donor accounts |
| UC-A05 | Manage Volunteer Accounts | Administrator | Manage volunteer accounts |
| UC-A06 | Monitor Food Listings | Administrator | Monitor listings across the system |
| UC-A07 | Remove Invalid Listing | Administrator | Remove invalid food listings |
| UC-A08 | Monitor Requests | Administrator | Monitor food requests |
| UC-A09 | Monitor Allocations | Administrator | Monitor allocations |
| UC-A10 | Monitor Deliveries | Administrator | Monitor pickup and delivery activity |
| UC-A11 | Manage Issues / Disputes | Administrator | Review and address reported issues |
| UC-A12 | Manage Categories | Administrator | Manage food categories |
| UC-A13 | View Reports | Administrator | View system reports |
| UC-A14 | View System Statistics | Administrator | View overall system statistics |
| UC-A15 | Manage Notifications / Settings | Administrator | Manage relevant system settings |

### 2.6.5 Core System Use-Case Relationships

The major FoodRescue workflow can be represented through the following sequence of use cases:

```Create Food Listing
        ↓
Validate Listing
        ↓
Prioritize Food
        ↓
Match Suitable Recipients
        ↓
Request Food
        ↓
Review Request
        ↓
Approve Request
        ↓
Create Allocation
        ↓
Assign Volunteer
        ↓
Schedule Pickup
        ↓
Confirm Pickup
        ↓
Update Delivery
        ↓
Confirm Delivery
        ↓
Record Completed Redistribution
        ↓
Update Impact Statistics 
```