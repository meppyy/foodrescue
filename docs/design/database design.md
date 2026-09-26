# FoodRescue — Database Design

## 4.3 Database Design

FoodRescue will use a relational database to persist information related to users, surplus-food listings, food requests, allocations, volunteer activities, notifications, and relevant transaction history.

The database design is intended to support the major system workflows while maintaining data consistency, avoiding unnecessary duplication, and allowing the system to be extended in the future.

## 4.3.1 Database Entities

The initial database design consists of the following primary entities:

1. User
2. Donor
3. Recipient
4. Volunteer
5. FoodListing
6. FoodRequest
7. Allocation
8. Notification


## 4.3.2 User Entity

The User entity stores common authentication and account information.

| Attribute | Description |
|---|---|
| user_id | Unique identifier for the user |
| name | User's name |
| email | User's email address |
| password | Stored user password |
| phone | User's phone number |
| role | Assigned user role |
| status | Current account status |
| created_at | Account creation timestamp |

Primary Key:

`user_id`


## 4.3.3 Donor Entity

The Donor entity stores information specific to users who provide surplus food.

| Attribute | Description |
|---|---|
| donor_id | Unique donor identifier |
| user_id | Associated user account |
| organization_name | Donor organization name |
| address | Donor address |

Primary Key:

`donor_id`

Foreign Key:

`user_id → User.user_id`


## 4.3.4 Recipient Entity

The Recipient entity stores information about users or organizations that receive surplus food.

| Attribute | Description |
|---|---|
| recipient_id | Unique recipient identifier |
| user_id | Associated user account |
| organization_name | Recipient organization name |
| verification_status | Recipient verification state |
| address | Recipient address |

Primary Key:

`recipient_id`

Foreign Key:

`user_id → User.user_id`


## 4.3.5 Volunteer Entity

The Volunteer entity stores information required for pickup and delivery assignments.

| Attribute | Description |
|---|---|
| volunteer_id | Unique volunteer identifier |
| user_id | Associated user account |
| availability | Volunteer availability information |
| service_area | Geographic service area |

Primary Key:

`volunteer_id`

Foreign Key:

`user_id → User.user_id`


## 4.3.6 FoodListing Entity

The FoodListing entity stores information about surplus food provided by donors.

| Attribute | Description |
|---|---|
| listing_id | Unique food-listing identifier |
| donor_id | Donor who created the listing |
| food_name | Name of the food |
| category | Food category |
| quantity | Available quantity |
| preparation_time | Food preparation time |
| listing_time | Time the listing was created |
| expiry_time | Expiry or use-by time |
| location | Pickup location |
| dietary_type | Dietary classification |
| status | Current listing status |

Primary Key:

`listing_id`

Foreign Key:

`donor_id → Donor.donor_id`

The listing status shall support the defined FoodRescue lifecycle:

- Draft
- Available
- Requested
- Allocated
- Pickup Pending
- Collected
- Delivered
- Expired
- Cancelled


## 4.3.7 FoodRequest Entity

The FoodRequest entity stores requests submitted by recipients for available food.

| Attribute | Description |
|---|---|
| request_id | Unique request identifier |
| listing_id | Food listing being requested |
| recipient_id | Recipient submitting the request |
| requested_quantity | Quantity requested |
| request_time | Time the request was submitted |
| status | Current request status |

Primary Key:

`request_id`

Foreign Keys:

`listing_id → FoodListing.listing_id`

`recipient_id → Recipient.recipient_id`

The request status shall support:

- Pending
- Approved
- Rejected
- Cancelled
- Allocated
- Completed
- Expired


## 4.3.8 Allocation Entity

The Allocation entity stores the result of an approved food request and the information required for pickup and delivery coordination.

| Attribute | Description |
|---|---|
| allocation_id | Unique allocation identifier |
| request_id | Associated food request |
| volunteer_id | Assigned volunteer |
| pickup_time | Scheduled or recorded pickup time |
| delivery_time | Scheduled or recorded delivery time |
| status | Current allocation status |

Primary Key:

`allocation_id`

Foreign Keys:

`request_id → FoodRequest.request_id`

`volunteer_id → Volunteer.volunteer_id`


## 4.3.9 Notification Entity

The Notification entity stores system-generated notifications.

| Attribute | Description |
|---|---|
| notification_id | Unique notification identifier |
| user_id | User receiving the notification |
| message | Notification message |
| type | Notification type |
| read_status | Whether the notification has been read |
| created_at | Notification creation timestamp |

Primary Key:

`notification_id`

Foreign Key:

`user_id → User.user_id`


## 4.3.10 Entity Relationships

The initial relationships derived from the entity references are:

### User → Donor

A user account can be associated with a donor profile.

### User → Recipient

A user account can be associated with a recipient profile.

### User → Volunteer

A user account can be associated with a volunteer profile.

### Donor → FoodListing

A donor can create food listings.

### FoodListing → FoodRequest

A food listing can receive food requests.

### Recipient → FoodRequest

A recipient can submit food requests.

### FoodRequest → Allocation

An approved food request can result in an allocation.

### Volunteer → Allocation

A volunteer can be assigned to allocations.

### User → Notification

A user can receive notifications.

## 4.3.11 High-Level Relationship Structure

The database relationships can be summarized as:

User
  ├── Donor
  ├── Recipient
  ├── Volunteer
  └── Notification

Donor
  └── FoodListing

FoodListing
  └── FoodRequest

Recipient
  └── FoodRequest

FoodRequest
  └── Allocation

Volunteer
  └── Allocation

## 4.3.12 Database Design Goals

The database shall be designed to:

1. Maintain data consistency between related entities.
2. Support the complete surplus-food lifecycle.
3. Prevent invalid references between entities.
4. Support role-based application workflows.
5. Store sufficient historical information for reporting and impact tracking.
6. Allow future system expansion without major structural changes.